import os
import RPi.GPIO as GPIO
import time
import cv2

from socket import *
from os.path import exists
import sys

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8018))
serverSock.listen(1)

def speak(option):
    os.system("espeak {}".format(option))

cap = cv2.VideoCapture(0)       #webcam
option = '-v ko+f3 -f text.txt' #tts
button_pin = 15                 #gpio
GPIO.setwarnings(False)         #gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

connectionSock, addr = serverSock.accept()  #socket
print(str(addr),'에서 접속했습니다')
img_filename = 'test.png'
data_transferred = 0
if not exists(img_filename):
    print("no file")
    sys.exit()

while True:
    ret, frame = cap.read()
    cv2.imshow('find_Braille', frame)
    if GPIO.input(button_pin) == GPIO.HIGH\
            or cv2.waitKey(1) & 0xFF == ord('q'):
        print("Button pushed!")
        
        cv2.imwrite('test.png', frame)

        print("파일 %s 전송 시작" %img_filename)
        with open(img_filename, 'rb') as f:
            try:
                data = f.read(1024) #1024바이트 읽는다
                while data: #데이터가 없을 때까지
                    data_transferred += connectionSock.send(data) #1024바이트 보내고 크기 저장
                    data = f.read(1024) #1024바이트 읽음
            except Exception as ex:
                print(ex)
        print("전송완료 %s, 전송량 %d" %(img_filename, data_transferred))


        speak(option)
        break

cap.release()
cv2.destroyAllWindows()
