import crop_image       # model1으로 DETECTION된 이미지 CROP
import find_word        # model2로 CROP된 이미지를 받아서 바이너리 값 추출후 글자로 변환
import change_hangul    # 한글 변환 로직
import server           # 소켓 통신 서버 로직

## Socket : image 받아오기
server.execute_recv_img_thread()

## model1 : 전체 이미지 불러와서 점자 영역 crop하고 저장
crop_image.model1_demo()

## model2 : crop된 이미지에서 2x3 영역으로 단어 찾고 바이너리 값 txt파일로 저장
find_word.model2_demo()

## txt 바이너리 파일 -> 한글로 변환
change_hangul.convert()

## Socket : text 전송
server.execute_send_txt_thread()
