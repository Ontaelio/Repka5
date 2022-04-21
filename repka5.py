import sys
from time import sleep
from random import *

try:
    from PyQt5 import QtGui, QtCore
    from easygraphics import *
except ModuleNotFoundError as e:
    print('Essential modules not found.\n'
          'Please install PyQt5 and EasyGraphics:\n'
          '> pip install PyQt5\n'
          '> pip install easygraphics\n')
    sys.exit()

## sound module in the works!
try:
    import winsound
except ImportError:
    ## some code needed here for alternative ways to produce
    ## beep on non-Windows systems
    # print('Sounds available only on Windows systems, sorry.')
    # sound_on = False
    def play_sound(frequency, duration):
        pass
else:
    # if sound_on: print('Sound is ON')
    # else: print('Sound is OFF')
    def play_sound(frequency, duration):
        ''' play a single beep sound '''
        winsound.Beep(frequency, duration)


from repka_items import *
from repka_defaults import *
from repka_title import *
from repka_scores import *
from repka_music import *



def flush_keyboard():
    '''
    empties keyboard buffer
    '''
    while has_kb_msg(): tmp = get_key()

def random_spice(number, qty, c):

    step_x = int(screen_width / (number + 1))
    y = randint(screen_height/2, screen_height/2 + 100)

    set_write_mode(mode_ADD)

    for k in range(number):
        x = step_x * (k + 1) + randint(0 - step_x, step_x)
        set_color(c)
        set_fill_color(c)
        for k1 in range(qty):
            r = randint(1,5)
            if randint(0, 1): fill_circle(x,y,r)
            else:
                if randint(0, 1): fill_rect(x, y, x+r, y+r)
                else: fill_rect(x-r, y-r, x, y)
            
            
            x+= r * (randint(0,1)*2-1)
            y+= r * (randint(0,1)*2-1)
            if y > lower_limit: y = screen_height - 50
            elif y < upper_limit: y = 100
        

    set_write_mode(0)
    


def collapsing_xor_circle(x, y, r = 30):

    set_color(0xFFFFFF)
    set_write_mode(mode_XOR)
    for k in range(r, 0, -1):
        if delay_jfps(1000): circle(x, y, k)
        if delay_jfps(fps_delay): circle(x, y, k)
        # pause()

    set_write_mode(0)

def starting_xor_circle(x, y, r, fps, color):

    set_color(color)
    set_write_mode(26)
    for k in range(1, r):
        if delay_fps(800): circle(x, y, k)
        if delay_fps(fps): circle(x, y, k)
        if has_kb_msg():
            a = get_key()
            set_write_mode(0)
            return a
    
        # pause()

    

def expanding_circle(x, y, r = 25):

    set_color(0xFFFF00)
    set_fill_color(get_background_color())
    if delay_jfps(explosion_speed): circle(x, y, 1)
    if delay_jfps(1000): circle(x, y, 2)
    set_color(0xFFFFFF)
    if delay_jfps(explosion_speed): circle(x, y, 1)
    set_color(0xFFFF00)
    if delay_jfps(1000): circle(x, y, 3)
    set_color(0xFFFFFF)
    if delay_jfps(explosion_speed): circle(x, y, 2)
    set_color(0xAA7700)
    if delay_jfps(1000): circle(x, y, 1)
    
    
    for k in range(1, r-3):
        set_color(0xFFFF00 - 0x010600 * k)
        if delay_jfps(1000): circle(x, y, k+3)
        set_color(0xFFFFFF - 0x010600 * k)
        if delay_jfps(explosion_speed): circle(x, y, k+2)
        set_color(0xCC8800 - 0x010600 * k)
        if delay_jfps(1000): circle(x, y, k+1)
        set_color(get_background_color())
        if delay_jfps(explosion_speed): fill_circle(x, y, k)
    set_color(0xCC8800 - 0x010600 * (r-1))
    if delay_jfps(1000): circle(x, y, r-3)
    set_color(get_background_color())
    if delay_jfps(explosion_speed): fill_circle(x, y, r-2)
    set_color(0xCC8800 - 0x010600 * r)
    if delay_jfps(explosion_speed): circle(x, y, r-2)
    set_color(get_background_color())
    if delay_jfps(explosion_speed): fill_circle(x, y, r-1)
    if delay_jfps(explosion_speed): fill_circle(x, y, r)

    set_fill_color(used_up_color)
    set_color(used_up_color)

    fill_circle(x, y-4, 4)
    line(x-5, y+6, x+5, y+2)
    line(x-5, y+2, x+5, y+6)
    put_pixel(x-2,y-5,Color.BLACK)
    put_pixel(x+2,y-5,Color.BLACK)



def draw_title_screen():
    set_background_color(0x100328)
    set_fill_style(1)
    clear_device()
    starry_background(15000)
    random_spice(2, 5000, 0x070101)
    random_spice(2, 5000, 0x010801)
    random_spice(2, 7000, 0x060400)
    random_spice(2, 5000, 0x030012)
    random_spice(2, 7000, 0x080105)
    starry_night(1200)
    clear_excess_screen()
    print_repka(title_repka_color_1, title_repka_fill_1)
    print_repka(title_repka_color_2, title_repka_fill_2)
    print_5 (title_5_color_1, title_5_fill_1)


def title_screen_wait():
    stars = {}

    # create a dict to hold stars
    for k in range(default_twinkling_stars):
        r = randint(150, 255)
        g = randint(150, 255)
        b = randint(150, 255)
        color = (r << 16) + (g << 8) + b
        stars[k] = [randint(0, screen_width - 1), randint(upper_limit, lower_limit), color, False]

    if has_kb_msg(): a = get_key()
    a = None

    ## wait for a key to be _released_ (7)
    while a != 7:
        if has_kb_msg():
            aa = get_key()
            a = aa.type
        k = randint(0, 99)

        # if this star is not active
        if not stars[k][3]:
            t = get_pixel(stars[k][0], stars[k][1])
            if delay_jfps(10): put_pixel(stars[k][0], stars[k][1], stars[k][2])
            stars[k][2] = t
            stars[k][3] = True

        else:
            if delay_jfps(10): put_pixel(stars[k][0], stars[k][1], stars[k][2])
            stars[k][0] = randint(0, screen_width)
            stars[k][1] = randint(upper_limit, lower_limit)
            r = randint(150, 255)
            g = randint(150, 255)
            b = randint(150, 255)
            color = (r << 16) + (g << 8) + b
            stars[k][2] = color
            stars[k][3] = False

    #print(aa.key)
    return aa.key

def game_core():
    global now_playing
    
    curpos_x = 0
    curpos_y = screen_height / 2
    direction = 1
    fps_delay = default_fps_delay[play_mode]
    was_dead = 0
    level = starting_level[play_mode]
    lives = starting_lives - 1
    points = 0
    ammo = starting_ammo

    life_crystals = []
    ammo_crates = []
    
    ## draw the field
    set_fill_style(1)
    ## antialiasing must be off for correct get_pixel() readings
    set_antialiasing(False)

    flush_keyboard()
    a = None



    ## main game loop
    while lives > 0:

        if music_is_on:
            if level == starting_level[play_mode]:
                play_song(start_track)
                now_playing = start_track            
            else:
                track = select_track(fps_delay)
                if track != now_playing:
                    stop_song()
                    play_song(track)
                    now_playing = track
                    
        
        # background color aka spice_base (random after lvl 30)
        if level < 31: spice_base = bg_color[level]
        else: spice_base = bg_color[randint(23,30)]
        set_background_color(spice_base)

        spice_collected = 0
        lives_per_level = 0

        bullets_fired = 0
        bulpos_x = 0
        bulpos_y = 0
        bul_color = 0
        bullets_explosion = []
        expl_radius = 0

        lives += 1

        print('Level:', level)
        print('FPS:', fps_delay)

        clear_device()
        

        ## draw spice
        random_spice(level, 2500, spice_base)
        ## draw red spheres (qty)
        if level % 10:
            draw_obstacles(starting_obstacles + obstacles_per_level * level)
        ## draw ammo crates and life crystals
        ammo_crates = draw_crates(10,2)
        life_crystals = draw_lives(14, 2)
        

        ## clear bars on top and bottom
        clear_excess_screen()
        set_color(used_up_color)
        draw_line(0,50, screen_width, 50)
        draw_line(0,screen_height + 50, screen_width, screen_height + 50)

        ## print stats
        game_stats_font.setLetterSpacing(QtGui.QFont.AbsoluteSpacing, 1)
        set_font(game_stats_font)
        print_lives(lives - 1)
        print_level(level)
        print_score(points)
        
        

        ## draw bullet reserve       
        draw_bullets(ammo)

        ## show starting location, wait for a keypress
        a = None
        while not a: a = starting_xor_circle(0, curpos_y, 20, fps_delay, 0x00FF00)
                
        if a.key == key_up: direction = -1
        elif a.key == key_down: direction = 1
        
        ## go through a level
        while curpos_x < screen_width-1:

            ## bullets first
            if bullets_fired:
                put_pixel(bulpos_x, bulpos_y, bul_color)
                bulpos_x += 3
                if bulpos_x < screen_width:
                    bul_color = (get_pixel(bulpos_x, bulpos_y)).rgb() & 0xFFFFFF
                    if bul_color == 0xFF0000:
                        # expanding_circle(bulpos_x, bulpos_y, death_radius)
                        # bullets_fired = 0
                        bullets_explosion = [bulpos_x, bulpos_y]
                        expl_radius = 3
                        bullets_fired = 0
                        
                    else:
                        put_pixel(bulpos_x, bulpos_y, 0xFFFFFF)
                else: bullets_fired = 0

            ## explosion is happening
            if bullets_explosion:
                if expl_radius < death_radius:
                    set_color(explosion_edge)
                    circle(bullets_explosion[0], bullets_explosion[1], expl_radius)
                    set_fill_color(spice_base)
                    fill_circle(bullets_explosion[0], bullets_explosion[1], expl_radius -1)
                    expl_radius += 2
                else:
                    set_fill_color(spice_base)
                    fill_circle(bullets_explosion[0], bullets_explosion[1], expl_radius)
                    k = randint(0, 9)
                    if k == 2:
                        draw_life_crystal(bullets_explosion[0], bullets_explosion[1])
                        life_crystals.append(bullets_explosion)
                    elif k == 3:
                        draw_ammo_crate(bullets_explosion[0], bullets_explosion[1])
                        ammo_crates.append(bullets_explosion)
                    bullets_explosion = []
                
                    
                    

            ## Testing for the bloody trail
            if was_dead:
                if delay_jfps(fps_delay):
                    put_pixel(curpos_x, curpos_y, dead_color[was_dead])
                    was_dead -= 1

            ## normal while pixel with shadow
            
            else:
                if delay_jfps(fps_delay):
                    put_pixel(curpos_x, curpos_y, 0xFFFFFF)
                    put_pixel(curpos_x, curpos_y + 1, 0)
                

            ## advance position
            curpos_x +=1
            curpos_y += direction
            if curpos_y < upper_limit: curpos_y = lower_limit
            if curpos_y > lower_limit: curpos_y = upper_limit

            ## check new position for obstacles
            current_pixel = (get_pixel (curpos_x, curpos_y)).rgb() & 0xFFFFFF
            
            if  current_pixel == 0xFF0000:
                expanding_circle(curpos_x, curpos_y, death_radius)
                lives -= 1                
                if not lives: break
                print_lives(lives - 1)
                was_dead = 10

            # life crystal
            elif current_pixel == life_gem_color:                
                draw_life_crystal(lives_per_level * 15 + 15, screen_height + 65)
                lives_per_level +=1
                if lives_per_level > 3:
                    lives += 1
                    print_lives(lives - 1)
                for u in life_crystals:
                    if abs(curpos_x - u[0]) < 10:
                        draw_life_crystal(u[0], u[1], False)
                        break

            # ammo crate
            elif current_pixel == crate_body_color:                
                # pulia vnizu(lives_per_level * 15 + 10, screen_height + 65)
                ammo += 10
                draw_bullets(ammo)
                for u in ammo_crates:
                    if abs(curpos_x - u[0]) < 10:
                        draw_ammo_crate(u[0], u[1], False)
                        break

            # spice check
            elif (current_pixel != used_up_color
                  and current_pixel != explosion_edge
                  and current_pixel > spice_base):
                spc = current_pixel / spice_base
                
                spice_collected += spc
                sx = screen_width - 1 - (randint(0, 10) * randint(1,5) * randint(1, 5))
                sy = randint(1, 49) + screen_height + 50

                ##print(spc)
                play_sound(int(spc*100), 1)
                
                put_pixel(sx, sy, current_pixel)
                # print(int(a))
                #if a > 30: pause()

            ## check keys
            if has_kb_msg():
                a = get_key()
                # check key press (not release)
                if a.type == 6:
                    #print(a.key)
                    # directional keys
                    if a.key == key_up: direction = -1
                    elif a.key == key_down: direction = 1

                    # fire!
                    elif a.key == key_fire:
                        if ammo and not bullets_fired:
                            draw_bullet(ammo, False)
                            ammo -= 1
                            bulpos_x = curpos_x + 1
                            bulpos_y = curpos_y
                            bul_color = (get_pixel(bulpos_x, bulpos_y)).rgb() & 0xFFFFFF
                            bullets_fired = 1
                            
                    # exit
                    elif a.key == key_F10:
                       
                       close_graph()
                       close_music_device()
                       sys.exit()

        
        if lives:
            level +=1
            points += round(spice_collected / 10)
            ammo += ammo_per_level
        
            if play_mode == 2:
                fps_delay += 4
            elif lives_per_level > 4:
                fps_delay -= round(fps_delay / 10)
                    #print(fps_delay)
            elif lives_per_level < 3:
                fps_delay += (3 - lives_per_level) * (round(fps_delay/12) + 1)
                
            if fps_delay < (min_fps_delay[play_mode] + level):
                fps_delay = min_fps_delay[play_mode] + level
            if fps_delay > max_fps_delay[play_mode]:
                fps_delay = max_fps_delay[play_mode]
            curpos_x = 0

    return level, points

def after_game(level, points, score_table):
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

    draw_rect_text(scores_rect_x1, scores_rect_y1 - 25,
                       400, 20, 'T O P  S C O R E S')
    
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
        write_table(score_table)

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
    
def main():
    global music_is_on
    
    
    score_table = check_table()    
    init_graph(screen_width, screen_height+100)
    set_caption('Repka 5')
    if music_is_on:
        music_is_on = check_music_files()
        if not music_is_on:
            print('Music disabled')
    #music_is_on = 0
    # MainWindow = QtWidgets.QWidget()
    # MainWindow.showFullScreen()
    set_render_mode(RenderMode.RENDER_MANUAL)

    # show title screen after start
    go_to_title = True

    while 1:

        if go_to_title:
            ## title screen
            set_antialiasing(True)
            if music_is_on: play_song(title_track)
            draw_title_screen()
            

            ## title screen returns the key pressed
            next_stage = title_screen_wait()
            if music_is_on: stop_song()

        if next_stage != key_ESC:
            
            level, points = game_core()
            if music_is_on: stop_song()
        else:
            level = 0
            points = 0

        set_antialiasing(True)
        if music_is_on: play_song(scores_track)
        next_stage = after_game(level, points, score_table)
        if music_is_on: stop_song()

        if next_stage == key_F10:
            break
        elif next_stage == key_ESC:
            go_to_title = True
        else:
            go_to_title = False
            next_stage = 'Level 1'
        


    close_graph()
    if music_is_on: close_music_device()
    


easy_run(main)
