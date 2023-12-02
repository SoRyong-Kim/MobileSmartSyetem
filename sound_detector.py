#sound_detector.py
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from adafruit_htu21d import HTU21D
import busio

# LED를 켜고 끄는 함수
def controlLED(on_off): 
    # led 번호의 핀에 on_off(0/1) 값 출력하는 함수
    GPIO.output(led, on_off)

# 초음파 센서를 제어하여 물체와의 거리를 측정하여 거리 값 리턴하는 함수
def measure_soundlevel():
    return GPIO.input(soundpin) # 거리 계산하여 리턴(단위 cm)

def measure_temperature(sensor): # 센서로부터 온도 값 수신 함수
    return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기
def measure_Humidity(sensor) : # 센서로부터 습도 값 수신 함수
    return float(sensor.relative_humidity) # HTU21D 장치로부터 습도 값 읽기

soundpin = 19
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(soundpin, GPIO.IN)

# LED를 다루기 위한 전역 변수 선언 및 초기화
led = 6  # GPIO6
GPIO.setup(led, GPIO.OUT)  # GPIO6 핀을 출력으로 지정

# 온습도센서
sda = 2 # GPIO2 핀. sda 이름이 붙여진 핀
scl = 3 # GPIO3 핀. scl 이름이 붙여진 핀
i2c = busio.I2C(scl, sda) # I2C 버스 통신을 실행하는 객체 생성
sensor = HTU21D(i2c) # I2C 버스에서 HTU21D 장치를 제어하는 객체 리턴
