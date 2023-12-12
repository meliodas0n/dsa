#!/usr/bin/python3

import random

class Player:
  def __init__(self):
    self.hp = 100
    self.mp = 100

if __name__ == "__main__":
  player = Player()
  print(player.hp, player.mp)