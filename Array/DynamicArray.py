import ctypes

class DynamicArray(object):

  def __init__(self):
    
    self.n = 0
    self.capacity = 1
    self.array = self.make_array(self.capacity)

  def __len__(self):
    return self.n

  def __getitem__(self, k):

    if not 0 <= k < self.n:
      return IndexError('k Out of Bounds!!')
    
    return self.array[k]

  def append(self, element):

    if self.n == self.capacity:
      return self._resize(self.capacity * 2)
    
    self.array[self.n] = element
    self.n += 1

  def _resize(self, new_capacity):
    
    B = self.make_array(new_capacity)

    for i in range(self.n):
      B[i] = self.array[i]
    
    self.array = B
    self.capacity = new_capacity

  def make_array(self, new_cap):
    
    return (new_cap * ctypes.py_object)()


arr = DynamicArray()

print(len(arr))
arr.append(1)
print(arr[0])
print(len(arr))
arr.append(2)
print(arr[1])
print(arr.capacity)
