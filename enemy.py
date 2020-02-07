import random
from utility import Utility

# POKEMING - GON'NA CATCH 'EM ALL
# -- A simple hack 'n slash game in console
# -- This class is handles all enemy related things
class Enemy:
    # Parameterized Constructor
    # <player> Player Object - The player itself
    def __init__(self, player):
        # Public properties
        self.player = player
        self.health = random.randint(100 * player.level, 120 * player.level)
        self.max_health = self.health
        self.attack_damage = random.randint(8, 12) + round(1.5 * self.player.level)
        self.name = self.get_random_name()
        self.element = self.get_random_element()

    # A function that will print the stats of the enemy
    def stats(self):
        print(f'Enemy: {self.name} | Element: {self.element}')
        print(f'HP: {self.health}/{self.max_health}')

    # A function that allows the enemy to attack the player
    # <player> Player Object - The player itself
    def attack(self, player):
        if self.is_dead == True:
            return

        # 5% chance for the enemy getting a critical hit
        if (x := random.randint(0, 20)) == 1:
            # Deal increased damage to the player
            player.damage(self.attack_damage + random.randint(0, 10))
            Utility.pause('Enemy landed critical hit!')
            return

        # Damage the player with the current damage of the enemy    
        player.damage(self.attack_damage)

    # A function that allows for the enemy to take damage and lose its health
    # <value> Integer - The value being damaged to the enemy's health
    def damage(self, value):
        self.health -= round(value)

    # A function to check whether the enemy is dead of not
    # return boolean 
    def is_dead(self):
        return True if self.health <= 0 else False

    # A function that allows for the enemy to have a random name
    # return String
    def get_random_name(self):
        names = ['Harley', 'Nira Sins', 'Gian Bleu', 'Turbo E', 'Gino Blie', 'Jung Cock', 'Dickson Tubero']
        return names[random.randint(-1, len(names) - 1)]

    # A function that allows for the enemy to have an element
    # return String
    def get_random_element(self):
        elements = ['Thunder', 'Ice', 'Fire', 'Undead', 'Water']
        return elements[random.randint(-1, len(elements) - 1)]