"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, Keyboard
# create the Robot instance.
robot = Robot()
key = Keyboard()
# get the time step of the current world.
timestep = 64

shoulder_lift = robot.getDevice("shoulder_lift_joint")
shoulder_pan = robot.getDevice("shoulder_pan_joint")
elbow = robot.getDevice("elbow_joint")
wrist1 = robot.getDevice("wrist_1_joint")
wrist2 = robot.getDevice("wrist_2_joint")
wrist3 = robot.getDevice("wrist_3_joint")

shoulder_lift_pos = 0
shoulder_pan_pos = 0
elbow_pos = 0
wrist1_pos = 0
wrist2_pos = 0
wrist3_pos = 0

key.enable(timestep)

def MoveBot(a=0,b=0,c=0,d=0,e=0,f=0):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist1.setPosition(d)
    wrist2.setPosition(e)
    wrist3.setPosition(f)


while robot.step(timestep) != -1:
  keyPress = key.getKey()
  if(keyPress == 315):
      shoulder_lift_pos -=0.01
  elif(keyPress == 317):
      shoulder_lift_pos +=0.01
  elif(keyPress == 314):
      shoulder_pan_pos +=0.01
  elif(keyPress == 316):
      shoulder_pan_pos -=0.01
      
  elif(keyPress == 87):
      elbow_pos -=0.01
  elif(keyPress == 83):
      elbow_pos +=0.01
  elif(keyPress == 65):
      wrist1_pos +=0.01
  elif(keyPress == 68):
      wrist1_pos -=0.01
      
  elif(keyPress == 49):
      wrist2_pos +=0.01
  elif(keyPress == 50):
      wrist2_pos -=0.01
  elif(keyPress == 51):
      wrist3_pos +=0.01
  elif(keyPress == 52):
      wrist3_pos -=0.01
  MoveBot(shoulder_lift_pos, shoulder_pan_pos, elbow_pos, wrist1_pos, wrist2_pos, wrist3_pos)