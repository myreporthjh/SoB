# 점자의 소리 (Sound of Braille)
* [발표자료](https://docs.google.com/presentation/d/1WSleXYFF2FmuSL_zByKoB1HBIoQ587_Zn22ENmkoQBQ/edit?usp=sharing)
* 점자를 인식하고 문장으로 만들어서 소리로 출력하는 프로젝트
* 목표: 시각장애인용 점자 탐색 지팡이를 만드는 것

## High Level Design
![HLD drawio_final2](https://github.com/myreporthjh/SoB/assets/148738904/af0cd416-e2e8-4daa-af27-9030b0382c64)

## USE CASE
![use_case drawio](https://github.com/myreporthjh/SoB/assets/148738904/1c066193-9c47-4f00-b9b4-e904a14dce17)

## Clone code

```shell
git clone https://github.com/myreporthjh/SoB.git
```

## Prerequite

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Steps to run

```shell
source .venv/bin/activate

cd Software/
python main.py

# 소켓 통신 사용시 Hardware 부분도 같이 실행
cd Hardware/
python main.py
```

## Output
* 촬영 (라즈베리파이 + 웹캠)
  
  ![image](https://github.com/myreporthjh/SoB/assets/148738904/c22391ea-6a5c-4a52-9fc0-625cb4babc27)

* Model1 (문장 단위 인식)
  
  ![image](https://github.com/myreporthjh/SoB/assets/148738904/611d2c7d-24c1-44a1-b81d-aa5a4949b6c6)

* Model2 (점자 요소 세부인식)

  ![image](https://github.com/myreporthjh/SoB/assets/148738904/b173b04c-505b-4390-98d7-a47f901b8437)

* 글자조합

  ![image](https://github.com/myreporthjh/SoB/assets/148738904/f075f2f6-1ae9-4766-a0a7-dc408362919b)


## Appendix
[점자 일람표](http://www.hsb.or.kr/client/visually/visually2_7.asp)
