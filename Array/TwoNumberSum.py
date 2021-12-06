def twoNumberSum(array, targetSum):
    # Write your code here.

    length = len(array)
    for i in range(0, length):
        for j in range(i + 1, length):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []
