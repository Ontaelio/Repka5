from easygraphics import *
from random import *

from repka_defaults import *

# letter blocks
repka_r = ([0,0],
           [0,1],
           [0,2],
           [0,3],
           [1,0],
           [1,2],
           [2,0],
           [2,1],
           [2,2],
           )

repka_e = ([0,0],
           [0,1],
           [0,2],
           [0,3],
           [1,0],
           [1,1.5],
           [1,3],
           [2,0],
           [2,1.5],
           [2,3]
           )

repka_p = ([0,0],
           [0,1],
           [0,2],
           [0,3],
           [1,0],
           [2,0],
           [2,1],
           [2,2],
           [2,3]
           )

repka_k = ([0,0],
           [0,1],
           [0,2],
           [0,3]
           )

repka_a = ([0,0],
           [0,1],
           [0,2],
           [0,3],
           [1,0],
           [1,2],
           [2,0],
           [2,1],
           [2,2],
           [2,3]
           )

repka_5 = ([0,0],
           [0,1],
           [0,2],
           [0,4],
           [1,0],
           [1,2],
           [1,4],
           [2,0],
           [2,0],
           [2,2],
           [2,3],
           [2,4]
           )

t_space_x = (screen_width / 20, 20)
t_block_size = (screen_width / 20, 20)
t_start_point_x = (screen_width / 40, scores_rect_x1 + 5)
t_start_point_y = (screen_height /6  - 6, scores_rect_y1 - t_block_size[1] * 4 - 37)
start_point_5 = t_start_point_y[0] + t_block_size[0] * 5 - 20

def paint_block(x, y, side_size = t_block_size[0]):
    '''
    draw a square block size sede_size for title
    '''


    if delay_fps(1000):
        fill_rect (x, y, x + side_size, y + side_size)

def starry_background(num = 10000):
    for k in range(0, num):
        r = randint(30, 90)
        g = randint(30, 90)
        b = randint(30, 90)
        color = (r << 16) + (g << 8) + b
        x = randint(0, screen_width - 1)
        y = randint(upper_limit, lower_limit)
        put_pixel(x, y, color)
    

def starry_night(num = 1000):
    for k in range(0, num):
        r = randint(110, 230)
        g = randint(110, 230)
        b = randint(110, 230)
        color = (r << 16) + (g << 8) + b
        x = randint(0, screen_width - 1)
        y = randint(upper_limit, lower_limit)
        put_pixel(x, y, color)
        if randint(1, 5) == 1:
            color = ((r//2) << 16) + (g//2 << 8) + b//2
            put_pixel(x+1, y, color)
            put_pixel(x-1, y, color)
            put_pixel(x, y+1, color)
            put_pixel(x, y-1, color)
            if randint(1, 5) == 1:
                color = ((r//3) << 16) + (g//3 << 8) + b//3
                put_pixel(x+2, y, color)
                put_pixel(x-2, y, color)
                put_pixel(x, y+2, color)
                put_pixel(x, y-2, color)
                
def print_5(color, f_style):

    set_fill_color(color)
    set_fill_style(f_style)
    x_start = screen_width/2 - t_block_size[0] * 1.5
    y_start = start_point_5

    for block in repka_5:
        x = x_start + block[0] * t_block_size[0]
        y = y_start + block[1] * t_block_size[0]
        paint_block(x, y, t_block_size[0])

   

def print_repka(color, f_style, scale = 0):
    

    space_x = t_space_x[scale]
    block_size = t_block_size[scale]
    start_point_x = t_start_point_x[scale]
    start_point_y = t_start_point_y[scale]

    set_fill_color(color)
    set_fill_style(f_style)
    
    
    for block in repka_r:
        x = block[0] * block_size + start_point_x
        y = block[1] * block_size + start_point_y
        paint_block(x, y, block_size)
        
    for block in repka_e:
        x = block[0] * block_size + start_point_x + block_size * 3 + space_x
        y = block[1] * block_size + start_point_y
        paint_block(x, y, block_size)
        
    for block in repka_p:
        x = block[0] * block_size + start_point_x + block_size * 6 + space_x * 2
        y = block[1] * block_size + start_point_y
        paint_block(x, y, block_size)
        
    for block in repka_k:
        x = block[0] * block_size + start_point_x + block_size * 9 + space_x * 3
        y = block[1] * block_size + start_point_y
        paint_block(x, y, block_size)
                   
        fill_polygon (start_point_x + block_size * 10 + space_x * 3, start_point_y + block_size * 1.5,
                      start_point_x + block_size * 11.2 + space_x * 3, start_point_y,
                      start_point_x + block_size * 12 + space_x * 3, start_point_y + block_size / 1.4,
                      start_point_x + block_size * 10.5 + space_x * 3, start_point_y + block_size * 2.2)

        fill_polygon (start_point_x + block_size * 10 + space_x * 3, start_point_y + block_size * 2.5,
                      start_point_x + block_size * 11.2 + space_x * 3, start_point_y  + block_size * 4,
                      start_point_x + block_size * 12 + space_x * 3, start_point_y + + block_size * 4 - block_size / 1.4,
                      start_point_x + block_size * 10 + space_x * 3, start_point_y + block_size * 1.5)
        
    for block in repka_a:
        x = block[0] * block_size + start_point_x + block_size * 12 + space_x * 4
        y = block[1] * block_size + start_point_y
        paint_block(x, y, block_size)

    #print_5 (0xFFFF00, f_style)
        


    
