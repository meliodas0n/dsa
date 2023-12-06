class Node:
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    node = Node(data, self.head)
    self.head = node

  def print(self):
    if self.head is None:
      print('Linked List is Empty!')
      return
    llstr = ''
    while self.head:
      llstr += str(self.head.data) + '-->'
      self.head = self.head.next
    print(llstr)

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(90)
    ll.insert_at_beginning(100)
    ll.insert_at_beginning(1)
    ll.insert_at_end(1)
    ll.insert_at_end(5)
    ll.insert_at_end(10)
    ll.print()
