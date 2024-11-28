
# FingerLightControl

A simple conceptual project that demonstrates controlling devices connected to an Arduino using hand gestures detected by a camera. This project utilizes Python for hand gesture recognition and Arduino to control the connected device.

## Overview

This project captures hand gestures using a camera, processes the image to count the number of raised fingers, and sends this information to an Arduino via serial communication. Based on the number of detected fingers, the Arduino controls the state of a connected device (e.g., an LED).

---

# FingerLightControl

یک پروژه ساده و مفهومی که کنترل دستگاه‌های متصل به آردوینو را با استفاده از حرکات دست که توسط دوربین شناسایی می‌شود، نشان می‌دهد. در این پروژه از Python برای شناسایی حرکات دست و از آردوینو برای کنترل دستگاه متصل استفاده شده است.

## مروری کلی

این پروژه با استفاده از دوربین، حرکات دست را شناسایی کرده، تصویر را پردازش می‌کند تا تعداد انگشتان دست را شمارش کند و این اطلاعات را از طریق ارتباط سریال به آردوینو ارسال می‌کند. سپس آردوینو بر اساس تعداد انگشتان شناسایی شده، وضعیت دستگاه متصل (مثلاً یک LED) را کنترل می‌کند.

---

## Requirements | پیش‌نیازها

### Software | نرم‌افزار:
- Python 3.x
- Libraries:
  - OpenCV (`cv2`)
  - Mediapipe
  - Kivy
  - pySerial
- Arduino IDE

### Hardware | سخت‌افزار:
- Arduino (e.g., Arduino Uno)
- LED or any other device connected to the Arduino
- Camera to capture hand gestures

---

## Installation & Setup | نصب و راه‌اندازی

### 1. Arduino Setup | تنظیمات آردوینو:

- Upload the `FingerLightControl.ino` code to your Arduino. This code reads the number of fingers from the serial input and controls a connected LED accordingly.

- کد `FingerLightControl.ino` را بر روی آردوینو آپلود کنید. این کد تعداد انگشتان را از ورودی سریال می‌خواند و مطابق آن یک LED متصل را کنترل می‌کند.


---

### 2. Python Setup | تنظیمات Python:

- Run the `FingerLightControl.py` file. This script captures the video feed from your camera, detects the number of fingers, and sends this count to the Arduino via serial communication.

- فایل `FingerLightControl.py` را اجرا کنید. این اسکریپت ویدئو را از دوربین شما می‌گیرد، تعداد انگشتان را شناسایی کرده و این تعداد را از طریق ارتباط سریال به آردوینو ارسال می‌کند.


---

## Usage | استفاده

1. **Upload the Arduino code:** Ensure that the Arduino is connected and upload the provided code. This will allow the Arduino to respond to the number of fingers detected by the Python script.
2. **Run the Python script:** Start the Python program, which will open the camera feed and start detecting fingers. Based on the number of fingers detected, the Arduino will control the connected device.

1. **آپلود کد آردوینو:** مطمئن شوید که آردوینو متصل است و کد را آپلود کنید. این کار باعث می‌شود آردوینو به تعداد انگشتان شناسایی شده توسط اسکریپت پایتون پاسخ دهد.
2. **اجرای اسکریپت پایتون:** برنامه پایتون را اجرا کنید که ویدئوی دوربین را باز کرده و انگشتان را شناسایی می‌کند. بر اساس تعداد انگشتان شناسایی شده، آردوینو دستگاه متصل را کنترل خواهد کرد.

<div align="center">
<img src="https://github.com/user-attachments/assets/c1554a9c-3370-4807-89b2-7502074b90b4" align="center" style="width: 100%" />
</div>  
---

## Note | نکته:

This project is primarily educational and conceptual, aimed at demonstrating how Python and Arduino can be integrated for simple gesture-based control.

این پروژه بیشتر جنبه آموزشی و مفهومی دارد و هدف آن نشان دادن نحوه یکپارچه‌سازی Python و آردوینو برای کنترل ساده مبتنی بر ژست‌های حرکتی است.

---
