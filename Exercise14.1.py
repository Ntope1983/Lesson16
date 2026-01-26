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
        if self.health <= 0:
            return True
        else:
            return False

    def end_round(self):
        if self.health < 100:
            self.health += 1
        if self.delay > 0:
            self.delay -= 1

    def print(self):
        print(f"Character Name:{self.name},Health:{self.health},Attack_Speed:{self.attack_speed},Delay:{self.delay}")


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
        round = 0
        while True:
            round += 1
            print(f"Round:{round}")
            avail_a = [c for c in self.team_a if c.delay == 0 and not c.is_dead()]
            avail_b = [c for c in self.team_b if c.delay == 0 and not c.is_dead()]

            alive_a = [c for c in self.team_a if not c.is_dead()]
            alive_b = [c for c in self.team_b if not c.is_dead()]

            if not alive_a and not alive_b:
                print("DRAW")
                break
            if not alive_a:
                print("TEAM B wins")
                break
            if not alive_b:
                print("TEAM A wins")
                break

            for attacker in avail_a:
                if not alive_b:
                    break
                target = random.choice(alive_b)
                dmg = attacker.attack()
                target.health = max(0, target.health - dmg)

            for attacker in avail_b:
                if not alive_a:
                    break
                target = random.choice(alive_a)
                dmg = attacker.attack()
                target.health = max(0, target.health - dmg)

            for c in self.team_a + self.team_b:
                if not c.is_dead():
                    c.end_round()


orc1 = Character("Ntope")
orc2 = Character("Vlassonio")
orc3 = Character("Xoverdose")
orc4 = Character("Skoulikion")
orc5 = Character("Valmadin")
night_elf1 = Character("Crowly")
night_elf2 = Character("Hydra")
night_elf3 = Character("Sodapopin")
team_a = [orc1, orc2, orc3, orc4, orc5]
team_b = [night_elf1, night_elf2, night_elf3]
arena1 = Arena(team_a, team_b)
arena1.print_state()
arena1.play()
arena1.print_state()
