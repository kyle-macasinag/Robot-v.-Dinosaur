class Weapon:
    def __init__(self, name, attack_power):
        self.weapon_name = name
        self.weapon_attack_power = attack_power

    # def choose_weapon(self):
    #     print(" Flamer   Bolt Gun   Chain Sword")
    #     self.choice = input("Which weapon would you like to use? ")
    #     if self.choice == "Flamer":
    #         self.weapon_name = "Flamer"
    #         self.attack_power = 25
    #     elif self.choice == "Chain Sword":
    #         self.weapon_name = "Chain Sword"
    #         self.attack = 35
    #     elif self.choice == "Bolt Gun":
    #         self.weapon_name = "Bolt Gun"
    #         self.attack = 40