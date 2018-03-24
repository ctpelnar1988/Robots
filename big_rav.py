import RPi.GPIO as GPIO
import time
from time import sleep
import pygame

pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

### SENSORS
GPIO_TRIGGER = 14

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

ECHOS = {"ECHO_LEFT": 15, "ECHO_MIDDLE": 18, "ECHO_RIGHT": 23}
for e in ECHOS:
  GPIO.setup(ECHOS[e], GPIO.IN)

### MOTORS

## FRONT RIGHT
Motor_FrontR_1 = 6
Motor_FrontR_2 = 13
Motor_FrontR_Enable = 5

GPIO.setup(Motor_FrontR_1, GPIO.OUT)
GPIO.setup(Motor_FrontR_2, GPIO.OUT)
GPIO.setup(Motor_FrontR_Enable, GPIO.OUT)

## BACK RIGHT
Motor_BackR_3 = 26
Motor_BackR_4 = 21
Motor_BackR_Enable = 19

GPIO.setup(Motor_BackR_3, GPIO.OUT)
GPIO.setup(Motor_BackR_4, GPIO.OUT)
GPIO.setup(Motor_BackR_Enable, GPIO.OUT)

## FRONT LEFT
Motor_FrontL_1 = 24
Motor_FrontL_2 = 22
Motor_FrontL_Enable = 25

GPIO.setup(Motor_FrontL_1, GPIO.OUT)
GPIO.setup(Motor_FrontL_2, GPIO.OUT)
GPIO.setup(Motor_FrontL_Enable, GPIO.OUT)

## BACK LEFT
Motor_BackL_3 = 16
Motor_BackL_4 = 12
Motor_BackL_Enable = 20

GPIO.setup(Motor_BackL_3, GPIO.OUT)
GPIO.setup(Motor_BackL_4, GPIO.OUT)
GPIO.setup(Motor_BackL_Enable, GPIO.OUT)

def distance(e):
  GPIO.output(GPIO_TRIGGER, True)
  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  StartTime = time.time()
  StopTime = time.time()
  while GPIO.input(e) == 0:
    StartTime = time.time()

  while GPIO.input(e) == 1:
    StopTime = time.time()

  TimeElapsed = StopTime - StartTime
  distance = (TimeElapsed * 34300) / 2
  return distance

def run_distance():
  sensors = []
  for e in ECHOS:
    dist = distance(ECHOS[e])
    sensors.append({"{}".format(e): "{}".format(dist)})
    time.sleep(0.3)
  print("{}".format(sensors))

def backward():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.HIGH)
  GPIO.output(Motor_FrontR_2, GPIO.LOW)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.LOW)
  GPIO.output(Motor_BackR_4, GPIO.HIGH)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_1, GPIO.HIGH)
  GPIO.output(Motor_FrontL_2, GPIO.LOW)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_3, GPIO.LOW)
  GPIO.output(Motor_BackL_4, GPIO.HIGH)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)


def forward():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.LOW)
  GPIO.output(Motor_FrontR_2, GPIO.HIGH)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.HIGH)
  GPIO.output(Motor_BackR_4, GPIO.LOW)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_1, GPIO.LOW)
  GPIO.output(Motor_FrontL_2, GPIO.HIGH)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_3, GPIO.HIGH)
  GPIO.output(Motor_BackL_4, GPIO.LOW)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def right():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.HIGH)
  GPIO.output(Motor_FrontR_2, GPIO.LOW)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.LOW)
  GPIO.output(Motor_BackR_4, GPIO.HIGH)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_1, GPIO.LOW)
  GPIO.output(Motor_FrontL_2, GPIO.HIGH)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_3, GPIO.HIGH)
  GPIO.output(Motor_BackL_4, GPIO.LOW)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def left():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.LOW)
  GPIO.output(Motor_FrontR_2, GPIO.HIGH)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.HIGH)
  GPIO.output(Motor_BackR_4, GPIO.LOW)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_1, GPIO.HIGH)
  GPIO.output(Motor_FrontL_2, GPIO.LOW)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_3, GPIO.LOW)
  GPIO.output(Motor_BackL_4, GPIO.HIGH)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def stop():
  GPIO.output(Motor_FrontR_Enable, GPIO.LOW)
  GPIO.output(Motor_BackR_Enable, GPIO.LOW)
  GPIO.output(Motor_FrontL_Enable, GPIO.LOW)
  GPIO.output(Motor_BackL_Enable, GPIO.LOW)

if __name__ == '__main__':
  try:
    while True:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.JOYBUTTONDOWN:
          if j.get_button(3):
            print("Moving Forward")
            forward()
          elif j.get_button(1):
            print("Moving Backward")
            backward()
          elif j.get_button(2):
            print("Moving Right")
            right()
          elif j.get_button(0):
            print("Moving Left")
            left()
        elif event.type == pygame.JOYBUTTONUP:
          stop()
          print("Listening...")
  except KeyboardInterrupt:
    print("Shutting Down and Cleaning Up")
    GPIO.cleanup()
