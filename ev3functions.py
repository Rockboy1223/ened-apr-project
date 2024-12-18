#!/usr/bin/env python3

#####################################
# imports
from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor, UltrasonicSensor, ColorSensor
import time
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
# Global Values

LiftSpeed=12
Up=False
L=SpeedPercent(-20)
R=SpeedPercent(-20.31)



##############################################################################################################################################
# Functions for Robot
def sturn(Direction, Currently_Facing):
    #ensure to calibrate first##########################
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    #####################################################
    LeftMotor=LargeMotor(OUTPUT_A)
    RightMotor=LargeMotor(OUTPUT_D)
    gyro=GyroSensor(INPUT_2)
    
    
    ######################################################


    if Direction=='North':
        if Currently_Facing=='North':
            print('This shouldnt happen')
        elif Currently_Facing=='East':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)

        elif Currently_Facing=='South':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        elif Currently_Facing=='West':
            TurnL=SpeedPercent(6)
            TurnR=SpeedPercent(-6.31)
        while gyro.angle>2 and gyro.angle<-2:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()

    elif Direction=='East':
        if Currently_Facing=='North':
            TurnL=SpeedPercent(6)
            TurnR=SpeedPercent(-6.31)
        elif Currently_Facing=='East':
            print('This shouldnt happen')
        elif Currently_Facing=='South':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        elif Currently_Facing=='West':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        while gyro.angle>2 and gyro.angle<-2:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()

    elif Direction=='South':
        if Currently_Facing=='North':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        elif Currently_Facing=='East':
            TurnL=SpeedPercent(6)
            TurnR=SpeedPercent(-6.31)
        elif Currently_Facing=='South':
            print('This shouldnt happen')
        elif Currently_Facing=='West':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        while gyro.angle>2 and gyro.angle<-2:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()            

    elif Direction=='West':
        if Currently_Facing=='North':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        elif Currently_Facing=='East':
            TurnL=SpeedPercent(-6)
            TurnR=SpeedPercent(6.31)
        elif Currently_Facing=='South':
            TurnL=SpeedPercent(6)
            TurnR=SpeedPercent(-6.31)
        elif Currently_Facing=='West':
            print('This shouldnt happen')
        while gyro.angle>2 and gyro.angle<-2:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()

    ######################################################
    # reset
    LeftMotor.reset()
    RightMotor.reset()
    return










def turn(Desired_Heading_in_Degrees, Direction):
    #ensure to calibrate first##########################
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    #####################################################
    LeftMotor=LargeMotor(OUTPUT_A)
    RightMotor=LargeMotor(OUTPUT_D)
   
    gyro=GyroSensor(INPUT_2)
    Head=(Desired_Heading_in_Degrees)
    LeftMotor.reset()
    RightMotor.reset()
    gyro.reset()
    ######################################################
    #Clockwise
    if Direction== 'cw':
        TurnL=SpeedPercent(-3)
        TurnR=SpeedPercent(3)
        while gyro.angle<Head-0.5:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()
    #####################################################
    #CounterClockwise
    elif Direction== 'ccw':
        TurnL=SpeedPercent(3)
        TurnR=SpeedPercent(-3)
        while gyro.angle>-Head+1:
            tank.on(TurnL,TurnR)
            time.sleep(0.01)
        tank.stop()
    LeftMotor.reset()
    RightMotor.reset()
    return

    






def cforward(Desired_Distance):
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    #####################################################
    LeftMotor=LargeMotor(OUTPUT_A)
    RightMotor=LargeMotor(OUTPUT_D)
    gyro=GyroSensor(INPUT_2)
    gyro.reset()
    LeftMotor.reset()
    RightMotor.reset()
    tank=MoveTank(OUTPUT_A, OUTPUT_D)
    time.sleep(1)
    Distance_To_Travel=(Desired_Distance)
    DistancePerRotation=14.2/2
    Rotations=Distance_To_Travel/DistancePerRotation
    L=SpeedPercent(-20)
    R=SpeedPercent(-20.31)
    #####################################################
        
    tank.on(L,R)
    time.sleep(0.01)

    while 1==1:
        if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
            break
        while gyro.angle>1.2:
            #correct towards right
            #also i think i assumed wrong, switch left and right
            tank.on(L,SpeedPercent(-21.4))
            time.sleep(0.01)
            if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
                break
        while gyro.angle<-1.2:
            #correct towards left
            tank.on(SpeedPercent(-22.01),SpeedPercent(-20.11))
            time.sleep(0.01)
            if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
                break
        tank.on(L,R)

    tank.stop()
    LeftMotor.reset()
    RightMotor.reset()
    return

def cslowforward(DD):
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    #####################################################
    LeftMotor=LargeMotor(OUTPUT_A)
    RightMotor=LargeMotor(OUTPUT_D)
    gyro=GyroSensor(INPUT_2)
    gyro.reset()
    LeftMotor.reset()
    RightMotor.reset()
    tank=MoveTank(OUTPUT_A, OUTPUT_D)
    time.sleep(1)
    Distance_To_Travel=(DD)
    DistancePerRotation=14.2/2
    Rotations=Distance_To_Travel/DistancePerRotation
    L=SpeedPercent(-20+13)
    R=SpeedPercent(-20+13)
    #####################################################
        
    tank.on(L,R)
    time.sleep(0.01)

    while 1==1:
        if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
            break
        while gyro.angle>1.6:
            #correct towards right
            #also i think i assumed wrong, switch left and right
            tank.on(L,SpeedPercent(-20.5+13))
            time.sleep(0.01)
            if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
                break
        while gyro.angle<-1.6:
            #correct towards left
            tank.on(SpeedPercent(-22.01+13),SpeedPercent(-20.11+13))
            time.sleep(0.01)
            if ((-LeftMotor.position/364)+(-RightMotor.position/364))/2>Rotations:
                break
        tank.on(L,R)

    tank.stop()
    LeftMotor.reset()
    RightMotor.reset()
    return




def cbackward(Desired_Distance):
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    #####################################################
    LeftMotor=LargeMotor(OUTPUT_A)
    RightMotor=LargeMotor(OUTPUT_D)
    gyro=GyroSensor(INPUT_2)
    gyro.reset()
    LeftMotor.reset()
    RightMotor.reset()
    tank=MoveTank(OUTPUT_A, OUTPUT_D)

    Distance_To_Travel=(Desired_Distance)
    DistancePerRotation=14/2
    Rotations=Distance_To_Travel/DistancePerRotation
    L=SpeedPercent(20)
    R=SpeedPercent(20.31)

    #####################################################
        
    tank.on(L,R)
    time.sleep(0.01)
    while 1==1:
        if ((LeftMotor.position/364)+(RightMotor.position/364))/2>Rotations:
            break
        while gyro.angle>1.5:
            #correct towards right
            #also i think i assumed wrong, switch left and right
            tank.on(SpeedPercent(21),R)
            time.sleep(0.01)
            if ((LeftMotor.position/364)+(RightMotor.position/364))/2>Rotations:
                break
        while gyro.angle<-1.5:
            #correct towards left
            tank.on(L,SpeedPercent(21))
            time.sleep(0.01)
            if ((LeftMotor.position/364)+(RightMotor.position/364))/2>Rotations:
                break
        tank.on(L,R)

    tank.stop()
    LeftMotor.reset()
    RightMotor.reset()
    return
    


def Lift_Down():
    global LiftSpeed
    global Up
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    Lift=MediumMotor(OUTPUT_C)
    t=0
    if Up==True:
        while t<200:
            Lift.on(SpeedPercent(-LiftSpeed))
            t=t+1
        Lift.off()
        Up=False
    return

def Lift_Up():
    global LiftSpeed
    global Up
    from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank
    tank= MoveTank(OUTPUT_A, OUTPUT_D)
    from ev3dev2.sensor import INPUT_2
    from ev3dev2.sensor.lego import GyroSensor
    import time
    Lift=MediumMotor(OUTPUT_C)
    t=0
    if Up==False:
        Lift.reset()
        while t<200:
            Lift.on(SpeedPercent(LiftSpeed))
            t=t+1
        Lift.off()
        Up=True
    return





'''
Up=False
Lift_Up()
time.sleep(1)
cforward(5)
Lift_Down()
cbackward(7)
time.sleep(5)
'''

'''
Ultra.MODE_US_DIST_IN = 'US-DIST-IN'
while float(Ultra.distance_inches)>6:
    tank.on(L,R)
tank.off()
time.sleep(5)
'''

