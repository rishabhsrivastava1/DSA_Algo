class DeQueue:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addFront(self, item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0,item)

  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)

  def size(self):
    return len(self.items)


q = DeQueue()

print(q.isEmpty())
q.addFront('2')
q.addRear('3')
q.addRear('True')
print(q.items)
print("Size = " + str(q.size()))
q.removeFront()
q.removeRear()
print(q.items)
print(q.isEmpty())