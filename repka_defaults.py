from PyQt5 import QtGui, QtCore

scores_file = ('repsa5.rep', 'repah5.rep', 'repfa5.rep')

screen_width = 1000
screen_height = 600
upper_limit = 51
lower_limit = screen_height + 50
right_space = 40
left_space = 20
scores_rect_x1 = 310
scores_rect_x2 = 690
scores_rect_y1 = 180
scores_rect_y2 = 600
scores_width = scores_rect_x2 - scores_rect_x1

title_repka_color_1 = 0xFF00FF
title_repka_fill_1 = 7
title_repka_color_2 = 0x999900
title_repka_fill_2 = 8
title_5_color_1 = 0xFFFF00
title_5_fill_1 = 8
default_twinkling_stars = 120

scores_screen_font = QtGui.QFont("Century Gothic", 12)
game_stats_font = QtGui.QFont("Century Gothic", 18)
#scores_name_prefix = 'Player_'
scores_name_prefix = '_date'


play_mode = 2
starting_level = (1, 11, 1)

# music_is_on = 1

default_lives_color = 0xDDDD00
danger_lives_color = 0xFF9900
zero_lives_color = 0xFF0100
lots_lives_color = 0x20DD00
default_level_color = 0xDD00CC
default_score_color = 0x00BBEE

explosion_speed = 80
default_fps_delay = (40, 40, 60)
min_fps_delay = (15, 15, 60)
max_fps_delay = (80, 90, 80)
death_radius = 19
starting_obstacles = 350
obstacles_per_level = 30

curpos_y = screen_height / 2
curpos_x = 0
starting_lives = 3
starting_ammo = 10
ammo_per_level = 5


mode_ADD = 12
mode_XOR = 26
used_up_color = 0x666666
crate_body_color = 0x247900
crate_lines_color = 0x00FFFF
life_gem_color = 0xFFFF00
life_eye_color = 0x00FFFF
explosion_edge = 0xFFAA00

dead_color = [0x000000,
              0XFFCCCC,
              0xFFAAAA,
              0xCF8888,
              0xAF6666,
              0x8F4444,
              0x7F3333,
              0x6F2222,
              0x4F1111,
              0x2F0000,
              0x0F0000]

coin_color = [0xAAAA00, 0x888899, 0xBB7700]
spice_color = [0xAA00AA, 0x00AAAA, 0x33AA77]

bg_color = [0x000000,
            0x000030,
            0x003000,
            0x270003,
            0x100901,
            0x001010,
            0x100010,
            0x070607,
            0x070013,
            0x130700,
            0x000909, #10
            0x001200,
            0x110001,
            0x000012,
            0x000505,
            0x050005,
            0x050401,
            0x020305,
            0x050302,
            0x020503,
            0x060202, #20
            0x000006,
            0x000600,
            0x050001,
            0x020202,
            0x000303,
            0x030201,
            0x030003,
            0x020400,
            0x000204,
            0x040002] #30

key_up = 16777235
key_down = 16777237
key_F10 = 16777273
key_fire = 32
key_ESC = 16777216
key_Enter = 16777220

default_score_table = [['Alpha', 15, 1500],
                       ['Bravo', 11, 900],
                       ['Charlie', 10, 800],
                       ['Delta', 9, 700],
                       ['Echo', 9, 650],
                       ['Foxtrot', 8, 600],
                       ['Golf', 8, 550],
                       ['Hotel', 7, 500],
                       ['India', 7, 450],
                       ['Juliet', 6, 400],
                       ['Kilo', 6, 370],
                       ['Lima', 6, 350],
                       ['Mike', 5, 320],
                       ['November', 5, 300],
                       ['Oscar', 5, 280],
                       ['Papa', 5, 270],
                       ['Quebec', 5, 260],
                       ['Romeo', 5, 250],
                       ['Sierra', 5, 240],
                       ['Oleg !!!11', 4, 12]]
    