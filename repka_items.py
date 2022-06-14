from easygraphics import *
from PyQt5 import QtGui, QtCore
from random import *
from repka_defaults import *

## legacy name!
def shar(x, y, c):

     set_color(0)
     set_fill_color(0)
     fill_circle(x+1, y+1, 5)
     set_color(c)
     set_fill_color(c)
     fill_circle(x, y, 5)
     put_pixel(x-2,y-3,Color.WHITE)
     put_pixel(x-3,y-2,Color.WHITE)
     put_pixel(x-2,y-3,Color.WHITE)
     put_pixel(x+4,y,Color.BLACK)
     put_pixel(x+4,y+1,Color.BLACK)
     put_pixel(x+3,y+2,Color.BLACK)
     put_pixel(x+2,y+3,Color.BLACK)
     put_pixel(x+1,y+3,Color.BLACK)

def flush_keyboard():
    '''
    empties keyboard buffer
    '''
    while has_kb_msg(): tmp = get_key()

def draw_ammo_crate(x, y, is_live = True):

    if is_live:
        crate_color = crate_body_color
        lines_color = crate_lines_color
    else:
        crate_color = used_up_color
        lines_color = 0
    

    set_fill_color(0x00)
    fill_rounded_rect(x-5,y-6,x+7,y+8, 4, 4)
    fill_rounded_rect(x-4,y-5,x+8,y+9, 4, 4)
    set_fill_color(crate_color)
    fill_rounded_rect(x-6,y-7,x+6,y+7, 4, 4)
    set_color(lines_color)
    line(x-3, y-4, x+2, y-4)
    line(x-3, y, x+2, y)
    line(x-3, y+4, x+2, y+4)

def draw_life_crystal(x, y, is_live = True):
    if is_live:
        gem_color = life_gem_color
        eye_color = life_eye_color
    else:
        gem_color = used_up_color
        eye_color = 0

    set_fill_color(0)
    fill_polygon(x-5, y+1, x+1, y+10, x+7, y+1, x+1, y-4)
    set_fill_color(gem_color)
    fill_polygon(x-6, y, x, y+9, x+6, y, x, y-5)
    set_fill_color(eye_color)
    fill_circle(x,y,3)

def draw_bullet(b, is_live = True):
    x = b*2 + 7
    y = screen_height + 80
    if is_live:
        put_pixel(x, y, 0xFFFF00)
        set_color(crate_body_color)
    else:
        put_pixel(x, y, 0x666666)
        set_color(0x333333)

    draw_line(x, y+1, x, y+7)

def draw_bullets(b_num, is_live = True):
    for k in range(1, b_num + 1):
        draw_bullet(k, is_live)

def draw_obstacles(number):

    for k in range(number):

        x = randint(right_space, screen_width - left_space)
        y = randint(upper_limit + 3, lower_limit - 3)
        shar(x, y, Color.RED)

def draw_lives(life_num, rand_num = 10):

    # life crystals
    l_list = []
    t1 = []
    l_step = int((screen_width - right_space - left_space) / life_num)
    for k in range(life_num):
        x = (k+1)*l_step + randint(-10, 10)
        y = randint(60, screen_height + 40)
        if randint(0, rand_num):
            
            draw_life_crystal(x, y)
            t1 = [x, y]
            l_list.append(t1)
    return l_list
            
def draw_crates(ammo_num, rand_num = 10):

    # ammo crates
    a_list = []
    t1 = []
    a_step = int((screen_width - right_space - left_space) / ammo_num)
    for k in range(ammo_num):
        x = (k+1)*a_step + randint(-10, 10)
        y = randint(60, screen_height + 40)
        if randint(0, rand_num):
            draw_ammo_crate(x, y)
            t1 = [x, y]
            a_list.append(t1)

    return a_list           
    

def place_coins(number):

    for k in range(number):
        x = randint(40, 1000)
        y = randint(0, 600)
        c = randint(0, 2)
        r = randint(2, 6)
        set_color(0)
        set_fill_color(0)
        fill_circle(x+1, y+1, r)
        set_color(coin_color[c])
        set_fill_color(coin_color[c])
        fill_circle(x, y, r)

## functions to print stuff on top of the screen
def print_lives(lives, color = 0):
    '''
    print lives at default location
    '''
    ## set color according to lives left
    if not color:
        if lives > 5: set_color(lots_lives_color)
        elif lives > 1: set_color(default_lives_color)
        elif lives == 1: set_color(danger_lives_color)
        else: set_color(zero_lives_color)
    else: set_color(color)

    ## clear lives area
    set_fill_color(0)
    fill_rect(0,0,200,49)
    
    draw_rect_text(20, 10, 180, 36,
                   'Lives: ' + str(lives),
                   flags = QtCore.Qt.AlignLeft + QtCore.Qt.AlignTop)

def print_level(level, color = 0xAA0088):
    '''
    print level at default location
    '''
    set_color(color)
    draw_rect_text(screen_width//2 - 100, 10, 200, 36, 'Level: ' + str(level),
                   flags = QtCore.Qt.AlignHCenter  + QtCore.Qt.AlignTop)
    
def print_score(points, color = default_score_color):
    '''
    print score at default location
    '''
    set_color(color)       
    draw_rect_text(screen_width - 200, 10, 180, 36,
                   'Score: ' + str(points),
                   flags = QtCore.Qt.AlignRight  + QtCore.Qt.AlignTop)
        
def clear_excess_screen():
    set_fill_color(0)
    fill_rect(0,0,screen_width, 50)
    fill_rect(0,screen_height + 50,screen_width, screen_height + 100)
