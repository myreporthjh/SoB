import os
import RPi.GPIO as GPIO
import time

button_pin = 15

def speak(option):
    os.system("espeak {}".format(option))

option = '-v ko+f3 -f text.txt'

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while(1):
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")
        speak(option)
    time.sleep(0.1)
