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

# Box Config
Default_Shelve=[[3,0],[9,0],[15,0],[21,0],[27,0],[33,0],[3,12],[9,12],[15,12],[21,12],[27,12],[33,12]]



Shelve_Positions=[]

#####################################
# Travelling Config
ActionList=[]
StraightList=[]
TurnList=[]
Need_To_Go=''
#####################################
# inputs
# A1 A2 B1 B2 C1 C2 D1 D2
Shelve_Unit='A1'
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
Target_Box_Number=7
# A B C D
Drop_Off_Location='B'
# A B C D
Home='B'
# 1 2 3 4
Expected_Barcode=1


#####################################
#Set Home
if Home=='A':
    Facing='North'
    Home_Coords=[6,-6]
    Current_Coords=[6,-6]
    LocalReturn=[6,6]
elif Home=='B':
    Facing='South'
    Home_Coords=[102,-6]
    Current_Coords=[102,-6]
    LocalReturn=[6,6]
elif Home=='C':
    Facing='South'
    Home_Coords=[6,114]
    Current_Coords=[6,114]
    LocalReturn=[6,102]
elif Home=='D':
    Facing='South'
    Home_Coords=[102,114]
    Current_Coords=[102,114]
    LocalReturn=[102,102]
Need_To_Go=Facing
#####################################
# Barcode Configuration:

BarcodeRead=[-1,-1,-1,-1]
Barcode1=[1,0,0,0]
Barcode2=[1,0,1,0]
Barcode3=[1,1,0,0]
Barcode4=[1,0,0,1]


#####################################
#Set Drop Off Location
if Drop_Off_Location=='A':
    DropOff_Coords=[6,-6]
elif Drop_Off_Location=='B':
    DropOff_Coords=[102,-6] 
elif Drop_Off_Location=='C':
    DropOff_Coords=[6,114]
elif Drop_Off_Location=='D':
    DropOff_Coords=[102,114]
################################################
# Shelves Determinier
if Shelve_Unit =='A1':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+12
        y_val=Default_Shelve[i][1]+12
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit=='B1':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+60
        y_val=Default_Shelve[i][1]+12
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit =='A2':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+12
        y_val=Default_Shelve[i][1]+36
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit=='B2':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+60
        y_val=Default_Shelve[i][1]+36
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit =='C1':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+12
        y_val=Default_Shelve[i][1]+60
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit=='D1':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+60
        y_val=Default_Shelve[i][1]+60
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit =='C2':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+12
        y_val=Default_Shelve[i][1]+84
        Shelve_Positions.append([x_val,y_val])
elif Shelve_Unit=='D2':
    for i in range(len(Default_Shelve)):
        x_val=Default_Shelve[i][0]+60
        y_val=Default_Shelve[i][1]+84
        Shelve_Positions.append([x_val,y_val])
else:
    print('Shelving Error')
    time.sleep(10)
    quit()

#print(Shelve_Positions)

##########################################################
# Box Coordinate Determiner
if Target_Box_Number>12 or Target_Box_Number<1:
    print('Box Bound Error')
    time.sleep(10)
    quit()

elif Target_Box_Number>6.5:
    BoxSide='Upper'
    if Target_Box_Number==7:
        Target_Box_Coords=Shelve_Positions[7-1]
    elif Target_Box_Number==8:
        Target_Box_Coords=Shelve_Positions[8-1]
    elif Target_Box_Number==9:
        Target_Box_Coords=Shelve_Positions[9-1]
    elif Target_Box_Number==10:
        Target_Box_Coords=Shelve_Positions[10-1]
    elif Target_Box_Number==11:
        Target_Box_Coords=Shelve_Positions[11-1]
    elif Target_Box_Number==12:
        Target_Box_Coords=Shelve_Positions[12-1]
    else:
        print('Box Integer Error')
        time.sleep(10)
        quit()
elif Target_Box_Number<6.5:
    BoxSide='Lower'
    if Target_Box_Number==1:
        Target_Box_Coords=Shelve_Positions[1-1]
    elif Target_Box_Number==2:
        Target_Box_Coords=Shelve_Positions[2-1]
    elif Target_Box_Number==3:
        Target_Box_Coords=Shelve_Positions[3-1]
    elif Target_Box_Number==4:
        Target_Box_Coords=Shelve_Positions[4-1]
    elif Target_Box_Number==5:
        Target_Box_Coords=Shelve_Positions[5-1]
    elif Target_Box_Number==6:
        Target_Box_Coords=Shelve_Positions[6-1]
    else:
        print('Box Integer Error')
        time.sleep(10)
        quit()



#print(Target_Box_Coords)

##########################################################
# Target Location Determiner
if Target_Box_Coords[1]>90:
    Local_Target=[(Target_Box_Coords[0]),(102)]
elif Target_Box_Coords[1]>66:
    Local_Target=[(Target_Box_Coords[0]),(78)]
elif Target_Box_Coords[1]>42:
    Local_Target=[(Target_Box_Coords[0]),(54)]  
elif Target_Box_Coords[1]>18:
    Local_Target=[(Target_Box_Coords[0]),(30)]
else:
    Local_Target=[(Target_Box_Coords[0]),(6)]

#print(Local_Target)
######################################################################
#function to perform actions from lists
def RunActions():
    global ActionList
    global StraightList
    global TurnList
    global Facing
    StraightIndex=0
    TurnIndex=0


    for ACTIONINDEX in range(len(ActionList)):
        if ActionList[ACTIONINDEX]=='S':
            #go straight
            if Facing=='West':
                ev3functions.cforward(float(StraightList[StraightIndex]+2))
            else:
                ev3functions.cforward(StraightList[StraightIndex])
            StraightIndex=StraightIndex+1
        elif ActionList[ACTIONINDEX]=='T':
            #turn
            ev3functions.turn(TurnList[TurnIndex][0],TurnList[TurnIndex][1])

            TurnIndex=TurnIndex+1
        
        elif ActionList[ACTIONINDEX]=='STOP':
            time.sleep(5)

        elif ActionList[ACTIONINDEX]=='P':
            #pickup

            #ensure lift is up for first time
            ev3functions.Lift_Up()

            if BoxSide=='Upper':
                #face south
                if Facing=='East':
                    print('Upper/East')
                    #turn towards box
                    ev3functions.turn(90, 'cw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'ccw')
                elif Facing=='West':
                    print('Upper/West')
                    #turn towards box
                    ev3functions.turn(90, 'ccw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'cw')
                
            elif BoxSide=='Lower':
                #face north
                if Facing=='East':
                    
                    print('Lower/East')
                    #turn towards box
                    ev3functions.turn(90, 'ccw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'cw')


                elif Facing=='West':
                    print('Lower/West')
                    #turn towards box
                    ev3functions.turn(90, 'cw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'ccw')
        



        elif ActionList[ACTIONINDEX]=='D':
            #drop off


            #go forward a little
            ev3functions.cforward(3)
            #drop off box code here
            ev3functions.Lift_Down()
            #return to spot
            ev3functions.cbackward(3)
            

    return




######################################################################
def RunActionsADJ():
    global ActionList
    global StraightList
    global TurnList
    global Facing
    StraightIndex=0
    TurnIndex=0


    for ACTIONINDEX in range(len(ActionList)):
        if ActionList[ACTIONINDEX]=='S':
            #go straight
            if Facing=='East':
                ev3functions.cforward(float(StraightList[StraightIndex]+3))
            elif Facing=='South':
                ev3functions.cforward(float(StraightList[StraightIndex]+1))
            else:
                ev3functions.cforward(StraightList[StraightIndex])
            StraightIndex=StraightIndex+1
        elif ActionList[ACTIONINDEX]=='T':
            #turn
            ev3functions.turn(TurnList[TurnIndex][0],TurnList[TurnIndex][1])

            TurnIndex=TurnIndex+1
        
        elif ActionList[ACTIONINDEX]=='STOP':
            time.sleep(5)

        elif ActionList[ACTIONINDEX]=='P':
            #pickup

            #ensure lift is up for first time
            ev3functions.Lift_Up()

            if BoxSide=='Upper':
                #face south
                if Facing=='East':
                    print('Upper/East')
                    #turn towards box
                    ev3functions.turn(90, 'cw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'ccw')
                elif Facing=='West':
                    print('Upper/West')
                    #turn towards box
                    ev3functions.turn(90, 'ccw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'cw')
                
            elif BoxSide=='Lower':
                #face north
                if Facing=='East':
                    
                    print('Lower/East')
                    #turn towards box
                    ev3functions.turn(90, 'ccw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'cw')


                elif Facing=='West':
                    print('Lower/West')
                    #turn towards box
                    ev3functions.turn(90, 'cw')
                    #drive up to box
                    ev3functions.cforward(5)
                    #turn so that barcode is in line
                    ev3functions.turn(90, 'ccw')
                    #drive backwards/Store barcode
                    #drive forwards again
                    #turn back
                    ev3functions.turn(90, 'cw')
                    #back up to make room for claw
                    ev3functions.cbackward(3)
                    #Lower the lift
                    ev3functions.Lift_Down()
                    #Drive forwards to pick up box
                    ev3functions.cforward(3)
                    #pick up box
                    ev3functions.Lift_Up()
                    #back up
                    ev3functions.cbackward(5)
                    #turn to face original direction
                    ev3functions.turn(90, 'ccw')
        



        elif ActionList[ACTIONINDEX]=='D':
            #drop off


            #go forward a little
            ev3functions.cforward(3)
            #drop off box code here
            ev3functions.Lift_Down()
            #return to spot
            ev3functions.cbackward(3)
            

    return




######################################################################
#Function for list resetting
def AllListReset():
    global ActionList
    global StraightList
    global TurnList
    ActionList=[]
    StraightList=[]
    TurnList=[]

    return

######################################################################
# Function for path determination to simplify code

def Pathfind(Place_From, Place_To_Go):
    global Facing
    global ActionList
    global TurnList
    global StraightList
    global Current_Coords
    global Local_Target
    global Need_To_Go
    #print(Facing)
    Current_Coords=Place_From  
    Local_Target=Place_To_Go

    
    while Current_Coords[0]!=Local_Target[0] or Current_Coords[1]!=Local_Target[1]:


        Vertical=Local_Target[1]-Current_Coords[1]
        Horizontal=Local_Target[0]-Current_Coords[0]

        Direction_of_Travel=CollisionFunction.Check_for_Collisions(Local_Target, Current_Coords)

        #print(Direction_of_Travel)

        if Direction_of_Travel=='X':
            if Horizontal>0:
                Need_To_Go='East'
            elif Horizontal<0:
                Need_To_Go='West'
            #print('E/W')
        elif Direction_of_Travel=='Y':
            if Vertical>0:
                Need_To_Go='North'
            elif Vertical<0:
                Need_To_Go='South'
            #print('N/S')
        else:
            print('Something Strange has happened...')
        

        #print(Vertical, Horizontal)



        if Facing=='North':
            if Need_To_Go=='North':
                ActionList.append('S')
                StraightList.append(abs(Vertical))
                Current_Coords[1]=Current_Coords[1]+Vertical
                Facing='North'
            elif Need_To_Go=='East':
                ActionList.append('T')
                TurnList.append([90,'cw'])
                Facing='East'
            elif Need_To_Go=='South':
                ActionList.append('T')
                TurnList.append([180,'ccw'])
                Facing='South'
            elif Need_To_Go=='West':
                ActionList.append('T')
                TurnList.append([90,'ccw'])
                Facing='West'

        elif Facing=='East':
            if Need_To_Go=='North':
                ActionList.append('T')
                TurnList.append([90,'ccw'])
                Facing='North'
            elif Need_To_Go=='East':
                ActionList.append('S')
                StraightList.append(abs(Horizontal))
                Current_Coords[0]=Current_Coords[0]+Horizontal
                Facing='East'
            elif Need_To_Go=='South':
                ActionList.append('T')
                TurnList.append([90,'cw'])
                Facing='South'
            elif Need_To_Go=='West':
                ActionList.append('T')
                TurnList.append([180,'ccw'])
                Facing='West'
            
        elif Facing=='South':
            if Need_To_Go=='North':
                ActionList.append('T')
                TurnList.append([180,'ccw'])
                Facing='North'
            elif Need_To_Go=='East':
                ActionList.append('T')
                TurnList.append([90,'cw'])
                Facing='East'
            elif Need_To_Go=='South':
                ActionList.append('S')
                StraightList.append(abs(Vertical))
                Current_Coords[1]=Current_Coords[1]+Vertical
                Facing='South'
            elif Need_To_Go=='West':
                ActionList.append('T')
                TurnList.append([90,'ccw'])
                Facing='West'
            
        elif Facing=='West':
            if Need_To_Go=='North':
                ActionList.append('T')
                TurnList.append([90,'cw'])
                Facing='North'
            elif Need_To_Go=='East':
                ActionList.append('T')
                TurnList.append([180,'ccw'])
                Facing='East'
            elif Need_To_Go=='South':
                ActionList.append('T')
                TurnList.append([90,'ccw'])
                Facing='South'
            elif Need_To_Go=='West':
                ActionList.append('S')
                StraightList.append(abs(Horizontal))
                Current_Coords[0]=Current_Coords[0]+Horizontal
                Facing='West'

        
            
        else:
            print('Facing Error')
            time.sleep(10)
            quit()
        
        
        
        
        
        #print(Current_Coords)
        #print(Local_Target)
        #time.sleep(1)
    return




















######################################################################

gyro.calibrate()
######################################################################
#Ensure Lift is up before travelling
ev3functions.Lift_Down()

######################################################################
# Determine Path of Travel To Box (Here the local target has been set to on path off of box)
#Pathfind(Current_Coords, Local_Target)
##################################################################  
#STOP HERE (Pause for 5s)
#ActionList.append('STOP')
##################################################################
#Go to box and and Pause
#RunActions()
#AllListReset()
##################################################################
# Determine Path of Travel To Box Drop Off
#Local_Target=DropOff_Coords
#Pathfind(Current_Coords, Local_Target)
##################################################################  
##################################################################
#Go to Box Drop off (Adjusted for being off)
#RunActionsADJ()
#AllListReset()  
##################################################################
#STOP HERE
#ActionList.append('STOP')
##################################################################  
#Return to home from B
Pathfind(Current_Coords, LocalReturn)
Home_Coords=[6,-6]
Pathfind(Current_Coords, Home_Coords)
RunActions()
AllListReset()
##################################################################
print(ActionList)
print(StraightList)
print(TurnList)