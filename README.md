# 점자의 소리
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

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정 방법에 대해 기술)

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
* Model1 (문장 단위 인식)
  
  ![image](https://github.com/myreporthjh/SoB/assets/148738904/391502b5-9ae0-4190-8759-55ead0889873)

* Model2 (점자 요소 세부인식)
  
  ![image](https://github.com/myreporthjh/SoB/assets/148738904/b521e63c-c238-4b6d-9254-59c4871171ff)

* 글자조합
  
  ![image](https://github.com/myreporthjh/SoB/assets/148738904/d5eded26-05e8-47cd-b519-004dd2c8cc9c)


## Appendix
[점자 일람표](http://www.hsb.or.kr/client/visually/visually2_7.asp)
