from utility import Utility

# POKEMING - GON'NA CATCH 'EM ALL
# -- A simple hack 'n slash game in console
# -- This class is handles all skill related things
class Skill:
    # Parameterized Constructor
    # <player> Player Object - The player that will cast the skill
    def __init__(self, player):
        # Public properties
        self.heal_amount = 10
        self.skill_damage = 50
        self.player = player

    # This allows for the player to regenerate its health gradually
    def heal(self):
        if self.player.has_enough_mana(3):
            self.player.health = self.player.max_health if self.player.health + (round(self.heal_amount * self.player.level) + round(self.player.max_health / 6)) >= self.player.max_health else self.player.health + (round(self.heal_amount * self.player.level) + round(self.player.max_health / 6))

    # This allows for the player to cast thunder spell to the enemy
    # <enemy> Enemy Object - The enemy being target
    def thunder(self, enemy):
        self.cast_skill(enemy, 'thunder')

    # This allows for the player to cast blizzard spell to the enemy
    # <enemy> Enemy Object - The enemy being target
    def blizzard(self, enemy):
        self.cast_skill(enemy, 'blizzard')

    # This allows for the player to cast fire spell to the enemy
    # <enemy> Enemy Object - The enemy being target
    def fire(self, enemy):
        self.cast_skill(enemy, 'fire')

    # This allows for the player to cast holy spell to the enemy
    # <enemy> Enemy Object - The enemy being target
    def holy(self, enemy):
        self.cast_skill(enemy, 'holy')

    # This checks the affinity of the enemy so that it will deal amplified or nullified damage to it
    # <enemy> Enemy Object - The enemy being target
    # <skill> String - The skill being casted
    # return boolean
    def cast_skill(self, enemy, skill):
        enemy_damage = 0
        if self.player.has_enough_mana(20):
            print(f'You cast a {skill} spell.')

            # Deals amplified damage
            if (enemy.element == 'Water' and skill == 'thunder') or (enemy.element == 'Ice' and skill == 'fire') or (enemy.element == 'Undead' and skill == 'holy'):
                enemy_damage = self.skill_damage * 2
                Utility.pause('It is super effective!')

            # Deals nullified damage
            elif (enemy.element == 'Fire' and skill == 'blizzard') or (enemy.element == 'Water' and skill == 'fire'):
                enemy_damage = self.skill_damage / 2
                Utility.pause('It is not very effective!')
            else:
                enemy_damage = self.skill_damage
            
            # Damage the enemy
            enemy.damage(enemy_damage)
            return True
        else:
            return False