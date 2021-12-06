class CircularQueue:
  #front = rear = -1

  #queue = []

  def __init__(self):
    self.items = []
    self.front = self.rear = -1

  def isEmpty(self):
    return self.items == []

  def addRear(self, item):
    
      if (self.front==0 and self.rear==len(self.items)-1) and (self.front == self.rear+1):
          print("Queue Overflow")
      
      else:

          if self.rear == -1:
              self.front = self.rear = 0
          elif self.rear == len(self.items)-1:
              self.rear = 0
          else:
              self.rear += 1
          self.items.insert(self.rear,item)
          

      #self.items.insert(0,item)

  def removeFront(self):

        if self.front ==-1:
            print("Queue Underflow")
    
        else:

            if self.front == self.rear:
                self.front = self.rear = -1
            elif self.front == len(self.items)-1:
                self.front = 0
            else:
                self.front += 1
            return self.items.pop(self.front)
                

  def size(self):
    return len(self.items)
 


c = CircularQueue()

print(c.isEmpty())
c.addRear('2')
c.addRear('3')
c.addRear('True')
print(c.items)
print("Size = " + str(c.size()))
c.removeFront()
c.removeFront()
c.removeFront()
print(c.items)
print(c.isEmpty())