from controller import Robot
from controller import Motor
from controller import Altimeter
#from controller import LED
import math

class MyController(Robot):
    def __init__(self):
            super(MyController,self).__init__()
            self.timeStep=32
            
            self.distanceSensor = self.getDevice('ds0')
            self.distanceSensor.enable(self.timeStep)
            
            self.accelerometer=self.getDevice("accelerometer")
            self.accelerometer.enable(self.timeStep)
            
            #self.front_led = self.getDevice("front_led")
            #self.back_led = self.getDevice("back_led")
            #self.left_led = self.getDevice("left_led")
            #self.right_led = self.getDevice("right_led")          
            
            self.left_motor = self.getDevice("left wheel motor")
            self.right_motor = self.getDevice("right wheel motor")
      
            self.left_motor.setPosition(math.inf)
            self.right_motor.setPosition(math.inf)
            
            self.left_motor.setVelocity(0.5)
            self.right_motor.setVelocity(-0.5)
            self.direction_switch=False
            self.accValues=[]
            
            

    
    def run(self):
        while self.step(self.timeStep) != -1:
            for i in range(3):
                self.accValues.append(self.accelerometer.getValues())
            self.accValues=[]
                    
controller = MyController()
controller.run()