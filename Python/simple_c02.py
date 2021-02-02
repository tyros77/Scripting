# Author: tyros77
# This is a simple C02 detector for the beaglebone black utilizing an SGP20 Gas sensor
# Completed as a group project for school


import busio
import adafruit_sgp30
import board, os, keyboard
import http.client, urllib.parse, serial
import Adafruit_BBIO.UART as UART
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

#LED setup 
ledRed="P9_15"
ledGreen="P9_12"
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)

#Display setup
UART.setup("UART4")
ser = serial.Serial(port = "/dev/ttyS4", baudrate=9600)
ser.close()
ser.open()

#CO2 sensor config
i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
spg30 = adafruit_sgp30.Adafruit_SGP30(i2c)
print("Running...")
try:
    while True:
        eC02, TVOC = spg30.iaq_measure()
        #Send to ThingSpeak
        params = urllib.parse.urlencode({'field1': eC02,'key':'FWUSBNVHD94ZMTOE'})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept":"test/plan"}
        conn=http.client.HTTPConnection("api.thingspeak.com:80")
        conn.request("POST","/update",params,headers)
        res=conn.getresponse()	
        print(res.status,res.reason)
        if eC02 < 1000:
            #write to display
            dig0 = int(eC02/1000)
            dig1 = int((eC02-(dig0*1000))/100)
            dig2 = int((eC02-((dig0*1000)+(dig1*100)))/10)
            dig3 = (eC02-(((dig0*1000)+(dig1*100)+(dig2*10))))
            ser.write([0x79,0,dig0])
            ser.write([0x79,1,dig1])
            ser.write([0x79,2,dig2])
            ser.write([0x79,3,dig3])
            #Turn on Green
            GPIO.output(ledGreen, GPIO.HIGH)
            GPIO.output(ledRed, GPIO.LOW)
        else:
            dig0 = int(eC02/1000)
            dig1 = int((eC02-(dig0*1000))/100)
            dig2 = int((eC02-((dig0*1000)+(dig1*100)))/10)
            dig3 = (eC02-(((dig0*1000)+(dig1*100)+(dig2*10))))
            ser.write([0x79,0,dig0])
            ser.write([0x79,1,dig1])
            ser.write([0x79,2,dig2])
            ser.write([0x79,3,dig3])
            #Turn on blinking Red
            GPIO.output(ledGreen, GPIO.LOW)
            GPIO.output(ledRed, True)
            sleep(.01)
            GPIO.output(ledRed, False)
            sleep(.001)
except KeyboardInterrupt:
        print('Exiting..')
        #clear display, turn off light & cleanup
        GPIO.output(ledRed, False)
        GPIO.output(ledGreen, False)
        ser.write([0x76])
        ser.close()
        GPIO.cleanup()
