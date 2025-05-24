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
      else:
        current = self.head
        while current.next:
          current = current.next
        current.next = Node(i)
  
  def traverse_list(self):
    while self.head is not None:
      print(self.head.data, end=" ")
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