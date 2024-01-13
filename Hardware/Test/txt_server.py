from socket import *
from os.path import exists
import os
import sys

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', 8018))
serverSock.listen(1)
connectionSock, addr = serverSock.accept()
print(str(addr),'에서 접속했습니다')

txt_filename = 'text.txt'
txt_data = connectionSock.recv(1024)
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
            txt_data = connectionSock.recv(1024) #1024바이트를 받아 온다
    except Exception as txt_ex:
        print(txt_ex)
print('파일 %s 받기 완료. 전송량 %d' %(txt_filename, txt_data_transferred))