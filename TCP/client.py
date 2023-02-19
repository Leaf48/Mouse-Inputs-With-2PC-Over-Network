import socket
from pynput.mouse import Controller
from pynput import mouse
from time import sleep

TCP_IP = '192.168.0.76'
TCP_PORT = 25567
BUFFER_SIZE = 15

mouse_ = Controller()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

prev_x = 0
prev_y = 0

while True:
    try:
        right: int = 0
        left: int = 0

        x, y = mouse_.position
        payload = f'[{x},{y},{right},{left}]'
        # print(position)
        for i in range(2000):
            pass

        s.send(payload.encode())


    except Exception as e:
        print(e)
