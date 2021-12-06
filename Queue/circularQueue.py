class CircularQueue:
  #front = rear = -1

  #queue = []
    

  def __init__(self, size):
    self.items = [None] * size
    self.front = self.rear = -1
    self.size = size
    

  def isEmpty(self): 
    return self.front == -1 and self.rear == -1
  
  def isFull(self):

    return ((self.rear+1) % self.size ) == self.front 

  def enQueue(self, item):

    if self.isFull():
        print("Queue Overflow")
        return

    if self.isEmpty():
        self.front = self.rear = 0
    else:
        self.rear = (self.rear+1) % self.size 

    self.items.insert(self.rear, item)      


  def deQueue(self):

    if self.isEmpty():
        print("UnderFlow")
        return

    pop_element = self.items[self.front]
    self.items[self.front] = None

    if self.front == self.rear:
        self.front = self.rear = -1
    else:
        self.front = (self.front+1) % self.size
    return pop_element

  def Size(self):
    return self.size
 

c = CircularQueue(2)

print(c.isEmpty())
c.enQueue('2')
print(c.items, c.front, c.rear)
c.enQueue('3')
print(c.items, c.front, c.rear)
c.enQueue('True')
print(c.items, c.front, c.rear)
print("Size = " + str(c.Size()))
print(c.deQueue())
print(c.deQueue())
print(c.deQueue())
print(c.items)
print(c.isEmpty())