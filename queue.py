class Queue:

  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def Enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)


q = Queue()

print(q.isEmpty())
q.Enqueue('2')
q.Enqueue('3')
q.Enqueue('True')
print(q.items)
print("Size = " + str(q.size()))
q.dequeue()
q.dequeue()
print(q.items)
print(q.isEmpty())