# Base functions for rendering objects to screen
# Aim of the lesson is to teach stacks, not pygame

import pygame
from pygame import draw, Rect
from random import randint
from config.config import config

from stack import Stack


# Unpack the configs we need
width = config["window_width"]
height = config["window_height"]
tower_width = int(width / 3)
disc_height = config["disc_height"]

# Initialise pygame for rendering
pygame.init()
screen = pygame.display.set_mode((width, height))


# PUBLIC HELPER FUNCTIONS #
def random_color():
  return (randint(100, 255), randint(100, 255), randint(100, 255))

def render(objects):
  if len(objects) == 0:
    return

  screen.fill('black')

  if type(objects[0]) is Stack:
    __render_stacks(objects)
  else:
    __render_towers(objects)

  pygame.display.flip()


# PRIVATE #
def __render_towers(towers):
  for i in range(len(towers)):
    __render_stack(i, towers[i].stack)

def __render_stacks(stacks):
  for i in range(len(stacks)):
    __render_stack(i, stacks[i])

def __render_stack(x, stack):
  for i in range(len(stack.list)):
    disc = stack.list[i]

    disc_width = 100 * disc.size/100
    pos = __get_centered_pos(x, i, disc_width)
    __render_disc(pos, disc_width, disc.color)

def __render_disc(pos, disc_width, color):
  rect = Rect(pos, (disc_width, disc_height))
  draw.rect(screen, color, rect, 0)

def __get_centered_pos(x, y, disc_width):
  padding = (100 - disc_width) / 2
  x *= tower_width
  return (x + padding, height - ((int(y)+1) * disc_height))
