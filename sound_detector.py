# sound_detector.py
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
soundpin = 19
GPIO.setup(soundpin, GPIO.IN)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

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
