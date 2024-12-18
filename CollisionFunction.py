#!/usr/bin/env python3
TimeofXCollision=0
TimeofYCollision=0
TimeofDiagCollision=0
HorizontalCollision=False
VerticalCollision=False
HorizontalCollision=False

def CollisionX(t):
    global TimeofXCollision
    global HorizontalCollision
    HorizontalCollision=True
    TimeofXCollision=t
    return
def CollisionY(t):
    global TimeofYCollision
    global VerticalCollision
    VerticalCollision=True
    TimeofYCollision=t
    return
def CollisionDiag(t):
    global TimeofDiagCollision
    #Add Diag stuff
    TimeofDiagCollision=t
    return


def Check_for_Collisions(Target, Current):
    '''Note that these are in arrays [x,y]'''
    ACT=''
    global TimeofXCollision
    global TimeofYCollision
    global TimeofDiagCollision
    global HorizontalCollision
    global VerticalCollision
  #  global #



    #Horizontal
    Horizontal_Step=(Target[0]-Current[0])/1000
    HorizontalCollision=False
    
    for time in range(0,1000):

        CalculatedHorizontal=(time*Horizontal_Step)+Current[0]
        
        if CalculatedHorizontal<0:
            CollisionX(time)
            break
        elif CalculatedHorizontal>12 and CalculatedHorizontal<48:
            if Current[1]<0:
                    CollisionX(time)
                    break
            elif Current[1]>12 and Current[1]<24:
                    CollisionX(time)
                    break
            elif Current[1]>36 and Current[1]<48:
                    CollisionX(time)
                    break
            elif Current[1]>60 and Current[1]<72:
                    CollisionX(time)
                    break
            elif Current[1]>84 and Current[1]<96:
                    CollisionX(time)
                    break
            elif Current[1]>108:
                    CollisionX(time)
                    break
            
        elif CalculatedHorizontal>60 and CalculatedHorizontal<96:
            if Current[1]<0:
                    CollisionX(time)
                    break
            elif Current[1]>12 and Current[1]<24:
                    CollisionX(time)
                    break
            elif Current[1]>36 and Current[1]<48:
                    CollisionX(time)
                    break
            elif Current[1]>60 and Current[1]<72:
                    CollisionX(time)
                    break
            elif Current[1]>84 and Current[1]<96:
                    CollisionX(time)
                    break
            elif Current[1]>108:
                    CollisionX(time)
                    break
            
        elif CalculatedHorizontal>108:
            CollisionX(time)
            break
        HorizontalCollision=False


    #Vertical
    Vertical_Step=(Target[1]-Current[1])/1000
    VerticalCollision=False
    
    for time in range(0,10000):
        time=time*0.1

        CalculatedVertical=(time*Vertical_Step)+Current[1]
        
        if CalculatedVertical<-12:
            CollisionY(time)
            break
        elif CalculatedVertical<0:
              if Current[0]>12 and Current[0]<96:
                    CollisionY(time)
                    break
        elif CalculatedVertical>12 and CalculatedVertical<24:
                if (Current[0]>12 and Current[0]<48) or (Current[0]>60 and Current[0]<96):
                    CollisionY(time)
                    break
        elif CalculatedVertical>36 and CalculatedVertical<48:
                if (Current[0]>12 and Current[0]<48) or (Current[0]>60 and Current[0]<96):
                    CollisionY(time)
                    break
        elif CalculatedVertical>60 and CalculatedVertical<72:
                if (Current[0]>12 and Current[0]<48) or (Current[0]>60 and Current[0]<96):
                    CollisionY(time)
                    break
        elif CalculatedVertical>84 and CalculatedVertical<96:
                if (Current[0]>12 and Current[0]<48) or (Current[0]>60 and Current[0]<96):
                    CollisionY(time)
                    break
        elif CalculatedVertical>108:
              if Current[0]>12 and Current[0]<96:
                    CollisionY(time)
                    break
        elif CalculatedVertical>120:
            CollisionY(time)
            break
        VerticalCollision=False


 #ACT is Move on the ______________ axis
    if VerticalCollision==True and HorizontalCollision==True:
          if TimeofXCollision<TimeofYCollision:
                ACT='Y'
          else:
                ACT='X'
    elif VerticalCollision==True:
          ACT='X'
    elif HorizontalCollision==True:
          ACT='Y'
    elif (Target[0]-Current[0])==0:
          ACT='Y'
    elif (Target[1]-Current[1])==0:
          ACT='X'
    else:
          #PANIC
          print('COLLISION FUNCTION CRITICAL ERROR')

    return ACT


        






    








#CurrentYep=[102,6]
#Local=[102,-6]
#print(Check_for_Collisions(Local, CurrentYep))



#print(TimeofXCollision)
#print(HorizontalCollision)
#print(TimeofYCollision)
#print(VerticalCollision)





