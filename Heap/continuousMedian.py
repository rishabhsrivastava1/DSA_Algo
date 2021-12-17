
class ContinuousMedianHandler:
    def __init__(self):
        self.lowerHalf = Heap(Max_Heap_Func, [])
        self.greaterHalf = Heap(Min_Heap_Func, [])
        self.median = None

    def insert(self, newElement):
        
        if not self.lowerHalf.length or newElement < self.lowerHalf.peek():
            self.lowerHalf.insert(newElement)
        else:
            self.greaterHalf.insert(newElement)

        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):

        if self.lowerHalf.length - self.greaterHalf.length == 2:
            self.greaterHalf.insert(self.lowerHalf.remove())
        elif self.greaterHalf.length - self.lowerHalf.length == 2:
            self.lowerHalf.insert(self.greaterHalf.remove())

    def updateMedian(self):

        if self.lowerHalf.length == self.greaterHalf.length:
            self.median = (self.lowerHalf.peek() + self.greaterHalf.peek()) / 2
        elif self.lowerHalf.length > self.greaterHalf.length:
            self.median = self.lowerHalf.peek()
        else:
            self.median = self.greaterHalf.peek()        

    def getMedian(self):

        return self.median


class Heap:

    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        
        parentIdx = (len(array)-2) // 2
        for currentIdx in reversed(range(parentIdx)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    def insert(self, element):
        
        self.heap.append(element)
        self.length += 1 
        self.siftUp(self.length - 1, self.heap)

    def remove(self):

        self.swap(0, self.length - 1, self.heap)
        removedElement = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        
        return removedElement

    def peek(self):
        
        return self.heap[0]

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0:
            if self.comparisonFunc(heap[currentIdx], heap[parentIdx]):
                self.swap(currentIdx, parentIdx, heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1) // 2
            else:
                return

    def siftDown(self, currentIdx, endIdx, heap):
        leftChildIdx = 2 * currentIdx + 1
        while leftChildIdx <= endIdx:

            if (2 * currentIdx + 2) <= endIdx:
                rightChildIdx = 2 * currentIdx + 2
            else:
                rightChildIdx = -1
            
            if rightChildIdx!=-1 and self.comparisonFunc(heap[rightChildIdx], heap[leftChildIdx]):
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx

            if self.comparisonFunc(heap[idxToSwap], heap[currentIdx]):
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                leftChildIdx = 2 * idxToSwap + 1
            else:
                return

    def swap(self, i, j, heap):

        heap[i], heap[j] = heap[j], heap[i]

def Max_Heap_Func(a, b):
    
    return a > b

def Min_Heap_Func(a, b):

    return a < b 
