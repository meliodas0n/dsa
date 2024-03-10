class Vector:
  def __init__(self, d):
    self.__coords = [0] * d

  def __len__(self):
    return len(self.__coords)
