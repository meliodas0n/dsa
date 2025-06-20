class UnionFind:
  def __init__(self, n):
    self.up_bound = list(range(n))
    self.rank = [0] * n
  
  def find(self, x_index):
    if self.up_bound[x_index] == x_index:
      return x_index
    self.up_bound[x_index] = self.find(self.up_bound[x_index])
    return self.up_bound[x_index]
  
  def union(self, x_index, y_index):
    repr_x = self.find(x_index)
    repr_y = self.find(y_index)
    if repr_x == repr_y:
      return False
    if self.rank[repr_x] == self.rank[repr_y]:
      self.rank[repr_x] += 1
      self.up_bound[repr_y] += 1
    elif self.rank[repr_x] > self.rank[repr_y]:
      self.up_bound[repr_y] = repr_x
    else:
      self.up_bound[repr_x] = repr_y
    return True