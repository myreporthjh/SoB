import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imwrite('test.png', frame)
cap.release()

#이 파이썬 파일 실행하면 사진 찍듯 저장함
