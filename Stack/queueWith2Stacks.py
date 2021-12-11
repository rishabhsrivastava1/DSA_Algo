class Que:

  def __init__(self):
      self.instack = []
      self.outstack = []

  def enqueue(self, element):

      self.instack.append(element)

  def dequeue(self):

        if len(self.outstack) == 0:
            while len(self.instack) > 0:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()


queue = Que()

queue.enqueue('1')
queue.enqueue('2')
queue.enqueue('3')
print("Instack")
print(queue.instack)
print("Outstack")
print(queue.outstack)
queue.dequeue()
print("Instack")
print(queue.instack)
print("Outstack")
print(queue.outstack)
queue.dequeue()
print("Instack")
print(queue.instack)
print("Outstack")
print(queue.outstack)
