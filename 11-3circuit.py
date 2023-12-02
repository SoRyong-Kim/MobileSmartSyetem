import time
import RPi.GPIO as GPIO

# LED를 켜고 끄는 함수
def controlLED(on_off):
    # led 번호의 핀에 on_off(0/1) 값 출력하는 함수
    GPIO.output(led, on_off)

# 초음파 센서를 제어하여 물체와의 거리를 측정하여 거리 값 리턴하는 함수
def measure_sound():
    
    
    return 1

# 초음파 센서를 다루기 위한 전역 변수 선언 및 초기화
trig = 20  # GPIO20
echo = 16  # GPIO16
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)  # GPIO20 핀을 출력으로 지정
GPIO.setup(echo, GPIO.IN)  # GPIO16 핀을 입력으로 지정

# LED를 다루기 위한 전역 변수 선언 및 초기화
led = 12  # GPIO6
GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정
