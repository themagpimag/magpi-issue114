from buildhat import Motor
from time import sleep

motor_left = Motor('A')
motor_right = Motor('B')

def stop():
  motor_left.stop()
  motor_right.stop()

def forward():
  motor_left.start(50)
  motor_right.start(-50)

def back():
    motor_left.start(-50)
    motor_right.start(50)

def left():
  motor_left.start(50)
  motor_right.start(50)

def right():
  motor_left.start(-50)
  motor_right.start(-50)

for i in range(2):
    forward()
    sleep(1)
    back()
    sleep(1)
    right()
    sleep(1)
    left()
    sleep(1)
    stop()