class CircularQueue:
  #front = rear = -1

  #queue = []

  def __init__(self):
    self.items = []
    self.front = self.rear = -1

  def isEmpty(self):
    return len(self.items) == 0

  def addRear(self, item):
    
      if (self.front==0 and self.rear==len(self.items)-1) or (self.front == self.rear+1):
          print("Queue Overflow")
      
      else:

          if self.rear == -1 and (self.rear == len(self.items)-1):
              self.rear = 0
    
          else:
              self.rear = self.rear+1
          self.items.insert(self.rear,item)
          

      #self.items.insert(0,item)

  def removeFront(self):

        if self.front == -1 and self.rear == -1:
            print("Queue Underflow")
    
        else:
            self.front = (self.front+1) % len(self.items)
            return self.items.pop(self.front)
                

  def size(self):
    return len(self.items)
 
