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


   


def collapsing_xor_circle(fps_delay, x, y, r = 30):
    '''
    not used, written for a non-implemented alternative trick ('dive')
    draws a collapsing circle using XOR, blocking
    '''

    set_color(0xFFFFFF)
    set_write_mode(mode_XOR)
    for k in range(r, 0, -1):
        if delay_jfps(1000): circle(x, y, k)
        if delay_jfps(fps_delay): circle(x, y, k)
        # pause()

    set_write_mode(0)

def starting_xor_circle(x, y, r, fps, color):
    '''
    draws an expanding circle at the starting point.
    waits for keyboard input
    x, y, r = circle
    fps = current fps
    color = color
    '''

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
    '''
    Explosion after colliding with a red sphere and dying.
    Not the same as bullet-hit one.
    x, y = coordinates;
    r=25 by default
    '''

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



def advance_hero(curpos_x, curpos_y, fps_delay, direction, was_dead):
    '''
    draw the player line one pixel forward.
    Accepts args:
    x, y - position of the new pixel
    fps_delay
    direction (1 or -1)
    was_dead - in case a bloody trail is needed
    returns:
    was_dead
    '''
    
    ## Testing for the bloody trail
    if was_dead:
        if delay_jfps(fps_delay):
            put_pixel(curpos_x, curpos_y, dead_color[was_dead])
            put_pixel(curpos_x-1, curpos_y, dead_color[was_dead])
            was_dead -= 1
            return was_dead

    ## normal while pixel with shadow
    
    else:
        if delay_jfps(fps_delay):
            #put_pixel(curpos_x-1, curpos_y + 1, 0)
            put_pixel(curpos_x-1, curpos_y, 0xFFFFFF)
                
            #put_pixel(curpos_x, curpos_y + 1, 0)
            put_pixel(curpos_x, curpos_y, 0xFFFFFF)
        if direction == 1:
            put_pixel(curpos_x-1, curpos_y + 2, 0)
        else:
            put_pixel(curpos_x, curpos_y + 1, 0)
    

def game_core(play_mode):
    global now_playing
    
    curpos_x = 0
    curpos_y = screen_height / 2
    direction = 1
    fps_delay = default_fps_delay[play_mode]
    was_dead = 0
    level = starting_level[play_mode]
    lives = starting_lives - (play_mode != 2)*1
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
            if play_mode == 0 and level == starting_level[play_mode]:
                play_song(start_track)
                now_playing = start_track            
            else:
                if play_mode == 2 and level < 10:
                    track = select_track(fps_delay-1, play_mode)
                else: track = select_track(fps_delay, play_mode)
                
                    
                #print(track, now_playing)
                if track != now_playing:
                    #print(f'playing: {now_playing}, changing track')
                    stop_song()
                    play_song(track)
                    now_playing = track
                    
        
        # background color aka spice_base (random after lvl 30)
        if level < 31: spice_base = bg_color[level]
        else: spice_base = bg_color[randint(23,30)]

        if play_mode == 2:
            if level < 6: spice_base = hcore_color[level]
            else:
                spice_base = hcore_color[randint(6,17)]
        
        set_background_color(spice_base)

        spice_collected = 0
        lives_per_level = 0

        bullets_fired = 0
        bulpos_x = 0
        bulpos_y = 0
        bul_color = 0
        bullets_explosion = []
        expl_radius = 0

        if play_mode != 2: lives += 1

        print('Level:', level)
        print('FPS:', fps_delay)

        clear_device()
        

        ## draw spice
        random_spice(level + (play_mode == 2)*5,
                     spice_density[play_mode],
                     spice_base)
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
        put_pixel(curpos_x, curpos_y, 0xFFFFFF)

        a = None
        while not a: a = starting_xor_circle(0, curpos_y, 20, fps_delay, 0x00FF00)
        if a.key == key_up: direction = -1
        elif a.key == key_down: direction = 1
       
        curpos_x += 1
        
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
                
                    
                    

            was_dead = advance_hero(curpos_x, curpos_y, fps_delay, direction, was_dead)
                

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
                
                for u in life_crystals:
                    if abs(curpos_x - u[0]) < 10:
                        draw_life_crystal(u[0], u[1], False)
                        draw_life_crystal(lives_per_level * 15 + 15, screen_height + 65)
                        lives_per_level +=1
                        if play_mode == 2:
                            lives += 1
                            print_lives(lives - 1)
                        else:
                            if lives_per_level > 3:
                                lives += 1
                                print_lives(lives - 1)

                        # the break below actually produced a rare and almost inabusable
                        # bug with _wrong_ life crystal being shut down on the same X axis.
                        # (as in, a new one was created after shooting, and it happens to
                        # sit on the same X axis or really close to it; the code finds the
                        # first one and breaks, then repeats when get_pixel() returns yellow
                        # _again_ on the next step, and so on until we pass the crystal,
                        # producing a ton of lives. It still gives one extra yellow crystal,
                        # but that's all). Without the break both crystals are shut down.
                        # Same for ammo below.
                        #break

            # ammo crate
            elif current_pixel == crate_body_color:                
                # pulia vnizu(lives_per_level * 15 + 10, screen_height + 65)
                
                for u in ammo_crates:
                    if abs(curpos_x - u[0]) < 10:
                        draw_ammo_crate(u[0], u[1], False)
                        ammo += 10
                        draw_bullets(ammo)
                        #break

            # spice check
            elif (current_pixel != used_up_color
                  and current_pixel != explosion_edge
                  and current_pixel > spice_base):
                spc = current_pixel / spice_base
                
                spice_collected += spc
                sx = screen_width - 1 - (randint(0, 10) * randint(1,5) * randint(1, 5))
                sy = randint(1, 49) + screen_height + 50

                ##print(spc)
                try:
                    play_sound(int(spc*100 + 37), 1)
                except ValueError:
                    # This is a rare bug that happens on later evels if a life crystal was
                    # partially destroyed by an explosion, exposing it's cyan 'eye', and the
                    # active pixel wanders right into it.
                    # This produces a ton of points (like 360), but otherwise is harmless.
                    # Can it be exploited? Sure. But such marksmanship should be rewarded!
                    #
                    #print('Sound error caught. spc ==', spc,'getpixel =', current_pixel)
                    #save_image('bug_'+str(randint(0,1000))+'.png')
                    print('* Jackpot! * ', spc//10, 'pts.')
                    
                
                # place collected spice in the vault
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
            if play_mode != 2: ammo += ammo_per_level
        
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


def main():
    global music_is_on
    global now_playing
    
    play_mode = 0
    check_unlocked_modes()
       
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
            menu_buffer = draw_title_screen(play_mode)
            

            ## title screen returns the key pressed
            next_stage, play_mode = title_screen_wait(menu_buffer, play_mode)
            score_table = check_table(play_mode)
            #save_image('test'+str(randint(0,1000))+'.png')
            if music_is_on: stop_song()

        if next_stage != key_ESC:
            
            level, points = game_core(play_mode)
            # testing stuff
            # points += 1600
            if music_is_on: stop_song()
        else:
            level = 0
            points = 0

        set_antialiasing(True)
        if music_is_on: play_song(scores_track)
        now_playing = scores_track
        next_stage = after_game(level, points, score_table, play_mode)
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
    

#main()
easy_run(main)
