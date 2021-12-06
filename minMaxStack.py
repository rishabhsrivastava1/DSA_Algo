class MinMaxStack:
	
	def __init__(self):
		self.items = []
    
	def isEmpty():
		return self.items == []
	
	def peek(self):
		return self.items[len(self.items)-1]

    def pop(self):
		return self.items.pop()

    def push(self, number):
		self.items.append(number)

    def getMin(self):
		min = self.items[0]
		for i in range(len(self.items)):
			if self.items[i] < min:
				min = self.items[i]
				
		return min

    def getMax(self):
		max = self.items[0]
		for i in range(len(self.items)):
			if self.items[i] > max:
				max = self.items[i]
				
		return max
