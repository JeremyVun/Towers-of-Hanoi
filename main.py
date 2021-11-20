from util import random_color, render
from random import randint
from config.config import config

# Part 1
from stack import Stack # (1a)
from disc import Disc # (1b)

# Part 2 EXTENSION - build game using stacks
# from tower import Tower # (2a)

def main():
  # (1c)
  stacks = build_stacks()
  render(stacks)

  # (2c)
  """
  towers = build_towers()
  render(towers)
  """

  # Event Loop
  while not is_game_over(stacks):
    # (1d)
    first = int(input("Move disc from stack [1, 2, 3]? ")) - 1
    second = int(input("Move disc to stack [1, 2, 3]? ")) - 1

    disc = stacks[first].pop()
    stacks[second].push(disc)
    render(stacks)

    # (2d)
    """
    towers[first].try_move_to(towers[second])
    render_towers(towers)
    """

  print("Game over!")

# Part 1 - use basic stack data structure
def build_stacks():
  stacks = []
  for i in range(3):
    stacks.append(Stack())

  stacks[1].push(Disc(100, random_color()))
  stacks[1].push(Disc(75, random_color()))
  stacks[2].push(Disc(50, random_color()))

  return stacks


# Check whether the game is over or not
def is_game_over(stacks):
  with_discs = sum(not s.is_empty() for s in stacks)
  return with_discs == 1


# Part 2 - build Tower Game Object from using Stack
"""
def build_towers():
  towers = []
  for i in range(3):
    towers.append(Tower())

  # Randomly add discs onto the towers
  disc_size = 100
  min_disc_size = config["min_disc_size"]

  while disc_size > min_disc_size:
    tower = towers[str(randint(1, 3))]
    new_disc = Disc(disc_size, random_color())
    tower.try_add_disc(new_disc)
    disc_size -= 15

  return towers
"""

if __name__ == "__main__":
  main()
