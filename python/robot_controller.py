#!/usr/bin/python3

import random

class Player:
  def __init__(self):
    self.hp = 100
    self.mp = 100
    self.level = 0

class Level():
  def __init__(self):
    self.level = random.randint(1, 1000000)

class Game:
  def __init__(self, player, game):
    self.player = player
    self.game = game

  def possible(self):
    return True if (self.player.hp != 0 or self.player.mp != 0) else False

class Move:
  # this will generate a random move (tbd)
  pass

def check_win_or_loose():
  pass

if __name__ == "__main__":
  player = Player()
  highest_level = Level()
  game = Game(player, highest_level)
  print(game.player.hp, game.player.mp, game.game.level)
  curr_level = 0
  while game.possible():
    continution = True
    if (player.hp == 0 or player.mp == 0) and curr_level <= game.level:
      print("Ahhh! You LOST!!")
      continution = False
      exit(0)
    elif (player.hp == 0 or player.mp == 0) and curr_level >= game.level:
      continution = False
      print("Yay! You WON!!")
      exit(0)
    elif curr_level >= game.level:
      print("Yay! You WON!!")
      continution = False
      exit(0)
    print(game.current_stats())
    print(Move().required_stats())
    is_making_move = input("Are you going to make a move ?(y/n)")
    if is_making_move == 'y':
      # subtract the main stats with required stats and then multiple the final stats by random number
      pass
    else:
      if check_win_or_loose():
        print("Yay! You WON!!")
        continution = False
        exit(0)
      else:
        print("Ahhh! You LOST!!")
        continution = False
        exit(0) 