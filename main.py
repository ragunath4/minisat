import machine
import utime
import uos

from chittiSat.mq2 import MQ2
from chittiSat.gyro import MPU6050
from chittiSat.pressure import *
from chittiSat.assistant import *
from chittiSat.sdcard import *

#I2C configuration
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1))
devices = i2c.scan()
if devices:
    print(devices)

#MQ2 sensor
#sensor = MQ2(pinData=26)
#sensor.calibrate()

#Gyro
mpu6050 = MPU6050(i2c)

#Pressure sensor
bmp280 = BMP280(i2c)
calibrate.pressure(bmp280)


while True:
        t = time.ticks_ms()/1000
        Pressure= bmp280.pressure
        temperature = bmp280.temperature
        #Smoke = sensor.readSmoke()
        #LPG = sensor.readLPG()
        #Methane = sensor.readMethane()
        #Hydrogen = sensor.readHydrogen()
        ax = round(mpu6050.accel.x, 2)
        ay = round(mpu6050.accel.y, 2)
        az = round(mpu6050.accel.z, 2)
        gx = round(mpu6050.gyro.x, 2)
        gy = round(mpu6050.gyro.y, 2)
        gz = round(mpu6050.gyro.z, 2)
        
        dashboard.sendWoair(Pressure,temperature,ax,ay,az,gx,gy,gz)


