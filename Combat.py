from colorama import Fore, Back
from collections import deque
from DrawUtils import clear_screen
import time
import colorama
import os
    
def battle(player, enemy):
    def render(player_first):
        clear_screen()
        p_atk = (player_atk / enemy.stats['health']) * 64
        e_atk = (enemy_atk / player.stats['health']) * 64
        print('{}{}\n{}{}{}{}{}{}{}\n{}{}{}hp ({}{}{}%)  ---   <{}{}{}-{}{}{}-{}{}{}-{}{}{}-{}{}{}-{}{}{}> last 3 hits\n'.format(
               Fore.YELLOW, player.name,
               Back.GREEN, ' ' * round(player_avg_hp * 64), 
               Back.RED, ' ' * round(e_atk),
               Back.WHITE, ' ' * (64 - round((player_avg_hp * 64) + e_atk)), Back.RESET,
               Fore.GREEN, player.cur_hp, Fore.RESET,
               Fore.GREEN, round(player_avg_hp * 100), Fore.RESET,
               Fore.RED, hit_queue[5], Fore.RESET,
               Fore.RED, hit_queue[4], Fore.RESET,
               Fore.RED, hit_queue[3], Fore.RESET,
               Fore.RED, hit_queue[2], Fore.RESET,
               Fore.RED, hit_queue[1], Fore.RESET,
               Fore.RED, hit_queue[0], Fore.RESET))
        
        print('{}{}\n{}{}{}{}{}\n{}{}{}hp ({}{}{}%)  ---   <{}{}{}-{}{}{}-{}{}{}-{}{}{}-{}{}{}-{}{}{}> last 3 hits\n'.format(
               Fore.YELLOW, enemy.name,
               Back.GREEN, ' ' * int(enemy_avg_hp * 64), 
               Back.WHITE, ' ' * (64 - int(enemy_avg_hp * 64)), Back.RESET,
               Fore.GREEN, enemy.cur_hp, Fore.RESET,
               Fore.GREEN, int(enemy_avg_hp * 100), Fore.RESET,
               Fore.RED, enemy_hit_queue[5], Fore.RESET,
               Fore.RED, enemy_hit_queue[4], Fore.RESET,
               Fore.RED, enemy_hit_queue[3], Fore.RESET,
               Fore.RED, enemy_hit_queue[2], Fore.RESET,
               Fore.RED, enemy_hit_queue[1], Fore.RESET,
               Fore.RED, enemy_hit_queue[0], Fore.RESET))
               
        #if(player_first):
        #    print(''.join(player_message) + '\n' + ''.join(enemy_message))
        #else:
        #    print(''.join(enemy_message) + '\n' + ''.join(player_message))
        
        #print(''.join(player_message) + '\n' + ''.join(enemy_message))
            
    colorama.init()
    #total attacks
    player_atks = 0
    enemy_atks = 0
    
    #attacks per second
    player_aps = 1 / player.stats['speed']
    enemy_aps = 1 / enemy.stats['speed']
    
    start_time = time.time()
    player_next_atk = start_time + player_aps
    enemy_next_atk = start_time + enemy_aps
    
    player_atk = 0
    enemy_atk = 0
    
    hit_queue = deque([0, 0, 0, 0, 0, 0])
    enemy_hit_queue = deque([0, 0, 0, 0, 0, 0])
    
    player_avg_hp = player.cur_hp / player.stats['health']
    enemy_avg_hp = enemy.cur_hp / enemy.stats['health']
    while True:
        cur_time = time.time()
        
        if player_next_atk < cur_time:
            #print('player attack!')
            player_next_atk += player_aps
            #print('You hit the enemy for', player.attack(enemy), 'damage.')
            #print('<%s>' % player.attack(enemy))
            player_atk = player.attack(enemy)
            
            hit_queue.popleft()
            hit_queue.append(player_atk)
            
            if enemy.cur_hp <= 0:
                enemy.cur_hp = 0
                enemy_avg_hp = enemy.cur_hp / enemy.stats['health']
                render(True)
                print('Time elapsed:', int(cur_time - start_time), 'seconds.')
                return True
            else:
                enemy_avg_hp = enemy.cur_hp / enemy.stats['health']
                render(True)
                
        if enemy_next_atk < cur_time:
            #print('enemy attack!')
            enemy_next_atk += enemy_aps
            #print('The enemy hit you for', enemy.attack(player), 'damage.')
            #print('>%s<' % enemy.attack(player))
            enemy_atk = enemy.attack(player)
            player_avg_hp = player.cur_hp / player.stats['health']
            
            enemy_hit_queue.popleft()
            enemy_hit_queue.append(enemy_atk)
            
            if player.cur_hp <= 0:
                player.cur_hp = 0
                player_avg_hp = player.cur_hp / player.stats['health']
                render(False)
                print('Time elapsed:', int(cur_time - start_time), 'seconds.')
                return False
            else:
                player_avg_hp = player.cur_hp / player.stats['health']
                render(False)
                