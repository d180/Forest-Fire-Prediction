import Adafruit_DHT
import RPi.GPIO as GPIO
import time
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)
smoke_sensor=0
count1=5
humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
while count1 < 0:
    if humidity is not None and temperature is not None:
        smoke_sensor=GPIO.input(17)
        if smoke_sensor == 0:
            GPIO.output(14,GPIO.HIGH)
        print(smoke_sensor)
        
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    count1-=1
    time.sleep(3)
    
print(humidity)
print(temperature)
