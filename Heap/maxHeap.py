class MaxHeap:

    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        parentIdx = (len(array) - 2) // 2
        for currentIdx in range(parentIdx):
            self.siftDown(currentIdx, len(array)-1, array)
        return array

    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx-1)//2
        while currentIdx > 0 and heap[currentIdx] > heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx-1)//2
  
    def siftDown(self, currentIdx, endIdx, heap):
        leftChild = 2 * currentIdx + 1
        while leftChild <= endIdx:

            if (2 * currentIdx + 2) <= endIdx:
                rightChild = 2 * currentIdx + 2
            else:
                rightChild = -1

            if heap[leftChild] < heap[rightChild] and rightChild != -1:
                idxToSwap = rightChild
            else:
                idxToSwap = leftChild

            if heap[idxToSwap] > heap[currentIdx]:
                self.swap(idxToSwap, currentIdx, heap)
                currentIdx = idxToSwap
                leftChild = 2 * idxToSwap + 1
            else:
                break

    def insert(self, element):
        self.heap.append(element)
        self.siftUp(len(self.heap)-1, self.heap)

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        removedElement = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return removedElement

    def peek(self):
        return self.heap[0]

    def swap(self, i, j, heap):
        temp = heap[i]
        heap[i] = heap[j]
        heap[j] = temp
  
array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
obj = MaxHeap(array)
obj.buildHeap(array)
print(obj.heap)
obj.insert(400)
print(obj.heap)
print(obj.peek())
print(obj.remove())
print(obj.heap)