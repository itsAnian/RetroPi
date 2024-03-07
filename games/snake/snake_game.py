import pygame
import random
import copy
from PIL import Image
from PIL import ImageDraw
import time
from samplebase import SampleBase

running = True
SCALE = 1
pygame.init()

screen_width = 32 * SCALE
screen_height = 32 * SCALE
# screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

SPEED = 2
tail = []
clist = []

global score
score = 0

global snake_dir
snake_dir = (0, 1)

global apple
apple = 0


def spawn_snake():
    for i in range(1, 10):
        x = pygame.Rect(i * SPEED, SPEED, 1 * SCALE, 1 * SCALE)
        tail.append(x)
        clist.append(x)


def spawn_apple():
    # while not on element from tail
    x = random.randrange(0, 30, 2)
    y = random.randrange(0, 30, 2)
    return pygame.Rect(x * SCALE, y * SCALE, SCALE, SCALE)


def move_snake():
    global snake_dir
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake_dir != (0, 1):
        snake_dir = (0, -1)
    elif keys[pygame.K_a] and snake_dir != (1, 0):
        snake_dir = (-1, 0)
    elif keys[pygame.K_s] and snake_dir != (0, -1):
        snake_dir = (0, 1)
    elif keys[pygame.K_d] and snake_dir != (-1, 0):
        snake_dir = (1, 0)
    for i in range(0, len(tail) - 1):
        tail[i + 1] = copy.deepcopy(clist[i])

    tail[0].move_ip(SPEED * snake_dir[0], SPEED * snake_dir[1])
    for i, e in enumerate(tail):
        clist[i] = copy.deepcopy(e)


def check_events():
    global snake_dir, apple, score
    # collision with border directions are relative
    next_position_ahead = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])
    next_position_left = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])
    next_position_right = tail[0].move(SPEED * snake_dir[0], SPEED * snake_dir[1])

    # split into method for other checks, such as left and right relative from the snake for self collision
    if collision_self(next_position_ahead):
        print("dead self")
    if collision_self(next_position_left):
        print("dead left")
    if collision_self(next_position_right):
        print("dead right")

    # collision ahead
    if (next_position_ahead.left < 0) or (next_position_ahead.left > screen_width) or (next_position_ahead.top < 0) or (
            next_position_ahead.top > screen_height):
        print("dead border")
    # collision above
    # collsion below

    # snake on apple
    if tail[0].left == apple.left and tail[0].top == apple.top:
        apple = spawn_apple()
        score = score + 1
        tail.append(tail[len(tail) - 1].move(-SPEED * snake_dir[0], -SPEED * snake_dir[1]))
        clist.append(tail[len(tail) - 1].move(-SPEED * snake_dir[0], -SPEED * snake_dir[1]))
        print("len tail: ", len(tail))
        print(score)


def collision_self(next_relative_position: pygame.Rect) -> bool:
    for snake_element in tail:
        if snake_element.left == next_relative_position.left and snake_element.top == next_relative_position.top:
            return True
    return False


spawn_snake()
apple = spawn_apple()

image = Image.new("RGB", (32, 32))
draw = ImageDraw.Draw(image)
buffer = SampleBase.matrix.CreateFrameCanvas()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("black")
    move_snake()
    check_events()
    head = tail[0]
    for i, e in enumerate(tail):
        if i == 0:
            draw.rectangle((e.left, e.top, e.right, e.bottom), fill=(255, 255, 0))
            continue
        draw.rectangle((e.left, e.top, e.right, e.bottom), fill=(255, 0, 0))
    draw.rectangle((apple.left, apple.top, apple.right, apple.bottom), fill=(0, 255, 0))
    print(head.left, head.top)
    draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))
    buffer.SetImage(image)
    # pygame.draw.rect(screen, "red", head)
    # pygame.draw.rect(screen, "white", apple)
    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(5) / 1000

pygame.quit()
