import cv2
import mediapipe as mp
import serial
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

# تنظیمات Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# تنظیمات آردوینو
arduino = serial.Serial('COM3', 9600)  # پورت مناسب را جایگزین کنید

class CameraCapture(Image):
    def __init__(self, **kwargs):
        super(CameraCapture, self).__init__(**kwargs)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # به‌روزرسانی هر 30 فریم در ثانیه

    def update(self, *args):
        ret, frame = self.capture.read()
        if ret:
            finger_count = self.detect_fingers(frame)
            
            # نمایش تعداد انگشتان در تصویر
            cv2.putText(frame, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            
            # کنترل آردوینو بر اساس تعداد انگشتان
            if 0 <= finger_count <= 4:
                arduino.write(str(finger_count).encode())  # ارسال تعداد انگشتان به آردوینو

            # تبدیل تصویر به فرمت Kivy
            buf1 = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf1, colorfmt='bgr', bufferfmt='ubyte')
            self.texture = texture

    def detect_fingers(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        finger_count = 0

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # کشیدن نقاط دست
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # شمارش انگشتان
                landmarks = hand_landmarks.landmark
                thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
                index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
                middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
                ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
                pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y

                if index_tip < thumb_tip: finger_count += 1
                if middle_tip < thumb_tip: finger_count += 1
                if ring_tip < thumb_tip: finger_count += 1
                if pinky_tip < thumb_tip: finger_count += 1

        return finger_count

class FingerControlApp(App):
    def build(self):
        layout = BoxLayout()
        self.camera_capture = CameraCapture()
        layout.add_widget(self.camera_capture)
        return layout

if __name__ == "__main__":
    FingerControlApp().run()
