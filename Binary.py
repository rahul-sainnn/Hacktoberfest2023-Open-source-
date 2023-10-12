def binarySearch (array, target):
  NOT_FOUND = -1
  left = 0 # left boundary of search space
  right = len(array) - 1 # right boundary of search space

  while left <= right:
    # middle - index used in determining whether 
    # to search left or right.
    middle = int(left + (right - left)/2) # prevents integer overflow
    if target == array[middle]:
      return middle
    elif target < array[middle]: 
      right = middle - 1
    else:
      left = middle + 1
  return NOT_FOUND

# array - collection to be searched. 
array = [2, 4, 5, 6, 7, 8, 23, 34, 54, 56] 
# target - value to be searched. 
target = 8
result = binarySearch(array, target)
print(result) # returns 5, the index of the target in the array.

target = 9 # now searchig for 9
result = binarySearch(array, target) # returns -1
print(result)
