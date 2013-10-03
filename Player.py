from random import random
import pickle

class Player:
    stats = {}
    def __init__(self, name, stats = None, exp = 0):
        self.name = name
        self.exp = exp
        self.level = calc_level(self.exp)
        self.turns = 0
        if stats is None:
            self.stats['attack'] = 5
            self.stats['defense'] = 5
            self.stats['strength'] = 5
            self.stats['speed'] = 1
            self.stats['health'] = 100
        else:
            self.stats = stats
        self.cur_hp = self.stats['health']
        
    def attack(self, enemy):
        damage = int(random() * self.stats['strength'] * 2) + self.stats['attack']
        enemy.cur_hp -= damage
        return damage
        
    def full_restore(self):
        self.cur_hp = self.stats['health']
        
def calc_level(exp):
    for i in range(100):
        if exp_needed(i) > exp:
            return i - 1
    return
    
def exp_needed(level):
    exp = 0
    for i in range(1, level + 1):
        exp += i * i
    return exp
    
def _save(player):
    with open('save.zs', 'w') as f:
        savestring = []
        savestring.append(player.name)
        savestring.append(str(player.exp))
        for k, v in player.stats.items():
            savestring.append(k + ',' + str(v))
        f.write('\n'.join(savestring))

def _load():
    stats = {}
    text = ''
    with open('save.zs') as f:
        data = f.read().split('\n')
    name = data[0]
    exp = int(data[1])
    data.pop(0)
    data.pop(0)
    for line in data:
        k, v = line.split(',')
        stats[k] = int(v)
    return Player(name, stats, exp)
    
def save(player):
    ''' save(player) '''
    with open('saves/_continue.txt', 'w') as f:
        f.write(player.name)
    pickle.dump(player, open('saves/' + player.name + '.save', 'wb'))
    
def load(name):
    ''' player = load('MyName') '''
    with open('saves/_continue.txt', 'w') as f:
        f.write(name)
    return pickle.load(open('saves/' + name + '.save', 'rb'))
    