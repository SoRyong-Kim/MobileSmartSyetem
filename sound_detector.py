import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)
soundpin = 19
GPIO.setup(soundpin, GPIO.IN)

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    soundlevel = GPIO.input(soundpin)
    if soundlevel == 1:
        client.publish("sound", "sound detected")
    time.sleep(1)