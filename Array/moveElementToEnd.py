def moveElementToEnd(array, toMove):
    # Write your code here.
	counter = 0
    for i in range(0,len(array)):
		if array[i]!=toMove:
			temp = array[counter]
			array[counter] = array[i]
			array[i] = temp
			counter += 1
	
	return array