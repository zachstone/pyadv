from player import Player, save, load
from combat import battle
from random import random
from drawutils import clear_screen, show_options
import os
import sys
import glob
import re

def create_account():
    while True:
        clear_screen()
        print('What would you like your character\'s name to be?')
        name = input()
        if name != '':
            break
    return Player(name.title())
    
def prompt(prompt):
    print(prompt)
    return input()
    
def quit_game():
    quit = show_options(['Yes', 'No'], 'Are you sure you want to quit the game?\n')
    if quit == 0:
        sys.exit()
    
def load_file():
    save_names = glob.glob('saves\\*.save')
    save_games = []
    #save_names = os.listdir('saves')
    #for name in save_names:
    #    if not name.endswith('.save'):
    #        save_names.remove(name)
    for i in range(len(save_names)):
        print(save_names[i])
        save_names[i] = save_names[i].split('.')[0].split('\\')[1]
        save_games.append(load(save_names[i]))
        
    if len(save_names) >= 1:
        try:
            player_choice = show_options([save_names[i] + ' (lvl ' + str(save_games[i].level) + ')' for i in range(len(save_names))],
                                         'What is your character\'s name?\n')
            return save_games[player_choice]
        except FileNotFoundError:
            pass
            
def main():
    clear_screen()
    player = None
    try:
        with open('saves/_continue.txt') as f:
            continue_name = f.read()
    except:
        continue_name = 'None'
    choice = show_options(['Continue - {}'.format(continue_name), 'Load', 'Create', 'Exit'])
    
    if choice == 0:
        player = load(continue_name)
    elif choice == 1:
        player = load_file()
    elif choice == 2:
        print('hello')
        player = create_account()
        save(player)
    elif choice == 3:
        quit_game()
        
    print(player.name, '-', player.level)
    for k, v in player.stats.items():
        print(k, '-', player.stats[k])
        
    while True:
        clear_screen()
        choice_num = show_options(['Walk Around', 'Fight', 'Sleep', 'Save'], 'What would you like to do? (Turn {})\n'.format(player.turns))
        
        if choice_num == 0:
            player.turns += 1
        elif choice_num == 1:
            player.turns += 1
            enemy = Player('Enemy')
            if battle(player, enemy) is True:
                cur_lvl = player.level
                exp_gain = int(random() * 8) + 1
                player.exp += exp_gain
                print('You won!', player.name, 'gains', exp_gain, 'exp.')
                if player.level > cur_lvl:
                    print(player.name, 'is now level', player.level)
            else:
                player = load_file()
        elif choice_num == 2:
            player.turns += 1
            player.full_restore()
            show_options(['Continue'], 'You feel well rested.\n')
        elif choice_num == 3:
            save(player)
            show_options(['Continue'], 'Your game was saved.\n')
        
def mainloop(player):
    pass
        
if __name__ == '__main__':
    main()