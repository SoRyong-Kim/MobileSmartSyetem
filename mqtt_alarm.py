import paho.mqtt.client as mqtt
import time
import os
import sound_detector  # sound_detector 모듈 import

def on_connect(client, userdata, flags, rc):
    client.subscribe("led", qos=0)  # "led" 토픽으로 구독 신청

def on_message(client, userdata, msg):
    on_off = int(msg.payload)  # on_off는 0 또는 1의 정수
    sound_detector.controlLED(on_off)  # LED를 켜거나 끔 ********************

ip = "localhost"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ip, 1883, 60)
client.loop_start()

while True:
    soundlevel = sound_detector.measure_soundlevel()
    client.publish("sound", soundlevel, qos=0)  # “sound” 토픽으로 사운드 센서 값 전송
    time.sleep(1)

client.loop_stop()  # 루프를 중지하지 않음 (계속해서 메시지 수신을 위해)
client.disconnect()  # 연결 해제하지 않음 (계속해서 메시지 수신을 위해)
