import pygame

def display_o_menu(matrix, joystick_found, joystick, draw, image):
    global x
    initial_delay = 0.5
    dt = 0
    x = 0
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    GREEN = (0,255,0)
    RED = (255,0,0)
    PLAY_COLOR = WHITE
    EXIT_COLOR = WHITE
    BORDER_COLOR = WHITE

    RETURN = 8



    def draw_o(color):
        #draws o
        draw.ellipse((3,3,7,7), fill=(color))
        draw.rectangle((4,4,6,6), fill=(BLACK))

    def draw_winmenu(text_color):
        #draw w
        draw.rectangle((11,3,11,7), fill=(text_color))
        draw.point ((12,6), fill=(text_color))
        draw.point ((13,5), fill=(text_color))
        draw.point ((14,6), fill=(text_color))
        draw.rectangle((15,3,15,7), fill=(text_color))

        #draw i
        draw.rectangle((17,3,17,7), fill=(text_color))

        #draw n
        draw.rectangle((19,3,19,7), fill=(text_color))
        draw.rectangle((20,4,20,4), fill=(text_color))
        draw.rectangle((21,5,21,5), fill=(text_color))
        draw.rectangle((22,6,22,6), fill=(text_color))
        draw.rectangle((23,3,23,7), fill=(text_color))

        #draw s
        draw.rectangle((25,3,28,3), fill=(WHITE))
        draw.point((25,4), fill=(WHITE))
        draw.rectangle((25,5,28,5), fill=(WHITE))
        draw.point((28,6), fill=(WHITE))
        draw.rectangle((25,7,28,7), fill=(WHITE))

        #draws underline for Menu
        draw.rectangle((1,9,30,9),fill=(WHITE))
        draw.rectangle((1,7,1,9),fill=(WHITE))
        draw.rectangle((30,7,30,9),fill=(WHITE))


    def draw_box(x):
        #draws box for play arrow
        draw.rectangle((5+x,11,5+x,21),fill=(BORDER_COLOR))
        draw.rectangle((5+x,11,13+x,11),fill=(BORDER_COLOR))
        draw.rectangle((13+x,11,13+x,21),fill=(BORDER_COLOR))
        draw.rectangle((5+x,21,13+x,21),fill=(BORDER_COLOR))

    def draw_arrow(color):
        #draws arrow
        draw.rectangle((8,14,8,18),fill=(color))
        draw.rectangle((9,15,9,17),fill=(color))
        draw.rectangle((10,16,10,16),fill=(color))

    def draw_exit(color):
        #draws x
        draw.point((20,14),fill=(color))
        draw.point((21,15),fill=(color))
        draw.point((22,16),fill=(color))
        draw.point((23,17),fill=(color))
        draw.point((24,18),fill=(color))
        draw.point((20,18),fill=(color))
        draw.point((21,17),fill=(color))
        draw.point((22,16),fill=(color))
        draw.point((23,15),fill=(color))
        draw.point((24,14),fill=(color))

    def move_box():
        global play_color
        global exit_color
        global running
        global x
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x < 14:  #movment of the select box
            if x > 0:
                x = 0
                play_color = (GREEN)
                exit_color = (WHITE)
        if keys[pygame.K_RIGHT] and x < 12:
            if x < 13:
                x = 13
                exit_color = (RED)
                play_color = (WHITE)

        if keys[pygame.K_RETURN]: #if enter is pressed
            if x == 0:
                print("o_wins:PLAY")
                running = False
            if x == 13:
                print("o_wins:EXIT")
                running = False

    def move_box_joy(x_axis,change_running):
        threshold = 0.1
        global play_color
        global exit_color
        global running
        global x
        x_axis = 0 if abs(x_axis) < threshold else x_axis
        if x_axis > 0 and x == 13:
            x = 0
            print("o_wins:x = 0")
            play_color = (GREEN)
            exit_color = (WHITE)
        elif x_axis < 0 and x == 0:
            x = 13
            play_color = (WHITE)
            exit_color = (RED)
            print("o_wins:x = 13")

        if joystick.get_button(RETURN):
            if x == 0:
                print("o_wins:PLAY")
                running = False
                return "play_again"
            if x == 13:
                print("o_wins:EXIT")
                running = False
                return "exit"

        return "continue"


    clock = pygame.time.Clock() #is just a clock for how often the while loop is repeated
    pygame.init()
    running = True
    play_color = (GREEN)
    exit_color = (WHITE)
    change_running = "continue"
    while running:

        if not(joystick_found):
            move_box()
        else:
            if change_running == "continue" and initial_delay <0:
                x_axis = joystick.get_axis(0)
                change_running = move_box_joy(x_axis,change_running)
            elif change_running == "play_again":
                print("owin_play_again")
                return True
            elif change_running == "exit":
                return False
        
        draw.rectangle((0,0,32,32),fill=(0,0,0,0))
        draw_o(WHITE)
        draw_winmenu(WHITE)
        draw_box(x)
        draw_arrow(play_color)
        draw_exit(exit_color)

        initial_delay = initial_delay-dt
        matrix.SetImage(image, 0, 0)
        dt = clock.tick(60)/1000