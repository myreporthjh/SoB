import os
import RPi.GPIO as GPIO
import time
import cv2

import sys
import socket
import numpy as np
from socket import *
from os.path import exists

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8018))
serverSock.listen(1)

def speak(option):
    os.system("espeak {}".format(option))

cap = cv2.VideoCapture(0)       #webcam
option = '-v ko+f3 -f text.txt' #tts
button_pin1 = 15                #gpio
button_pin2 = 14                #gpio
GPIO.setwarnings(False)         #gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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
    if GPIO.input(button_pin1) == GPIO.HIGH\
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
        break
serverSock.close()
cap.release()
cv2.destroyAllWindows()


print("Here naom")
serverSock2 = socket(AF_INET, SOCK_STREAM)
serverSock2.bind(('', 8019))
serverSock2.listen(1)
connectionSock2, addr2 = serverSock2.accept()
print(str(addr2),'에서 접속했습니다')

txt_filename = 'text.txt'
txt_data_transferred = 0

#if GPIO.input(button_pin2) == GPIO.HIGH:
txt_data = connectionSock2.recv(1024)

if not txt_data:
    print('파일 %s 가 서버에 존재하지 않음' %txt_filename)
    sys.exit()

nowdir = os.getcwd()
with open(nowdir+"/"+txt_filename, 'wb') as txt_f: #현재dir에 filename으로 파일을 받는다
    try:
        while txt_data: #데이터가 있을 때까지
            txt_f.write(txt_data) #1024바이트 쓴다
            txt_data_transferred += len(txt_data)
            txt_data = connectionSock2.recv(1024) #1024바이트를 받아 온다
    except Exception as txt_ex:
        print(txt_ex)
print('파일 %s 받기 완료. 전송량 %d' %(txt_filename, txt_data_transferred))
speak(option)
if GPIO.input(button_pin2) == GPIO.HIGH:
    sys.exit()

