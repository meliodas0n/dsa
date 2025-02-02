'''
You are given a grid of letters and your task is to find words in the grid. A word can be read horizontally, vertically or diagonally in either direction.
In a file wordgrid.py, implement the class WordFinder with the following methods:

set_grid: sets the contents of the grid as a list, where each element is a string representing a row of the grid
count: counts the number of occurrences of the given word

If a word can be read both forwards and backwards using the same letters, that should count as one occurrence only.
Your class will be tested using many different grids. The height and width of each test grid is at most 20 letters. Each letter is in the range A - Z.
'''

class WordFinder:
  def set_grid(self, grid):
    self._original = grid
    self._grid = [[j for j in i] for i in grid]

  def count(self, word):
    n = len(word)
    # horizontal
    c = 0
    horizontal_string = "".join(self._original)
    for i in range(0, len(horizontal_string) - n):
      if word == horizontal_string[i:i+n]:
        c += 1
        
    # vertical
    verts = {k: "" for k in range(len(self._grid[0]))}
    for i in range(len(self._grid[0])):
      for j in range(len(self._grid)):
        verts[i] = "".join(verts[i] + self._grid[j][i])
    for i in verts.values():
      if i == word:
        c += 1
    
    # diagonal
    diagonal_string = {k: "" for k in range(2)}
    if len(self._grid[0]) == len(self._grid):
      for i in range(len(self._grid)):
        diagonal_string[0] = "".join(diagonal_string[0] + self._grid[i][i])
        diagonal_string[1] = "".join(diagonal_string[1] + self._grid[i][len(self._grid[0]) - 1 - i])
    for diag in diagonal_string.values():
      for i in range(0, len(diag) - n):
        if word == horizontal_string[i:i+n]:
          c += 1
    return c

if __name__ == "__main__":
  grid = ["TIRATIRA",
          "IRATIRAT",
          "RATIRATI",
          "ATIRATIR"]

  finder = WordFinder()
  finder.set_grid(grid)

  print(finder.count("TIRA")) # 7 
  print(finder.count("TA")) # 13
  print(finder.count("RITARI")) # 3
  print(finder.count("A")) # 8
  print(finder.count("AA")) # 6
  print(finder.count("RAITA")) # 0     