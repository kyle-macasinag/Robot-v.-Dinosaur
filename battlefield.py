from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        robot = Robot
        dinosaur = Dinosaur

    def run_game(self):
        self.display_welcome
        self.battle_phase
        self.display_winner
    def display_welcome(self):
        print("Time for another round of Robot vs Dinosaur!")
    def battle_phase(self):
        pass
    def display_winner(self):
        pass
