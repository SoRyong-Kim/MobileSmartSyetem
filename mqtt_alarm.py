# mqtt_alarm.py
import paho.mqtt.client as mqtt
import time
import os
import sound_detector

def on_connect(client, userdata, flags, rc):
    client.subscribe("led", qos=0)
    print("Connected with result code "+str(rc))
    client.subscribe("alarm/topic")

def on_message(client, userdata, msg):
    on_off = int(msg.payload)  # on_off는 0 또는 1의 정수
    sound_detector.controlLED(on_off)  # LED를 켜거나 끔
    if msg.topic == "alarm/topic":  # 알람 토픽인 경우
        total_seconds = int(msg.payload.decode())
        sound_detector.controlLED(0)  # 알람이 끝나면 LED 끄기
        print(f"led가 꺼집니다.")
        print(f"알람이 {total_seconds} 초 뒤에 알람이 울립니다")
        sound_detector.controlLED(1)  # 알람이 울리기 시작하면 LED 켜기
        time.sleep(total_seconds)
        os.system('cvlc /home/pi/static/alarm.mp3 --play-and-exit')
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    soundlevel = sound_detector.measure_soundlevel()  # 사운드 센서로부터 사운드값 읽기
    if soundlevel == 1:
        client.publish("sound", "sound detected")  # “sound” 토픽으로 사운드센서 값 전송
    time.sleep(1)

client.loop_stop()
client.disconnect()
