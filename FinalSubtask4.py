#!/usr/bin/env python3

#####################################
# imports
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor

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
#####################################
# Driving Speed Configs
LDriver=SpeedPercent(-20)
RDriver=SpeedPercent(-20.31)

#####################################
LeftMotor.reset()
RightMotor.reset()
gyro.reset()
#####################################
ev3functions.Lift_Down()
ev3functions.cforward(1.4)
ev3functions.Lift_Up()
ev3functions.turn(90, 'ccw')
ev3functions.cforward(3)
ev3functions.turn(176, 'ccw')
ev3functions.Lift_Down()
ev3functions.cforward(2.5)
ev3functions.Lift_Up()
ev3functions.cbackward(1)
ev3functions.turn(94, 'ccw')
ev3functions.cforward(72)
ev3functions.Lift_Down()
ev3functions.cbackward(1)
ev3functions.Lift_Up()
ev3functions.cbackward(3)
ev3functions.Lift_Down()

