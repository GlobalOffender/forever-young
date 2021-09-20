from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(0,9):
    robotArm.moveRight()
robotArm.drop()
for i in range(0,8):
    robotArm.moveLeft()
robotArm.grab()
for i in range(0,7):
    robotArm.moveRight()
robotArm.drop()
for i in range(0,6):
    robotArm.moveLeft()
robotArm.grab()
for i in range(0,5):
    robotArm.moveRight()
robotArm.drop()
for i in range(0,4):
    robotArm.moveLeft()
robotArm.grab()
for i in range(0,3):
    robotArm.moveRight()
robotArm.drop()
for i in range(0,2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()