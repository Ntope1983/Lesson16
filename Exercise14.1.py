# World of Warcraft Part1
import random


class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_speed = 2
        self.delay = 0

    def attack(self):
        self.delay = 10 - self.attack_speed
        return random.randint(3, 10)

    def is_dead(self):
        if self.health == 0:
            return True
        else:
            return False

    def end_round(self):
        if self.health < 100:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def print(self):
        print(f"Character Name: {self.name}.Health{self.health}.Attack_Speed:{self.attack_speed}.Delay:{self.delay}")


class Arena:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b

    def print_state(self):
        print("----TEAM A----")
        for character in self.team_a:
            character.print()
        print("----TEAM B----")
        for character in self.team_b:
            character.print()

    def play(self):
        # delay 0
        characters_avail_team_a = [char for char in self.team_a if char.delay == 0]
        characters_avail_team_b = [char for char in self.team_b if char.delay == 0]

        for i in range(len(characters_avail_team_a)):
            choice = random.choice(characters_avail_team_a)
            choice.health -= characters_avail_team_a[i].attack()
