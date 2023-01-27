import socket
import json
import traceback

import pyautogui

UDP_IP = ""
UDP_PORT = 5005

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
except Exception as e:
    print(traceback.format_exc())

while True:
    try:
        data, addr = sock.recvfrom(1024)
    except Exception as e:
        print(traceback.format_exc())

    json_data = json.loads(data.decode())
    x = json_data["x"]
    y = json_data["y"]
    print(x, y)
    pyautogui.moveTo(x, y, duration=0)
