import os

# 말하기 함수 정의
def speak(option):
    os.system("espeak {}".format(option))

# 출력 데이터 정의
drink = {
    'name' : '코카콜라',
    'price' : '1111'
}
#옵션 및 메세지 정의
option = '-v ko+f3 -f text.txt' # -v는 보이스를 의미하고 ko+f3은 한국어 3번째 목소리를, -f는 파일 text.txt는 텍스트 파일을 의미
msg = drink['name'] + '는' + str(drink['price']) + ' 원입니다.'

#말하기 실행
print('espeak', option, msg)
speak(option)
