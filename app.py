# app.py
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import paho.mqtt.client as mqtt
import os
import threading
from time import sleep  # time 모듈에서 sleep 함수 import

app = Flask(__name__)
client = mqtt.Client()
sound_data = []

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("sound")

def on_message(client, userdata, msg):
    sound_value = int(msg.payload.decode())
    sound_data.append(sound_value)
    if len(sound_data) > 5:
        sound_data.pop(0)

client.on_connect = on_connect
client.on_message = on_message

def play_alarm(total_seconds):
    sleep(total_seconds)
    os.system('cvlc /home/pi/static/alarm.mp3 --play-and-exit')

def start_mqtt():
    client.connect("localhost", 1883, 60)
    client.loop_start()

def stop_mqtt():
    client.loop_stop()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    hours = request.form.get('hours')
    minutes = request.form.get('minutes')
    seconds = request.form.get('seconds')
    total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

    client.publish("alarm/topic", total_seconds)

    threading.Thread(target=play_alarm, args=(total_seconds,), daemon=True).start()

    return 'Alarm set for ' + hours + ' hours ' + minutes + ' minutes ' + seconds + ' seconds later.'

@app.route('/stop', methods=['POST'])
def stop():
    os.system('pkill vlc')
    return 'Alarm stopped.'

@app.route('/start_sound_measurement', methods=['GET'])
def start_sound_measurement():
    start_mqtt()
    return 'Sound measurement started.'

@app.route('/stop_sound_measurement', methods=['GET'])
def stop_sound_measurement():
    stop_mqtt()
    return str(sound_data)

@app.route('/get_sound_data', methods=['GET'])
def get_sound_data():
    return str(sound_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)
