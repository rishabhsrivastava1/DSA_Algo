def isValidSubsequence(array, sequence):
    # Write your code here.
	array_index = []
    for i in range(0,len(sequence)):
		element = sequence[i]
		for j in range(i,len(array)):
			if array[j]==element and len(array_index)<=len(sequence)-1:
				array_index.append(j)
	
	if array_index == sorted(array_index) and len(sequence)==len(array_index):
		return True
	else:
		return False
	'''
	if array_index == sorted(array_index):
		return array_index
	'''

	