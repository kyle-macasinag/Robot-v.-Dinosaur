from weapon import Weapon
from dinosaur import Dinosaur
dinosaur = Dinosaur

class Robot:
    def __init__(self, name):
        self.robot_name = name
        self.robot_health = 100
        self.active_weapon = Weapon("Chain Sword", 35)
    
    def attack(self, dinosaur):
        dinosaur.dino_health -= self.active_weapon.weapon_attack_power
        print(f"{self.robot_name} attacks {dinosaur.dino_name} for {self.active_weapon.weapon_attack_power} damage.  Their health is now {dinosaur.dino_health}." )