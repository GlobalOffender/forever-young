from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
for i in range(0,3):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
robotArm.moveRight()
robotArm.moveRight()
for i in range(0,3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
robotArm.moveLeft()
# Jouw python instructies zet je vanaf hier:

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()