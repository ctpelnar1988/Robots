import RPi.GPIO as GPIO
import time
from time import sleep
import pygame
import serial

pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Autonomous or Controller:
a = input("Autonomous Mode? T/F: ")
if a == "T":
    AUTONOMOUS_MODE = True
else:
    AUTONOMOUS_MODE = False

### MOTORS
FREQUENCY = 20
DUTY_CYCLE = 90
PWM_STOP = 0

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

# Set up PWM pins:
pwmMotor_FrontR_1 = GPIO.PWM(Motor_FrontR_1, FREQUENCY)
pwmMotor_FrontR_2 = GPIO.PWM(Motor_FrontR_2, FREQUENCY)
pwmMotor_BackR_3 = GPIO.PWM(Motor_BackR_3, FREQUENCY)
pwmMotor_BackR_4 = GPIO.PWM(Motor_BackR_4, FREQUENCY)
pwmMotor_FrontL_3 = GPIO.PWM(Motor_FrontL_3, FREQUENCY)
pwmMotor_FrontL_4 = GPIO.PWM(Motor_FrontL_4, FREQUENCY)
pwmMotor_BackL_1 = GPIO.PWM(Motor_BackL_1, FREQUENCY)
pwmMotor_BackL_2 = GPIO.PWM(Motor_BackL_2, FREQUENCY)

# Initial PWM Start:
pwmMotor_FrontR_1.start(PWM_STOP)
pwmMotor_FrontR_2.start(PWM_STOP)
pwmMotor_BackR_3.start(PWM_STOP)
pwmMotor_BackR_4.start(PWM_STOP)
pwmMotor_FrontL_3.start(PWM_STOP)
pwmMotor_FrontL_4.start(PWM_STOP)
pwmMotor_BackL_1.start(PWM_STOP)
pwmMotor_BackL_2.start(PWM_STOP)


def toggle_autonomous_mode(AUTONOMOUS_MODE):
    if AUTONOMOUS_MODE == True:
        AUTONOMOUS_MODE = False
    else:
        AUTONOMOUS_MODE = True
    return AUTONOMOUS_MODE

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
    #GPIO.output(Motor_FrontR_1, GPIO.HIGH)
    #GPIO.output(Motor_FrontR_2, GPIO.LOW)
    #GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

    # Back Right Motors
    #GPIO.output(Motor_BackR_3, GPIO.HIGH)
    #GPIO.output(Motor_BackR_4, GPIO.LOW)
    #GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

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
    #GPIO.output(Motor_FrontL_3, GPIO.LOW)
    #GPIO.output(Motor_FrontL_4, GPIO.HIGH)
    #GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

    # Back Left Motors
    #GPIO.output(Motor_BackL_1, GPIO.LOW)
    #GPIO.output(Motor_BackL_2, GPIO.HIGH)
    #GPIO.output(Motor_BackL_Enable, GPIO.HIGH)

def stop():
    GPIO.output(Motor_FrontR_Enable, GPIO.LOW)
    GPIO.output(Motor_BackR_Enable, GPIO.LOW)
    GPIO.output(Motor_FrontL_Enable, GPIO.LOW)
    GPIO.output(Motor_BackL_Enable, GPIO.LOW)
    
# PWM Control:

def pwm_stop():
    pwmMotor_FrontR_1.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontR_2.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackR_3.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackR_4.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontL_3.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontL_4.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackL_1.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackL_2.ChangeDutyCycle(PWM_STOP)
    
def pwm_forward():
    # Front Right Motors
    pwmMotor_FrontR_1.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontR_2.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

    # Back Right Motors
    pwmMotor_BackR_3.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackR_4.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

    # Front Left Motors
    pwmMotor_FrontL_3.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_FrontL_4.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

    # Back Left Motors
    pwmMotor_BackL_1.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_BackL_2.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_BackL_Enable, GPIO.HIGH)
    
def pwm_backward():
    # Front Right Motors
    pwmMotor_FrontR_1.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_FrontR_2.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

    # Back Right Motors
    pwmMotor_BackR_3.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_BackR_4.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_BackR_Enable, GPIO.HIGH)

    # Front Left Motors
    pwmMotor_FrontL_3.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontL_4.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

    # Back Left Motors
    pwmMotor_BackL_1.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackL_2.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_BackL_Enable, GPIO.HIGH)
    
def pwm_right():
    # Front Left Motors
    pwmMotor_FrontL_3.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_FrontL_4.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_FrontL_Enable, GPIO.HIGH)

    # Back Left Motors
    pwmMotor_BackL_1.ChangeDutyCycle(DUTY_CYCLE)
    pwmMotor_BackL_2.ChangeDutyCycle(PWM_STOP)
    GPIO.output(Motor_BackL_Enable, GPIO.HIGH)
    
def pwm_left():
    # Front Right Motors
    pwmMotor_FrontR_1.ChangeDutyCycle(PWM_STOP)
    pwmMotor_FrontR_2.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_FrontR_Enable, GPIO.HIGH)

    # Back Right Motors
    pwmMotor_BackR_3.ChangeDutyCycle(PWM_STOP)
    pwmMotor_BackR_4.ChangeDutyCycle(DUTY_CYCLE)
    GPIO.output(Motor_BackR_Enable, GPIO.HIGH)
    
def drive_autonomously():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    s = ser.readline()
    print(s)
    if b'1\r\n' == s:
        print("FORWARD!")
        pwm_forward()
    elif b'2\r\n' == s:
        pwm_stop()
        time.sleep(2)
        pwm_right()
        time.sleep(1)
        print("RIGHT!")
        pwm_stop()
        #time.sleep(2)
    elif b'3\r\n' == s:
        pwm_stop()
        time.sleep(2)
        pwm_backward()
        time.sleep(1)
        print("BACK!")
        pwm_stop()
        time.sleep(2)
    elif b'4\r\n' == s:
        pwm_stop()
        time.sleep(2)
        pwm_left()
        time.sleep(1)
        print("LEFT!")
        pwm_stop()
        time.sleep(2)
    else:
        print(s)

if __name__ == '__main__':
    try:
        while True:
            if AUTONOMOUS_MODE == True:
                drive_autonomously()
                #print("AUTONOMOUS_MODE")
            else:
                #print("DRIVER_MODE")
                events = pygame.event.get()
                for event in events:
                    if event.type == pygame.JOYBUTTONDOWN:
                        if j.get_button(3):
                            print("Moving Forward")
                            pwm_forward()
                        elif j.get_button(1):
                            print("Moving Backward")
                            pwm_backward()
                        elif j.get_button(2):
                            print("Moving Right")
                            pwm_right()
                        elif j.get_button(0):
                            print("Moving Left")
                            pwm_left()
                    elif event.type == pygame.JOYBUTTONUP:
                        pwm_stop()
                        print("Listening...")
    except KeyboardInterrupt:
        print("Shutting Down and Cleaning Up")
        pwm_stop()
        GPIO.cleanup()

