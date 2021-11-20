# Students to implement this
# How we build on top of data structures to create
# different advanced data structure

# (1b)
class Stack:
  def __init__(self):
    self.list = []

  # (1b)
  def push(self, disc):
    if disc != None:
      self.list.append(disc)

  # (1b)
  def pop(self):
    if self.list:
      return self.list.pop(-1)

  # (1b)
  def peek(self):
    if self.list:
      return self.list[-1]

  # (1b)
  def is_empty(self):
    return len(self.list) == 0
