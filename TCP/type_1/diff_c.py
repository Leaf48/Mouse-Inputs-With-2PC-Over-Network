from pynput.mouse import Controller
import socket
from time import sleep

mouse = Controller()

prev_x = 0
prev_y = 0

TCP_IP = '192.168.0.76'
TCP_PORT = 25567
BUFFER_SIZE = 15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    try:
        x, y = mouse.position
        x_, y_ = x, y
        # print("current", x, y)
        # print("previous", prev_x, prev_y)

        # no change
        if x == prev_x:
            x = 0
        else:
            if prev_x < x:
                x = x - prev_x
            elif x < prev_x:
                x = prev_x - x

        if y == prev_y:
            y = 0
        else:
            if prev_y < y:
                y = y - prev_y
            elif y < prev_y:
                y = prev_y - y


        # print("x: ", x, "y: ", y)


        prev_x = x_
        prev_y = y_


        # sleep(1)
        for i in range(1000000):
            pass

        if x == 0 and y == 0:
            pass
        else:
            s.send(f"[{x},{y}]".encode())


    except Exception as e:
        print(e)
        s.connect((TCP_IP, TCP_PORT))