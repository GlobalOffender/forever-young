from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(0,5):
    robotArm.moveRight()
robotArm.drop()
for i in range(0,4):
    robotArm.moveLeft()
for i in range(0,2):
    robotArm.grab()
    for i in range(0,5):
      robotArm.moveRight()
    robotArm.drop()
    for i in range(0,5):
      robotArm.moveLeft()
robotArm.moveRight()
for i in range(0,3):
    robotArm.grab()
    for i in range(0,5):
      robotArm.moveRight()
    robotArm.drop()
    for i in range(0,5):
      robotArm.moveLeft()
robotArm.moveRight()
for i in range(0,4):
    robotArm.grab()
    for i in range(0,5):
      robotArm.moveRight()
    robotArm.drop()
    for i in range(0,5):
      robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()