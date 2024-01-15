main.py -- 최종 라즈베리 파이에서 사용
gpio button, webcam, espeak, socket통신 연결
btn1을 누르면 웹캠에서 이미지를 저장한 뒤 서버로 데이터 전송
btn2를 누르면 서버에서 txt파일을 가져온 뒤 espeak로 출력

# GPIO 설치
```shell
pip apt-get install python3-rpi.gpio
```

# 웹캠 설치 및 Opencv 설치
```shell
lsusb
```
로 웹캠 위치 확인

![webcam1](https://mblogthumb-phinf.pstatic.net/MjAyMTA3MjlfMTQ1/MDAxNjI3NDg2OTAzMjc4.go3bDFBSByDGBuy_Ks--Dl1m2FsDL0-ZiCfcLG4FWe8g.PsEGHwI-H14Vn5HFWATAcmXHAPlPGhpIvI7TWLggMrQg.PNG.chgy2131/image.png?type=w800)

![webcam2](https://mblogthumb-phinf.pstatic.net/MjAyMTA3MjlfMjMx/MDAxNjI3NDg2OTIyMzM5.U0Txmh66jsXJGX102DKbXWKoTF3R8MXwhlEP0UKBhvYg.Mg9GuTjxhxFjFsqqlUKhxsc-zuxQDaUrM_Qd-G6Xj4og.PNG.chgy2131/image.png?type=w800)

```shell
sudo apt-get install fswebcam
```
![webcam3](https://mblogthumb-phinf.pstatic.net/MjAyMTA3MjlfMTgz/MDAxNjI3NDg3MDE4MTkz.Hr14HMlg80wdzabESDA23dTWquq14IzvlcN0UkvESWUg.XS6bGCH82RYboFomaqk5BpIXRgmvBoJKM88WBo1B8qsg.PNG.chgy2131/image.png?type=w800)
![webcam4](https://mblogthumb-phinf.pstatic.net/MjAyMTA3MjlfOTYg/MDAxNjI3NDg3MDIzODk2.75fXi8FbMJXiKE-V-SN3Vf61U0P8-4vmm109c_WsH4Mg.QL2fYuNm4gAVjXnYZelP3MugbzlCYIQXqd5A6sUA9RYg.PNG.chgy2131/image.png?type=w800)
![webcam5](https://mblogthumb-phinf.pstatic.net/MjAyMTA3MjlfMjAz/MDAxNjI3NDg3MDI4NzEy.R54n9UaZ0grGixdZ5sbUIXcPu6pLlqnigHfakpZ0XE8g.4y2xA8KQvOG_eo1W3QYwSWhFs6CpzG3MA2pS2ppK7y8g.PNG.chgy2131/image.png?type=w800)

# gtts설치
```shell
pip apt-get install gtts
```
gtts는 google text to speech모델로 인터넷과 연결되어서 사용한다.

# Socket 통신을 위한 socket설치
```shell
﻿sudo apt-get install socket
```

server.py - 컴퓨터에서 사용
socket통신으로 연결
멀티 쓰레딩으로 이미지 받기와 텍스트파일 전송을 나눠놓음
사용 전 포트와 ip 수정확인!! 2곳이니 둘다 확인!!


# Socket 통신을 위한 socket설치
```shell
﻿sudo apt-get install socket
```
