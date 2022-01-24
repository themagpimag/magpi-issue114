from buildhat import Motor
from time import sleep

motor_left = Motor('A')
motor_right = Motor('B')
motor_left.run_for_seconds(seconds=10, speed=50)
motor_right.run_for_seconds(seconds=10, speed=-50)