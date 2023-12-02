# mqtt_alarm.py
import paho.mqtt.client as mqtt
import time
import os
import sound_detector

def on_connect(client, userdata, flags, rc):
    client.subscribe("led", qos=0)
    client.subscribe("tmp", qos=0)
    client.subscribe("hum", qos=0)
    print("Connected with result code "+str(rc))
    client.subscribe("alarm/topic")

def on_message(client, userdata, msg):
    if msg.topic == "led":
        on_off = int(msg.payload)  # on_off는 0 또는 1의 정수
        sound_detector.controlLED(on_off)  # LED를 켜거나 끔

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    # 사운드센서
    soundlevel = sound_detector.measure_soundlevel()  # 사운드 센서로부터 사운드값 읽기
    client.publish('sound', payload=str(soundlevel))  # 읽은 사운드값을 'sound' 토픽에 publish

    #온습도센서
    sensor = sound_detector.sensor  # sound_detector.py에서 선언된 센서 객체
    tmp = sound_detector.measure_temperature(sensor)  # 센서 객체를 인자로 전달
    hum = sound_detector.measure_Humidity(sensor)  # 센서 객체를 인자로 전달
    tmp = sound_detector.measure_temperature(sensor)
    hum = sound_detector.measure_Humidity(sensor)
    client.publish('tmp', payload=str(tmp))
    client.publish('hum', payload=str(hum))
    time.sleep(2)

client.loop_stop()
client.disconnect()
