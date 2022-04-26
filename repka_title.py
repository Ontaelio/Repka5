from easygraphics import *
from random import *

from repka_defaults import *
from repka_items import *
from random import *

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



def random_spice(number, qty, c):
    '''
    Draws 'spice' (aka nebulae) on the screen.
    number = number of nebulaes
    qty = size of nebulae
    c = color
    '''

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
        
def draw_level_select(buf, lvl = None):
    '''
    draws (or re-draws) play mode select strings.
    takes arguments: buf, lvl = None
    buf = a get_image() image under the select string
    lvl = current mode to highlight (none is highlighted if None)
    '''
    
    set_font(scores_screen_font)
    set_color(used_up_color)

    put_image(0, txt_pos_y, buf) #, screen_width, 20)
    #p.beginNativePainting()
    for k, m in enumerate(open_modes):
        draw_rect_text(txt_pos_x[k], txt_pos_y,
                       100, 20, m, flags = QtCore.Qt.AlignHCenter)

    if lvl != None:
        set_color(0xFFFFFF)
        draw_rect_text(txt_pos_x[lvl], txt_pos_y,
                       100, 20, play_modes[lvl], flags = QtCore.Qt.AlignHCenter)

    

def draw_title_screen(play_mode):
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
    set_antialiasing(False)

    buf = create_image(screen_width, 20)
    get_image(0, txt_pos_y, screen_width, 20, buf)
    draw_level_select(buf, play_mode)
    #save_image('bug_'+str(randint(0,1000))+'.png')
    return buf

def mode_select(b, m, key):
    if key == key_left and m > 0:
        m -= 1
        draw_level_select(b, m)
        
    if key == key_right and m < 2:
        if open_modes[m+1] != 'locked': m += 1
        draw_level_select(b, m)
        
    return m
    

def title_screen_wait(buf, m_sel):
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
    aa = None
    

    ## wait for a key to be _released_ (7)
    while a != 7 or aa.key in [key_left, key_right]:
        if has_kb_msg():
            aa = get_key()
            a = aa.type
            if a == 6 and aa.key in [key_left, key_right]:
                m_sel = mode_select(buf, m_sel, aa.key)
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
    return aa.key, m_sel


    
