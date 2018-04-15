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

### MOTORS

## FRONT RIGHT
Motor_FrontR_1 = 7
Motor_FrontR_2 = 12
Motor_FrontR_Enable = 8

GPIO.setup(Motor_FrontR_1, GPIO.OUT)
GPIO.setup(Motor_FrontR_2, GPIO.OUT)
GPIO.setup(Motor_FrontR_Enable, GPIO.OUT)

## BACK RIGHT
Motor_BackR_3 = 21
Motor_BackR_4 = 20
Motor_BackR_Enable = 16

GPIO.setup(Motor_BackR_3, GPIO.OUT)
GPIO.setup(Motor_BackR_4, GPIO.OUT)
GPIO.setup(Motor_BackR_Enable, GPIO.OUT)

## FRONT LEFT
Motor_FrontL_3 = 18
Motor_FrontL_4 = 15
Motor_FrontL_Enable = 14

GPIO.setup(Motor_FrontL_3, GPIO.OUT)
GPIO.setup(Motor_FrontL_4, GPIO.OUT)
GPIO.setup(Motor_FrontL_Enable, GPIO.OUT)

## BACK LEFT
Motor_BackL_1 = 24
Motor_BackL_2 = 25
Motor_BackL_Enable = 23

GPIO.setup(Motor_BackL_1, GPIO.OUT)
GPIO.setup(Motor_BackL_2, GPIO.OUT)
GPIO.setup(Motor_BackL_Enable, GPIO.OUT)

def backward():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.HIGH)
  GPIO.output(Motor_FrontR_2, GPIO.LOW)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.HIGH)
  GPIO.output(Motor_BackR_4, GPIO.LOW)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_3, GPIO.LOW)
  GPIO.output(Motor_FrontL_4, GPIO.HIGH)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_1, GPIO.LOW)
  GPIO.output(Motor_BackL_2, GPIO.HIGH)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)


def forward():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.LOW)
  GPIO.output(Motor_FrontR_2, GPIO.HIGH)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.LOW)
  GPIO.output(Motor_BackR_4, GPIO.HIGH)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_3, GPIO.HIGH)
  GPIO.output(Motor_FrontL_4, GPIO.LOW)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_1, GPIO.HIGH)
  GPIO.output(Motor_BackL_2, GPIO.LOW)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def right():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.HIGH)
  GPIO.output(Motor_FrontR_2, GPIO.LOW)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.HIGH)
  GPIO.output(Motor_BackR_4, GPIO.LOW)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_3, GPIO.HIGH)
  GPIO.output(Motor_FrontL_4, GPIO.LOW)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_1, GPIO.HIGH)
  GPIO.output(Motor_BackL_2, GPIO.LOW)
  GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def left():
  # Front Right Motors
  GPIO.output(Motor_FrontR_1, GPIO.LOW)
  GPIO.output(Motor_FrontR_2, GPIO.HIGH)
  GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

  # Back Right Motors
  GPIO.output(Motor_BackR_3, GPIO.LOW)
  GPIO.output(Motor_BackR_4, GPIO.HIGH)
  GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

  # Front Left Motors
  GPIO.output(Motor_FrontL_3, GPIO.LOW)
  GPIO.output(Motor_FrontL_4, GPIO.HIGH)
  GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

  # Back Left Motors
  GPIO.output(Motor_BackL_1, GPIO.LOW)
  GPIO.output(Motor_BackL_2, GPIO.HIGH)
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
