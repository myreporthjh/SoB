main.py -- 최종 라즈베리 파이에서 사용
gpio button, webcam, espeak, socket통신 연결
btn1을 누르면 웹캠에서 이미지를 저장한 뒤 서버로 데이터 전송
btn2를 누르면 서버에서 txt파일을 가져온 뒤 espeak로 출력

server.py - 컴퓨터에서 사용
socket통신으로 연결
멀티 쓰레딩으로 이미지 받기와 텍스트파일 전송을 나눠놓음
사용 전 포트와 ip 수정확인!! 2곳이니 둘다 확인!!
