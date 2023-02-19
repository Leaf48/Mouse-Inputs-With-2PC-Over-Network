import socket
import re

import pyautogui
from pynput.mouse import Button, Controller

import serial

arduino = serial.Serial("COM3", 115200, timeout=0.1)

mouse = Controller()

TCP_IP = ""
TCP_PORT = 25567
BUFFER_SIZE = 15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


conn, addr = s.accept()
print('Connection address:', addr)

# [111,111,right(0 or 1),left(0 or 1)]
pattern = re.compile(r"\[([0-9]{0,4}),([0-9]{0,4})]")

clickCooldown = 0
cooldown = 250

while True:
    try:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break

        r = data.decode()
        res_pattern = pattern.search(r)

        x = int(res_pattern.group(1))
        y = int(res_pattern.group(2))

        print(f"x: {x} | y: {y}")
        # x_, y_ = mouse.position
        # mouse.position = (x_ + x, y_ + y)
        # pyautogui.moveTo(x, y)
        if x == 0 and y == 0:
            pass
        else:
            arduino.write(str.encode(str(f",{x},{y}*")))






    except Exception as e:
        # pass
        print(e)

conn.close()

