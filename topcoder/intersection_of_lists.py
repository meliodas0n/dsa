import sys

class Node:
  def __init__(self, data):
    self.data = data 
    self.next = None

class LinkedList:
  def __init__(self, datalist):
    self.datalist = datalist
    self.head = None
    for i in datalist:
      if not self.head:
        self.head = Node(i) 
        print(self.head)
        # self.traverse_list()
      else:
        self.head = self.head.next
        print(self.head)
        self.head.next = Node(i)
  
  def traverse_list(self):
    while self.head is not None:
      print(self.head.data, end="\n")
      self.head = self.head.next


def main():
  elements = [1, 2, 3, 4, 5]
  LinkedList(elements).traverse_list()

if __name__ == "__main__":
  main()


"""
I don't understand 
how is it not working ?
# head = Node(1)
# head.
"""