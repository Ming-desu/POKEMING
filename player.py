import random
from inventory import Inventory
from skill import Skill
from utility import Utility

# POKEMING - GON'NA CATCH 'EM ALL
# -- A simple hack 'n slash game in console
# -- This class is handles all player related things
class Player:
    # Default Constructor
    def __init__(self):
        # Public properties
        self.name = input('Enter your character name: ')
        self.attack_damage = random.randint(8, 12)
        self.heal_amount = random.randint(8, 12)
        self.max_health = 100
        self.health = self.max_health
        self.max_mana = 50
        self.mana = self.max_mana
        self.level = 1
        self.experience_point = 0
        self.max_experience_point = 100
        self.inventory = Inventory()
        self.skill = Skill(self)

    # This prints the player's current stats
    def stats(self):
        print(f'Player name: {self.name} | LVL: {self.level} | Coins: {self.inventory.coins}')
        print(f'HP: {self.health}/{self.max_health} | MP: {self.mana}/{self.max_mana}')
        print(f'Exp: {self.experience_point}/{self.max_experience_point}')

    # This allows the player to attack an enemy
    # <enemy> Enemy Object - The enemy to be attacked
    def attack(self, enemy):
        # 5% chance for the player to miss the attack
        if (miss_change := random.randint(0, 20)) == 1:
            Utility.pause('Your attack missed!')
            return
        
        # 10% chance for the player to land a critical hit
        if (x := random.randint(0, 10)) == 1:
            enemy.damage(self.attack_damage + random.randint(0, 10))
            Utility.pause('You landed a critical hit!')
            return

        # Damage the enemy
        enemy.damage(self.attack_damage)

    # This function check if there is enough mana to cast the spell
    # <mana_cost> Integer - The mana cost to cast the spell
    # return boolean
    def has_enough_mana(self, mana_cost):
        if self.mana > mana_cost:
            self.mana -= mana_cost
            return True
        else: 
            Utility.pause('Not enough mana.')
            return False

    # The function that allows the player to level up and gain some improvements
    def level_up(self):
        # Check for the exp if it exceeds the needed exp points
        if self.experience_point >= self.max_experience_point:
            # Improve the health, mana, exp, attack damage of the player
            self.level += 1
            self.max_health += 10 + (random.randint(0, 10) * self.level)
            self.health = self.max_health
            self.max_mana += 10 + (random.randint(0, 10) * self.level)
            self.mana = self.max_mana
            self.experience_point -= self.max_experience_point
            self.max_experience_point = round(self.max_experience_point * 1.5)
            self.attack_damage += random.randint(0, 5)

    # This allows the player to take damage from an attack
    # <value> Integer - The damage that the player will take
    def damage(self, value):
        self.health -= round(value)

    # This checks if the player is dead or not
    # return boolean
    def is_dead(self):
        return True if self.health <= 0 else False

    # This allows the player to gain experience points and some coins after killing an enemy
    # <enemy> Enemy Object - The enemy that was killed
    def killed_an_enemy(self, enemy):
        self.experience_point += (random.randint(19, 40) * self.level)
        self.inventory.coins += random.randint(0, 5)
        self.level_up()

    # This allows the player to reflenish its mana in exchange with in-game coins
    def pots(self):
        if self.inventory.coins - 3 <= 0:
            Utility.pause('Not enough money')
            return
        self.inventory.coins -= 3
        self.mana = self.mana + round(self.max_mana / 3) if self.mana + round(self.max_mana / 3) <= self.max_mana else self.max_mana