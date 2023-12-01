import paho.mqtt.client as mqtt
import time
import os
import sound_detector  # sound_detector 모듈 import

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("alarm/topic")

def on_message(client, userdata, msg):
    total_seconds = int(msg.payload.decode())
    print(f"알람이 {total_seconds} 초 뒤에 알람이 울립니다")
    time.sleep(total_seconds)
    os.system('cvlc /home/pi/static/alarm.mp3 --play-and-exit')

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    soundlevel = sound_detector.measure_soundlevel()
    client.publish("sound", soundlevel, qos=0)  # “sound” 토픽으로 사운드 센서 값 전송
    time.sleep(1)

client.loop_stop()  # 루프를 중지하지 않음 (계속해서 메시지 수신을 위해)
client.disconnect()  # 연결 해제하지 않음 (계속해서 메시지 수신을 위해)