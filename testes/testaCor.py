from ev3dev.ev3 import *
import time


m1 = LargeMotor('outD')
m2 = LargeMotor('outA')
cor = ColorSensor('in4')
cor2 = ColorSensor('in1')

cor.mode = 'COL-COLOR'
cor2.mode = 'COL-COLOR'

def testColor(corAtual):
    i = 0
    a = 0
    while(i < 100):          
        if(corAtual == cor.value()):           
            a = a + 1
        if(i%2 ==0):
            m1.run_timed(time_sp=100, speed_sp=100)
            m2.run_timed(time_sp=100, speed_sp=100)
        else:
            m1.run_timed(time_sp=100, speed_sp=-100)
            m2.run_timed(time_sp=100, speed_sp=-100)
        i = i +1
    
    if(a >= 60):
        return True
    m1.run_timed(time_sp=500, speed_sp=100)
    m2.run_timed(time_sp=500, speed_sp=100)
    return False

print(testColor(cor))