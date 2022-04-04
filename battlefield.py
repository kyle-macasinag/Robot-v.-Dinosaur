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
        robot = Robot
        dinosaur = Dinosaur
        while robot.robot_health > 0 and dinosaur.dino_health > 0:
            robot.attack()
            dinosaur.dino_attack()
        if robot.robot_health < 1:
            print(f"{robot.robot_name} broke down!")
            self.winner = dinosaur.dino_name
        if dinosaur.dino_health < 1:
            print(f"{dinosaur.dino_name} has collapsed!")
            self.winner = robot.robot_name
        pass

    def display_winner(self):
         robot = Robot
         dinosaur = Dinosaur
         if self.winner == dinosaur.dino_name:
             print(f"{dinosaur.dino_name} is the winner!")
         if self.winner == robot.robot_name:
             print(f"{robot.robot_name} is the winner!")
         pass
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()