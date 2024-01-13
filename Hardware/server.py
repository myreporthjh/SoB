from socket import *
from os.path import exists
import os
import sys
import time
import threading

def recv_img4client():    
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', 8019))
    serverSock.listen(1)
    print("Server On(8021)")
    connectionSock, addr = serverSock.accept()
    print(str(addr),'에서 접속했습니다')

    img_filename = 'test.png'
    img_data = connectionSock.recv(1024)
    img_data_transferred = 0

    if not img_data:
        print('파일 %s 가 서버에 존재하지 않음' %img_filename)
        sys.exit()

    nowdir = os.getcwd()
    with open(nowdir+"/"+img_filename, 'wb') as f: #현재dir에 filename으로 파일을 받는다
        try:
            while img_data: #데이터가 있을 때까지
                f.write(img_data) #1024바이트 쓴다
                img_data_transferred += len(img_data)
                img_data = connectionSock.recv(1024) #1024바이트를 받아 온다
        except Exception as ex:
            print(ex)
    print('파일 %s 받기 완료. 전송량 %d' %(img_filename, img_data_transferred))

def send_txt2client():
    serverSock = socket(AF_INET, SOCK_STREAM)
    serverSock.bind(('', 8080))
    serverSock.listen(1)
    print("Server On(8080)")
    connectionSock, addr = serverSock.accept()
    print(str(addr),'에서 접속했습니다')
    
    txt_filename = 'text.txt'
    txt_data_transferred = 0

    if not exists(txt_filename):
        print("no file")
        sys.exit()

    print("파일 %s 전송 시작" %txt_filename)
    with open(txt_filename, 'rb') as txt_f:
        try:
            txt_data = txt_f.read(1024) #1024바이트 읽는다
            while txt_data: #데이터가 없을 때까지
                txt_data_transferred += connectionSock.send(txt_data) #1024바이트 보내고 크기 저장
                txt_data = txt_f.read(1024) #1024바이트 읽음
        except Exception as txt_ex:
            print(txt_ex)
    print("전송완료 %s, 전송량 %d" %(txt_filename, txt_data_transferred))
    connectionSock.close()

def execute_recv_img_thread():
    recv_img = recv_img4client()
    recv_thread = threading.Thread(target=recv_img, daemon=True)
    recv_thread.start()
    recv_thread.join()


def execute_send_txt_thread():
    send_txt = send_txt2client()
    send_thread = threading.Thread(target=send_txt, daemon=True)
    send_thread.start()
    send_thread.join()


def main():
    execute_recv_img_thread()
    execute_send_txt_thread()

if __name__ == "__main__":
    main()