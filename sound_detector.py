# sound_detector.py
import os
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from time import sleep  # time 모듈에서 sleep 함수 import

# LED를 다루기 위한 전역 변수 선언 및 초기화
led = 12  # GPIO12

soundpin = 19
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.cleanup()

GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정
GPIO.setup(soundpin, GPIO.IN)

ip = "localhost" 
client = mqtt.Client()
client.connect(ip, 1883, 60)

def measure_soundlevel():
    try:
        while True:
            soundlevel = GPIO.input(soundpin)
            if soundlevel == 1:
                client.publish("sound", soundlevel, qos=0)
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("테스트 종료")
        GPIO.cleanup()
        
