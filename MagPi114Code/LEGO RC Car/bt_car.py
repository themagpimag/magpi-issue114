from buildhat import Motor
from bluedot import BlueDot
from signal import pause
from gpiozero import LED

motor_left = Motor('A')
motor_right = Motor('B')
dot = BlueDot()
led_left = LED(20)
led_right = LED(21)

def stop():
    motor_left.stop()
    motor_right.stop()
    led_right.on()
    led_left.on()

def forward():
    motor_left.start(-100)
    motor_right.start(100)
    led_right.off()
    led_left.off()

def backward():
    motor_left.start(100)
    motor_right.start(-100)
    led_right.on(0.2)
    led_left.on(0.2)

def right():
    motor_left.start(-100)
    motor_right.start(-100)
    led_right.blink(0.2)
    led_left.off()

def left():
    motor_left.start(100)
    motor_right.start(100)
    led_right.off()
    led_left.blink(0.2)

def move(pos):
    if pos.top:
        forward()
    elif pos.bottom:
        backward()
    elif pos.left:
        left()
    elif pos.right:
        right()

dot.when_pressed = move
dot.when_released = stop
dot.when_moved = move

pause()
