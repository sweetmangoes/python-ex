def quicksort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print (quicksort([1])) # 1
print (quicksort([1,5])) # [1,5]
print (quicksort([2,6,4])) # [2,4,6]
print (quicksort([10,5,2,3])) # [3,2,5,10]