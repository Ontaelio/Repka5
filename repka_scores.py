import json
from datetime import date
from random import *
from os.path import exists
from copy import deepcopy
from time import sleep

from easygraphics import *

from repka_defaults import *
from repka_title import *

def create_scores(play_mode):
    '''
    modify default_score_table to allow for skip10 mode
    (add 6 levels to skip10)
    '''
    
    if play_modes[play_mode] != 'skip10':
        return default_score_table
    else:
        s = deepcopy(default_score_table)
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
        print(f"Please either delete the file '{filename}' or check "
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
    
def after_game(level, points, score_table, play_mode):
    ## game end                
    # print(points)

    shade_color = color_rgb(0, 0, 0, 170)
    set_fill_style(1)
    set_fill_color(shade_color)
    fill_rect(0,0,screen_width, screen_height + 100)

    set_color(0xFFFF00)
    #set_line_style(3)
    #rect(scores_rect_x1, scores_rect_y1, scores_rect_x2, scores_rect_y2)

    print_repka(0xAAAA00, 11, 1)

    scores_screen_font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 4)
    set_font(scores_screen_font)

    draw_rect_text(scores_rect_x1, scores_rect_y1 - 20,
                       400, 20, top_scores_modes[play_mode])
    
    highscore = 0
    for k, entry in enumerate(score_table):
        
        set_color((((31 - k//2) * 8) << 16) + (((27 - k) * 8) << 8))
        print_score_place(k)

        if entry[2] < points:
            score_table.pop()
            score_table.insert(k, ['', level, points])
            highscore = k + 1
            set_color((((31 - k//2) * 8) << 16) + (27 - k) * 8)
            print_score_level(k, level)
            set_color((((25 - k) * 8) << 16) + (((31 - k//2) * 8) << 8) + (27 - k) * 8)
            print_score_points(k, points)
            points = 0

        else:
            print_score_name(k, entry[0])
            set_color((((31 - k//2) * 8) << 16) + (27 - k) * 8)
            print_score_level(k, entry[1])
            set_color((((25 - k) * 8) << 16) + (((31 - k//2) * 8) << 8) + (27 - k) * 8)
            print_score_points(k, entry[2])

    if highscore:
        k = highscore - 1
        score_table[k][0] = get_name(k, random_name())
        set_color((((31 - k//2) * 8) << 16) + (((27 - k) * 8) << 8))
        print_score_name(k, score_table[k][0])
        write_table(score_table, play_mode)

        if k == 0 and play_mode != 2:
            ## make new playmode available
            if open_modes[play_mode + 1] == 'locked':
                open_modes[play_mode + 1] = play_modes[play_mode + 1]

    set_color(used_up_color)
    scores_screen_font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
    set_font(scores_screen_font)
    if delay_fps(800): draw_rect_text(100, screen_height + 60, screen_width - 200, 20,
                                      'F10 to Quit, ESC to Title screen, any key to Play again')
    if delay_fps(100): flush_keyboard()

    
    ## needed for keyboard buffer to flush
    sleep(0.2)

    a = None
    
    while a != 6:
        if has_kb_msg():
            aa = get_key()
            a = aa.type
   
    set_fill_style(1)
    clear_excess_screen()
    set_color(used_up_color)
    draw_rect_text(100, screen_height + 60, screen_width - 200, 20, 'One moment...')

    if delay_fps(100): pass
    flush_keyboard()

    ## needed for keyboard buffer to flush
    sleep(0.2)

    return aa.key
        
