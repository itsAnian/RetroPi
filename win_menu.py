import pygame
import time
from PIL import Image
from PIL import ImageDraw
try:
    from RGBMatrixEmulator import RGBMatrix, RGBMatrixOptions
except ImportError:
    from rgbmatrix import RGBMatrix, RGBMatrixOptions

options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options=options)

joystick_found = True
pygame.init()
try:
    pygame.joystick.init()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    joystick.get_numaxes()
except Exception:
    joystick_found = False
    print("Kein Joystick gefunden")

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_BLUE = (0,255,255)
PLAY_COLOR = WHITE
EXIT_COLOR = WHITE
BORDER_COLOR = WHITE

RETURN = 0

x = 0
play_color = (GREEN)
exit_color = (WHITE)
save_color = (WHITE)
running = True

input_lock_time = .3
last_input_time = 0

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)

def draw_winmenu():
    #draw w
    draw.rectangle((9,3,9,7), fill=(WHITE))
    draw.point ((10,6), fill=(WHITE))
    draw.point ((11,5), fill=(WHITE))
    draw.point ((12,6), fill=(WHITE))
    draw.rectangle((13,3,13,7), fill=(WHITE))

    #draw i
    draw.rectangle((15,3,15,7), fill=(WHITE))

    #draw n
    draw.rectangle((17,3,17,7), fill=(WHITE))
    draw.rectangle((18,4,18,4), fill=(WHITE))
    draw.rectangle((19,5,19,5), fill=(WHITE))
    draw.rectangle((20,6,20,6), fill=(WHITE))
    draw.rectangle((21,3,21,7), fill=(WHITE))
    #draws underline for Menu
    draw.rectangle((3,9,28,9),fill=(WHITE))
    draw.rectangle((3,7,3,9),fill=(WHITE))
    draw.rectangle((28,7,28,9),fill=(WHITE))

def draw_box(x):
    #draws box for play arrow
    draw.rectangle((2+x,11,2+x,21),fill=(BORDER_COLOR))
    draw.rectangle((2+x,11,10+x,11),fill=(BORDER_COLOR))
    draw.rectangle((10+x,11,10+x,21),fill=(BORDER_COLOR))
    draw.rectangle((2+x,21,10+x,21),fill=(BORDER_COLOR))

def draw_arrow(color):
    #draws arrow
    draw.rectangle((5,14,5,18),fill=(color))
    draw.rectangle((6,15,6,17),fill=(color))
    draw.rectangle((7,16,7,16),fill=(color))

def draw_exit(color):
    #draws x
    draw.point((24,15),fill=(color))
    draw.point((25,16),fill=(color))
    draw.point((26,17),fill=(color))
    draw.point((27,18),fill=(color))
    draw.point((28,19),fill=(color))
    draw.point((24,19),fill=(color))
    draw.point((25,18),fill=(color))
    draw.point((26,17),fill=(color))
    draw.point((27,16),fill=(color))
    draw.point((28,15),fill=(color))

def draw_save(color):
    #draws save
    draw.rectangle((15,13,15,19),fill=(color))
    draw.rectangle((16,13,16,20),fill=(color))
    draw.rectangle((17,13,17,19),fill=(color))
    draw.rectangle((13,17,19,17),fill=(color))
    draw.rectangle((14,18,18,18),fill=(color))

def move_box():
    global x
    global running
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:  #movment of the select box
        x -= 10
    if keys[pygame.K_RIGHT] and x <= 10:
        x += 10

    if keys[pygame.K_RETURN]: #if enter is pressed
        if x == 0:
            print("PLAY")
            running = False
        if x == 10:
            print("SAVE")
            running = False
        if x == 20:
            print("EXIT")
            running = False

def set_color():
    global play_color
    global exit_color
    global save_color
    #sets the colors for the content of the boxes
    if x == 0:
        play_color = (GREEN)
        save_color = (WHITE)
        exit_color = (WHITE)
    if x == 10:
        play_color = (WHITE)
        save_color = (LIGHT_BLUE)
        exit_color = (WHITE)
    if x == 20:
        play_color = (WHITE)
        save_color = (WHITE)
        exit_color = (RED)

def move_box_joy(x_axis):
    global x
    global running
    global last_input_time
    global input_lock_time

    current_time = time.time()
    threshold = 0.1
    if current_time - last_input_time > input_lock_time:
        x_axis = 0 if abs(x_axis) < threshold else x_axis
        if x_axis > 0 and x > 0:
            x -= 10
            last_input_time = current_time
        elif x_axis < 0 and x < 20:
            x += 10
            last_input_time = current_time

    if joystick.get_button(RETURN):
        if x == 0:
            print("PLAY")
            running = False
        if x == 10:
            print("SAVE")
            running = False
        if x == 20:
            print("EXIT")
            running = False

clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated

while running:
    if joystick_found:
        x_axis = joystick.get_axis(0)
        move_box_joy(x_axis)
    else:
        move_box()
    set_color()
    draw.rectangle((0,0,32,32),fill=(0,0,0,0))
    draw_winmenu()
    draw_box(x)
    draw_arrow(play_color)
    draw_exit(exit_color)
    draw_save(save_color)

    matrix.SetImage(image, 0, 0)
    clock.tick(10)