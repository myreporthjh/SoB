import RPi.GPIO as GPIO
import time
import cv2
import sys
import socket
import numpy as np
import threading
import os
from os.path import exists
from socket import *

from gtts import gTTS
from playsound import playsound

button_pin1 = 15                #gpio
button_pin2 = 14                #gpio
GPIO.setwarnings(False)         #gpio
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def speak():
    option = '-s 160 -p 95 -v ko+f3 -f result.txt' #tts
    os.system("espeak {}".format(option))

def speak_txt():
    with open("result.txt", "r") as sp_f:
        data = sp_f.read()

    sp = gTTS(lang = 'ko', text = data, slow=False)
    sp.save("speech.mp3")
    playsound("/home/pi/test/speech.mp3")

def send_img2server():
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('10.10.15.126', 8000))
    print('연결에 성공했습니다.(8021)')

    img_filename = 'sample.png'
    img_data_transferred = 0

    if not exists(img_filename):
        print("no file")
        sys.exit()

    print("파일 %s 전송 시작" %img_filename)
    with open(img_filename, 'rb') as img_f:
        try:
            img_data = img_f.read(1024) #1024바이트 읽는다
            while img_data: #데이터가 없을 때까지
                img_data_transferred += clientSock.send(img_data) #1024바이트 보내고 크기 저장
                img_data = img_f.read(1024) #1024바이트 읽음
        except Exception as img_ex:
            print(img_ex)
    print("전송완료 %s, 전송량 %d" %(img_filename, img_data_transferred))

def recv_txt4server():
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('10.10.15.126', 8010))
    print('연결에 성공했습니다.(8080)')

    txt_filename = 'result.txt'
    txt_data = clientSock.recv(1024)
    txt_data_transferred = 0

    if not txt_data:
        print('파일 %s 가 서버에 존재하지 않음' %txt_filename)
        sys.exit()

    nowdir = os.getcwd()
    with open(nowdir+"/"+txt_filename, 'wb') as txt_f: #현재dir에 filename으로 파일을 받는다
        try:
            while txt_data: #데이터가 있을 때까지
                txt_f.write(txt_data) #1024바이트 쓴다
                txt_data_transferred += len(txt_data)
                txt_data = clientSock.recv(1024) #1024바이트를 받아 온다
        except Exception as txt_ex:
            print(txt_ex)
    print('파일 %s 받기 완료. 전송량 %d' %(txt_filename, txt_data_transferred))

def execute_send_thread():
    send_img = send_img2server()
    send_thread = threading.Thread(target=send_img, daemon=True)
    send_thread.start()
    time.sleep(3)
    send_thread.join()

def execute_recv_thread():
    recv_txt = recv_txt4server()
    recv_thread = threading.Thread(target=recv_txt, daemon=True)
    recv_thread.start()
    time.sleep(3)
    recv_thread.join()

def main():
    cap = cv2.VideoCapture(0)       #webcam
    while True:
        ret, frame = cap.read()
        cv2.imshow('find_Braille', frame)
        if GPIO.input(button_pin1) == GPIO.HIGH\
                or cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('sample.png', frame)
            print("sample.png was saved!")
            execute_send_thread()
            continue

        if GPIO.input(button_pin2) == GPIO.HIGH:
            execute_recv_thread()
            speak_txt()
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
