def longestPeak(array):
    
	length = 0
	
	
	for i in range(1, len(array)-1):
		if array[i+1] < array[i] and array[i] > array[i-1]:
			temp_start = 0
			temp_end = 0
			
			for j in range(i, len(array)-1):
				if array[j+1] < array[j]:
					temp_end = j + 1
				else:
					break
					
			for k in range(i, 0, -1):
				if array[k-1] < array[k]:
					temp_start = k - 1
				else:
					break
					
			temp_length = temp_end - temp_start + 1
			
			if temp_length > length:
				length = temp_length
				
			i = temp_end - 1
			
	return length
			
		
print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))