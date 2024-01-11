from socket import *
from os.path import exists
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('10.10.15.125', 8018))

print('연결에 성공했습니다.')
# filename = input('전송할 파일 이름을 입력하세요: ')
#filename = 'test.png'
#clientSock.sendall(filename.encode('utf-8'))
img_filename = 'test.png'



img_data = clientSock.recv(1024)
img_data_transferred = 0

if not img_data:
    print('파일 %s 가 서버에 존재하지 않음' %img_filename)
    sys.exit()

print('다운받을 파일 이름 : ', img_filename)
nowdir = os.getcwd()
with open(nowdir+"/"+img_filename, 'wb') as img_f:  #현재dir에 filename으로 파일을 받는다
    try:
        while img_data:         #데이터가 있을 때까지
            img_f.write(img_data)   #1024바이트 쓴다
            img_data_transferred += len(img_data)
            img_data = clientSock.recv(1024) #1024바이트를 받아 온다
            if not img_data:
                break
    except Exception as img_ex:
        print(img_ex)
eof_signal = clientSock.recv(3).decode('utf-8')
if eof_signal == "EOF":
    print('파일 %s 받기 완료. 전송량 %d' %(img_filename, img_data_transferred))
clientSock.close()

"""
txt_filename = 'text.txt'
txt_data_transferred = 0

if not exists(txt_filename):
    print('파일 %s 가 존재하지 않음' %txt_filename)
    sys.exit()

print("파일 %s 전송 시작" %txt_filename)
with open(txt_filename, 'rb') as txt_f:
    try:
        txt_data = txt_f.read(1024) #1024바이트 읽는다
        while txt_data: #데이터가 없을 때까지
            txt_data_transferred += clientSock.send(txt_data) #1024바이트 보내고 크기 저장
            txt_data = txt_f.read(1024) #1024바이트 읽음
    except Exception as txt_ex:
        print(txt_ex)
print("전송완료 %s, 전송량 %d" %(txt_filename, txt_data_transferred))
"""