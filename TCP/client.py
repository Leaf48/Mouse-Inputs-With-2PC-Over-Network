import socket
from pynput.mouse import Controller
from pynput import mouse
from time import sleep

usleep = lambda xx: sleep(xx / 1000000.0)

TCP_IP = '192.168.0.76'
TCP_PORT = 25567
BUFFER_SIZE = 15

mouse_ = Controller()

isLeftClicked = False
isRightClicked = False


def on_click(x_, y_, button, pressed):
    global isLeftClicked, isRightClicked
    if pressed:
        if button == button.right:
            isRightClicked = True
        if button == button.left:
            isLeftClicked = True
    elif not pressed:
        if button == button.right:
            isRightClicked = False
        if button == button.left:
            isLeftClicked = False

    if isRightClicked:
        print("RIGHT Pressed")
    elif not isRightClicked:
        print("RIGHT Not Pressed")
    if isLeftClicked:
        print("left Pressed")
    elif not isLeftClicked:
        print("left Not Pressed")

    # print("x: {} | y: {} | button: {} | pressed: {}".format(x_, y_, button, pressed))


mouse_listener = mouse.Listener(
    on_click=on_click
)
mouse_listener.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    try:
        right: int = 0
        left: int = 0

        if isRightClicked:
            right = 1
        elif not isRightClicked:
            right = 0
        if isLeftClicked:
            left = 1
        elif not isLeftClicked:
            left = 0

        x, y = mouse_.position
        payload = f'[{x},{y},{right},{left}]'
        # print(position)
        for i in range(20000):
            pass

        s.send(payload.encode())


    except Exception as e:
        print(e)
