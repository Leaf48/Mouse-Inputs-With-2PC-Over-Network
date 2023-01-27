import socket
import json
import pyautogui
import traceback

UDP_IP = "192.168.0.76"
UDP_PORT = 5005


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except Exception as e:
    print(traceback.format_exc())

while True:
    x, y = pyautogui.position()
    data = {"x": x, "y": y}
    print(data)
    json_data = json.dumps(data)
    try:
        sock.sendto(json_data.encode(), (UDP_IP, UDP_PORT))
    except Exception as e:
        print(traceback.format_exc())

