# sound_detector.py
import os
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from time import sleep  # time 모듈에서 sleep 함수 import

ip = "localhost" 
client = mqtt.Client()
client.connect(ip, 1883, 60)

# LED를 켜고 끄는 함수
def controlLED(on_off): 
    # led 번호의 핀에 on_off(0/1) 값 출력하는 함수
    GPIO.output(led, on_off)

def measure_soundlevel():
    try:
        while True:
            soundlevel = GPIO.input(soundpin)
            if soundlevel == 1:
                client.publish("sound", soundlevel, qos=0)
            time.sleep(1) # 몇 초 단위로 확인할 지

    except KeyboardInterrupt:
        print("테스트 종료")
        GPIO.cleanup()
        
# LED를 다루기 위한 전역 변수 선언 및 초기화
led = 12  # GPIO6
GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정

soundpin = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정
GPIO.setup(soundpin, GPIO.IN)
