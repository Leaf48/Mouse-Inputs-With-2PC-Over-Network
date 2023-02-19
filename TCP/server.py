import socket
import re

import pyautogui
from pynput.mouse import Button, Controller

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
pattern = re.compile(r"\[([0-9]{0,4}),([0-9]{0,4}),(0|1),(0|1)]")

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
        right = int(res_pattern.group(3))
        left = int(res_pattern.group(4))

        print(f"x: {x} | y: {y} | right: {right} | left: {left}")
        mouse.position = (x, y)
        # pyautogui.moveTo(x, y)






    except Exception as e:
        pass
        # print(e)

conn.close()
