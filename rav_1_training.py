import pygame
import RPi.GPIO as GPIO
import time

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set GPIO Pins for Motors:

### Right Motor:
Motor1A = 13
Motor1B = 6
Motor1E = 26

### Left Motor:
Motor2A = 16
Motor2B = 5
Motor2E = 22

# Set GPIO direction (IN / OUT)

### Right Motor:
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

### Left Motor:
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

# Set GPIO Pins for Sensor:

### Center Sensor:
GPIO_TRIGGER_01 = 18
GPIO_ECHO_01 = 24

# LED Light
GPIO_LED = 25


# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER_01, GPIO.OUT)
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.setup(GPIO_ECHO_01, GPIO.IN)

def distance(gpio_trigger, gpio_echo):
    # set Trigger to HIGH
    GPIO.output(gpio_trigger, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(gpio_trigger, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(gpio_echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(gpio_echo) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(gpio_echo) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return round(distance, 1)

def turn_rav_left():
    # Forward motion for Right Motor:
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    # Backward motion for Left Motor:
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

def turn_rav_right():
    # Backward motion for Right Motor:
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    # Forward motion for Left Motor:
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)


def move_rav_forward():
    print("Move rav forward")
    # Forward motion for Right Motor:
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    # Forward motion for Left Motor:
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

def stop_rav():
    print("Stop rav")
    # Stop Right Motor:
    GPIO.output(Motor1E, GPIO.LOW)
    # Stop Left Motor:
    GPIO.output(Motor2E, GPIO.LOW)
    time.sleep(2)

try:
    GPIO.output(GPIO_LED, True)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                if j.get_button(3):
                    move_rav_forward()
                elif j.get_button(0):
                    turn_rav_left()
                elif j.get_button(2):
                    turn_rav_right()
                elif j.get_button(1):
                    stop_rav()
            elif event.type == pygame.JOYBUTTONUP:
                    print("Listening...")

except KeyboardInterrupt:
    print("EXITING NOW")
    GPIO.output(GPIO_LED, False)
    stop_rav()
    j.quit()
    GPIO.cleanup()
