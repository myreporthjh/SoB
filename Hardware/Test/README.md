button.py
상위 폴더의 main.py의 전신이 되는 파일

server.py
소켓통신을 이용하여 라즈베리파이와 컴퓨터를
서버와 클라이언트로 연결하는 예제
이 예제에서는 라즈베리 파이를 서버로 뒀다.(이미지를 보내야 했어서)

client.py
소켓통신을 이용하여 라즈베리파이와 컴퓨터를
서버와 클라이언트로 연결하는 예제

espeak.py
라즈베리에서 사용하는 tts예제
하지만 음성의 성능이 좋지 않아서 사용하지않음

gpio.py
gpio를 사용하여 버튼을 라즈베리파이와 연결한 예제

gtts_test.py
google tts를 사용하여 텍스트 파일을 mp3파일로 바꾸는 예제
인터넷 연결이 필요하지만 성능이 뛰어나 이 모델을 사용하기로 결정

pyttsx3_test.py
espeak와 비슷한 성능으로 사용하지 않음

txt_client.py
txt_server.py
소켓통신을 이용해서 텍스트를 보내기 위한 예제

webcam.py
opencv를 이용하여 라즈베리파이에서 webcam을 사용하는 예제

webcamcamera.py
opencv를 이용하여 라즈베리파이에서 webcam을 사용하는 예제
위와 동일하지만 소켓통신을 이용해서 서버에서 바로바로 웹캠을 띄움

