import os
import random
from player import Player
from enemy import Enemy

# POKEMING - GON'NA CATCH 'EM ALL
# -- A simple hack 'n slash game in console
# -- This class is the main wrapper of the game
class Main:
    # Default Constructor
    def __init__(self):
        # Public properties
        self.player = Player()
        self.enemy = Enemy(self.player)  
        self.scoreboard = 1    
        self.is_running = True
        self.screen_elements = [None] * 200
        self.game_logic()

    # A function that will set the highscore and save it to a .txt file
    def set_highscore(self):
        # Opens the file based on the path given
        file = open('scoreboard.txt', 'at')
        # Write a string to the file itself
        file.write('Name:' + str(self.player.name) + '\t LVL:' + str(self.player.level) + '\t Score:' + str(self.scoreboard) + '\r')
        # Close the file to avoid runtime error
        file.close()

        # Order the highscores
        self.order_highscores()

    # A function that will get the highscore from the .txt file and print it
    def get_highscores(self):
        # Clears the console
        os.system('cls')
        # Opens the file based on the path given
        file = open('scoreboard.txt', 'rt')

        # Get the array form of scores by splitting it with '\n'
        scores = file.read().split('\n')
        print('Highscores:')

        # Iterate through each element in the scores array
        for i in range(len(scores) - 2, -1, -1):
            # Split again the current value of score with '\t'
            # It will return an array with 3 elements {name, lvl, score}
            score = scores[i].split('\t')

            # Get the name itself
            name = score[0].split(':')[1]
            # Get the lvl 
            lvl = score[1].split(':')[1]
            # Get the score
            score = score[2].split(':')[1]
            # Print the score details
            print(f'{abs((i + 1) - len(scores))}. {name} | LVL: {lvl} | Score: {score}')
        
        # Close the file to avoid runtime issues
        file.close()
        input('Press any key to continue.')

    # A function that will order the highscores into ASCENDING order
    def order_highscores(self):
        # Open the file based on the path
        file = open('scoreboard.txt', 'rt')
        # Get the array of scores by splitting with '\n'
        scores = file.read().split('\n')
        # Remove the last element since it is empty
        scores.pop()

        # Do nothing if there is no score record
        if len(scores) == 0: return

        # Bubble Sort Algorithm
        for i in range(len(scores)):
            swapped = False
            for j in range(0, len(scores)-i-1):
                if int(scores[j].split('\t')[2].split(':')[1]) > int(scores[j+1].split('\t')[2].split(':')[1]):
                    scores[j], scores[j+1] = scores[j+1], scores[j]
                    swapped = True
            if swapped == False:
                break
        
        # Close the file to avoid runtime issues
        file.close()

        # Rewrite the scores in the ascending form arranged using bubble sort algorithm
        file = open('scoreboard.txt', 'wt')
        for x in scores:
            file.write(x + '\n')
        file.close()

    # A function that allows the player to interact with the game
    def gui(self):
        os.system('cls')
        print('=================================')
        print('POKEMING - GON\'NA CATCH \'EM ALL')
        print('=================================')
        self.player.stats()
        print('=================================')
        self.enemy.stats()
        print('=================================')
        print('Action Menu')
        print('1) Attack')
        print('2) Heal (-3 MP)')
        print('3) Thunder (-20 MP)')
        print('4) Blizzard (-20 MP)')
        print('5) Fire (-20 MP)')
        print('6) Holy (-20 MP)')
        print('7) MP Pots (-3 Coins)')
        print('8) Highscores')
        return input('Choose an action: ')

    # A function that will spawn new enemy
    def spawn_new_enemy(self): 
        self.scoreboard = self.scoreboard + 1
        self.player.killed_an_enemy(self.enemy)
        self.enemy = Enemy(self.player)

    # A function that will called if the player died in the game
    def game_over(self):
        os.system('cls')
        print(f'Game over! Score: {self.scoreboard}')
        self.is_running = False
        self.set_highscore()

    # The main circuit of the game itself
    def game_logic(self):
        # Check if the game is currently running
        while self.is_running:
            # Calls the gui for the player to interact
            self.choice = self.gui()
            os.system('cls')

            # Sets the action choices that has connection to the gameplay
            action_choices = [ '1', '2', '3', '4', '5', '6', '7' ]

            # See the gui to see the equivalent of these numbers
            if self.choice == '1': 
                self.player.attack(self.enemy)
            elif self.choice == '2': 
                self.player.skill.heal()
            elif self.choice == '3': 
                self.player.skill.thunder(self.enemy)
            elif self.choice == '4': 
                self.player.skill.blizzard(self.enemy)
            elif self.choice == '5': 
                self.player.skill.fire(self.enemy)
            elif self.choice == '6': 
                self.player.skill.holy(self.enemy)
            elif self.choice == '7':
                self.player.pots()
            elif self.choice == '8':
                self.get_highscores()
            else: 
                print('Action does not exist')

            # Check if the action chosen was linked to the gameplay
            # Let the enemy attack if it true
            if self.choice in action_choices:
                self.enemy.attack(self.player)

            # Check if the player is dead 
            # Dead player = Game over
            if self.player.is_dead():
                self.game_over()
            
            # Check if the enemy died
            # Spawn a new enemy
            if self.enemy.is_dead():
                self.spawn_new_enemy()

x = Main()