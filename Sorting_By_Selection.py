# first, this function finds the smallest element in array and returns its index
def findSmallest(arr):
  smaller = arr[0]
  smallest_index = 0
  for element in range(1, len(arr)):
    if arr[element] < smaller:
      smaller = arr[element]
      smallest_index = element
  return smallest_index

# then, this function will sort a new array s by selection
def sortingBySelection(arr):
  newArr = []
  for element in range(len(arr)):
    smaller = findSmallest(arr)
    newArr.append(arr.pop(smaller))
  return newArr

# example of using
sortingBySelection([5,3,6,2,10])
