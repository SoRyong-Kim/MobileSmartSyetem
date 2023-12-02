import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

def controlLED(on_off):
    # led 번호의 핀에 on_off(0/1) 값 출력하는 함수
    GPIO.output(led, on_off)

def measure_soundlevel():
    return GPIO.input(soundpin)

soundpin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(soundpin, GPIO.IN)

# LED를 다루기 위한 전역 변수 선언 및 초기화
led = 12  # GPIO6
GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정