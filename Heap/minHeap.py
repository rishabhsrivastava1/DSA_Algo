class MinHeap:
    
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Write your code here.
        parentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(parentIdx + 1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
        leftChildIdx = 2 * currentIdx + 1
        while leftChildIdx <= endIdx:
            
            if (currentIdx * 2 + 2)  <= endIdx:
                rightChildIdx = currentIdx * 2 + 2
            else:
                rightChildIdx = -1
            
            if rightChildIdx != -1 and heap[rightChildIdx] < heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                leftChildIdx = currentIdx * 2 + 1
            else:
                break
    
    def siftUp(self, currentIdx, heap):
        # Write your code here.
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):        
		
        return self.heap[0]
	
    def remove(self):
        # Write your code here.
        self.swap(0, len(self.heap)-1, self.heap)
        removedElement = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return removedElement

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)
	
    def swap(self, i, j, heap):
				
        heap[i], heap[j] = heap[j], heap[i]
