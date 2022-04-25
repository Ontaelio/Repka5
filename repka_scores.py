import json
from datetime import date
from random import *
from os.path import exists

from easygraphics import *

from repka_defaults import *

def create_scores(play_mode):
    '''
    modify default_score_table to allow for skip10 mode
    (add 6 levels to skip10)
    '''
    
    if play_modes[play_mode] != 'skip10':
        return default_score_table
    else:
        s = default_score_table
        for r in s:
            r[1] += 6
        return s

def check_table(play_mode):
    '''
    Check whether scores file is present, and if not,
    create it and fill with default values
    '''
    filename = scores_file[play_mode]
    score_table = []
    try:
        with open(filename, 'r') as score_file:
            score_table = json.load(score_file)# = open(filename, 'r')
    except FileNotFoundError as e:
        with open(filename, 'w') as score_file:
            score_table = create_scores(play_mode)
            json.dump(score_table, score_file)

    except json.decoder.JSONDecodeError as e:
        print ('Error loading high scores table.')
        print("Please either delete the file 'repsa5.rep' or check "
              "it for consistency")
        return -1

    # sort by score, just in case
    score_table.sort(key = lambda x: x[2], reverse = True)
    return score_table

def check_unlocked_modes():
    '''
    check what modes are available at the start of the game
    '''

    if not exists(scores_file[0]): return 0
    scores = check_table(0)
    if scores == -1: return -1
    ##a_modes = [play_modes[0], 'locked', 'locked']
    if scores[0][2] > default_score_table[0][2]:
        scores = check_table(1)
        open_modes[1] = play_modes[1]
    if scores[0][2] > default_score_table[0][2]:
        #scores = check_table(2)
        open_modes[2] = play_modes[2]
    #return a_modes

def write_table(score_table, play_mode):
    '''
    Write the record table into a file
    '''
    filename = scores_file[play_mode]
    try:
        with open(filename, 'w') as score_file:
            json.dump(score_table, score_file)
    except PermissionError as e:
        print(f"File '{filename}' is write-protected.\n"
              "High scores are not saved.")

## lazy random name generator. For great justice!
def random_name(n = scores_name_prefix):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                  'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    was_consonant = 0
    was_vowel = 0
    s = ''
    name_len = randint(4, 8)

    while len(s) < name_len:
        if randint(0,1) and not randint(0, was_vowel):
            l = vowels[randint(0, len(vowels)-1)]
            was_vowel += 1
            was_consonant = 0
                    
        elif not randint(0, was_consonant):
            l = consonants[randint(0, len(consonants)-1)]
            was_vowel = 0
            was_consonant += 1

        else: l = ''
        s += l

    if n == '_date':
        today = date.today()
        d = today.strftime("%d.%m")
        return (s.title() + '_' + d)
    else:
        return (n + s.title())

## Drawing high score table entries
def print_score_place(k):
    if delay_fps(800):
        draw_rect_text(scores_rect_x1,
                   scores_rect_y1 + k * 21 + 19, 40, 20,
                   str(k+1), flags = QtCore.Qt.AlignRight)
    
def print_score_name(k, name):
    if delay_fps(800):
        draw_rect_text(scores_rect_x1 + 50, scores_rect_y1 + k * 21 + 19,
                   210, 20, name, flags = QtCore.Qt.AlignLeft)
    
    
def print_score_level(k, level):
    if delay_fps(800):
        draw_rect_text(scores_rect_x1 + 260, scores_rect_y1 + k * 21 + 19,
                       40, 20, level)

def print_score_points(k, pts):
    if delay_fps(800):
        draw_rect_text(scores_rect_x1 + 300, scores_rect_y1 + k * 21 + 19,
                       70, 20, pts, flags = QtCore.Qt.AlignRight)
    
## Entering new score
def get_letter():
    '''
    Input char
    '''

    c = ''
    c = get_key()
    #print(c.key)
    #if c.char: print(ord(c.char))
    if c.type == 6:
        if c.char:
            return ord(c.char)
        else: return 0
    else: return 0

def get_name(line, default_name):
    '''
    Enter name in high scores
    line is position in scores table
    '''

    s = default_name
    set_antialiasing(False)
    set_color(0xFFFFFF)
    set_write_mode(mode_XOR)
    
    
    while 1:
        print_score_name(line, s)
        n = get_letter()
        old_s = s
        if n == 8: # backspace
            if len(s): s = s[0 : len(s)-1]
        elif 31 < n < 127 and len(s) < 15:
            s += chr(n)
        elif n == 13:
            print_score_name(line, old_s)
            break
        
        print_score_name(line, old_s)    

    set_antialiasing(True)
    set_write_mode(0)
    return s
    
    
    
##init_graph(100,100)
##s = ''
##n = -1
##while 1:
##    n = get_letter()
##    print(n)
##    if n not in [-1, 0, None]:
##        s += n
##    elif n == -1: break
##
##print(s)
##        
