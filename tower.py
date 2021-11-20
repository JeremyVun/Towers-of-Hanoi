from stack import Stack

# Part 2
# Using stacks to build Game Objects
class Tower:
  def __init__(self):
    self.stack = Stack()

  def is_empty(self):
    return self.stack.is_empty()

  # Try to add a disc to this tower
  def try_add_disc(self, disc):
    if self.stack.is_empty():
      self.stack.push(disc)
      return True

    top_disc = self.stack.peek()
    if top_disc.size <= disc.size:
      print(f"Cannot place disc of size {disc.size} ontop of disc of size {top_disc.size}")
      return False
    else:
      self.stack.push(disc)
      return True


  # try move a disc from one tower to another
  def try_move_to(self, other):
    if self.stack.is_empty():
      print(f"Tower has no discs to move!")
    else:
      disc = self.pop()
      if not other.try_add_disc(disc):
        self.push(disc)
