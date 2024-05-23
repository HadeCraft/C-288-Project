"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard
# create the Robot instance.
robot = Robot()
key = Keyboard()
# get the time step of the current world.
timestep = 64

A_motor = robot.getDevice("A motor")
B_motor = robot.getDevice("B motor")
C_motor = robot.getDevice("C motor")
D_motor = robot.getDevice("D motor")
E_motor = robot.getDevice("E motor")
F_motor = robot.getDevice("F motor")

A_motor_pos = 0
B_motor_pos = 0
C_motor_pos = 0
D_motor_pos = 0
E_motor_pos = 0
F_motor_pos = 0

key.enable(timestep)

def MoveBot(a=0,b=0,c=0,d=0,e=0,f=0):
    A_motor.setPosition(a)
    B_motor.setPosition(b)
    C_motor.setPosition(c)
    D_motor.setPosition(d)
    E_motor.setPosition(e)
    F_motor.setPosition(f)


while robot.step(timestep) != -1:
  keyPress = key.getKey()
  if(keyPress == 315):
      A_motor_pos -=0.01
  elif(keyPress == 317):
      B_motor_pos +=0.01
  elif(keyPress == 314):
      C_motor_pos +=0.01
  elif(keyPress == 316):
      D_motor_pos -=0.01
      
  elif(keyPress == 87):
      E_motor_pos -=0.01
  elif(keyPress == 83):
      F_motor_pos +=0.01
  MoveBot(A_motor_pos, B_motor_pos, C_motor_pos, D_motor_pos, E_motor_pos, F_motor_pos)