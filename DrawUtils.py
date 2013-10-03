from colorama import Fore, Back
import colorama
import os
import msvcrt

colorama.init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def fore_color(text_string, color):
    return color + text_string + Fore.RESET
    
def back_color(text_string, color):
    return color + text_string + Back.RESET
            
def show_options(options, text=''):
    """
    Receives a list of ('text', function) tuples. (Not any more)
    """
    highlight_pos = 0
    while True:
        clear_screen()
        print(text)
        
        for i in range(len(options)):
            if i == highlight_pos:
                print(back_color('> ' + options[i] + '  ', Back.GREEN))
            else:
                print('> ' + options[i] + '  ')
                
        key = msvcrt.getch()
        if key == b'\r' or key == b' ':
            return highlight_pos
        elif key == b'w':
            if highlight_pos > 0:
                highlight_pos -= 1
        elif key == b's':
            if highlight_pos < len(options) - 1:
                highlight_pos += 1
            