class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None

class LinkedList:
  def __init__(self, datalist):
    self.datalist = datalist
    self.head = Node(datalist[0])
    for i in datalist[1:]:
      self.head.next = Node(i)
  
  def traverse_list(self):
    while self.head is not None:
      print(self.head.data, end=" ")


def main():
  elements = [1, 2, 3, 4, 5]
  LinkedList(elements).traverse_list()

if __name__ == "__main__":
  main()