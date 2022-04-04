from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot("Cl4ptr4p")
        self.dinosaur = Dinosaur("Yoshi", 40)
        self.winner = ""

    def display_welcome(self):
        print("Time for another round of Robot vs Dinosaur!")
    def battle_phase(self):
        while self.robot.robot_health > 0 and self.dinosaur.dino_health > 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.dino_health < 1:
                print(f"{self.dinosaur.dino_name} has collapsed!")
            self.winner = self.robot.robot_name
            self.dinosaur.dino_attack(self.robot)
            if self.robot.robot_health < 1:
                print(f"{self.robot.robot_name} broke down!")
                self.winner = self.dinosaur.dino_name
       
        

    def display_winner(self):

         if self.winner == self.dinosaur.dino_name:
             print(f"{self.dinosaur.dino_name} is the winner!")
         if self.winner == self.robot.robot_name:
             print(f"{self.robot.robot_name} is the winner!")
         pass
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()