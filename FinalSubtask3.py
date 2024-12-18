#!/usr/bin/env python3

#####################################
# imports
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
from ev3dev2.sound import Sound
import time


import CollisionFunction
import ev3functions

#####################################
# Motor Configs
tank= MoveTank(OUTPUT_A, OUTPUT_D)
LeftMotor=LargeMotor(OUTPUT_A)
RightMotor=LargeMotor(OUTPUT_D)
Lift=MediumMotor(OUTPUT_C)
#####################################
# Sensor Configs
Color=ColorSensor(INPUT_1)
gyro=GyroSensor(INPUT_2)
Ultra=UltrasonicSensor(INPUT_3)
sound = Sound()
#####################################
# Driving Speed Configs
LDriver=SpeedPercent(-6)
RDriver=SpeedPercent(-6)
#####################################
# Barcode Configuration:

BarcodeRead=[1]
Barcode1=[1,0,0,0]
Barcode2=[1,0,1,0]
Barcode3=[1,1,0,0]
Barcode4=[1,0,0,1]
BarcodeType=''

#####################################
# Function for reading barcode

#####################################
LeftMotor.reset()
RightMotor.reset()
gyro.reset()
Color.calibrate_white()
#####################################
Distance_To_Travel=1.5
DistancePerRotation=14.2/2
Rotations=Distance_To_Travel/DistancePerRotation


DistSegment1=0.5
DistSegment2=1
DistSegment3=1.5

Rot1=DistSegment1/DistancePerRotation
Rot2=DistSegment2/DistancePerRotation
Rot3=DistSegment3/DistancePerRotation

Location=[]


L=SpeedPercent(-20+13)
R=SpeedPercent(-20.1+13)

Recent=0

#####################################

ev3functions.cslowforward(17.75)
time.sleep(2)
LeftMotor.reset()
RightMotor.reset()
for i in range(4):
    LeftMotor.on_for_degrees(SpeedPercent(-6), 30)
    RightMotor.on_for_degrees(SpeedPercent(-6), 30)
    time.sleep(1)
    Location.append((Color.raw[0]+Color.raw[1]+Color.raw[2])/3)

    time.sleep(0.1)
time.sleep(0.1)

#for number in range(len(Location)):
#    sound.speak(str(int(Location[number])))
#sound.speak('This barcode is {0} characters long'.format(len(BarcodeRead)))
for number in range(len(Location)-1):
    if number==0:
        if 11-Location[number]<-10:
            BarcodeRead.append(0)
        else:
            BarcodeRead.append(1)
    else:
        if Location[number]-Location[number-1]<-10:
            BarcodeRead.append(0)
        else:
            BarcodeRead.append(1)
if BarcodeRead[1]==0 and BarcodeRead[2]==0 and BarcodeRead[3]==0:
    BarcodeType=1
elif BarcodeRead[2]==1:
    BarcodeType=2
elif BarcodeRead[1]==1:
    BarcodeType=3
elif BarcodeRead[3]==1:
    BarcodeType=4
else:
    BarcodeType=2
#print(BarcodeRead)
#print(BarcodeType)
#for number in range(len(BarcodeRead)):
#    if BarcodeRead[number]==0:
#        sound.speak('White')
#    elif BarcodeRead[number]==1:
#        sound.speak('Black')
#    else:
#        sound.speak('Error 1')

sound.speak('This is barcode type {0}'.format(BarcodeType))
#time.sleep(10)

