class Vector:
  def __init__(self, d):
    self.__coords = [0] * d

  def __len__(self):
    return len(self.__coords)

  def __getitem__(self, j):
    return self.__cords[j]

  def __setitem__(self, j, val):
    self.__coords[j] = val

  def __add__(self, other):
    if len(self) != len(other):
      raise ValueError("Dimensions must agree")
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result
  
  def __eq__(self, other):
    return self.__coord == other.__coords

  def __ne__(self, other):
    return not self == other

  def __str__(self):
    return '<' + str(self.__coords)[1 : -1] + '>'
