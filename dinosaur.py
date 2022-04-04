from robot import Robot

class Dinosaur:
    def __init__(self, name, attack_power):
        self.dino_name = name
        self.dino_attack_power = attack_power
        self.dino_health = 100


    def dino_attack(self, robot):
        robot.robot_health -= self.dino_attack_power
        print (f"{self.dino_name} bites {robot.robot_name} for {self.dino_attack_power} damage. They now have {robot.robot_health} hp.")