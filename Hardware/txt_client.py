from socket import *
from os.path import exists
import os
import sys

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('10.10.15.125', 8019))

print('연결에 성공했습니다.')

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

