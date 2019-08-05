'''
Array Index & Element Equality
Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[output] integer
'''
def index_equals_value_search(arr):
  # [-8,1,2,5,6,8]
  #   0 1 2 3 4 5
  
  # [-8,0,1,2,4,8]
  #   0 1 2 3 4 5
  left = 0 
  right = len(arr)-1
  min_index = float('inf')
  while(left <= right):
    #mid = left + ((right - left)/2)
    mid = (left + right) / 2
    
    if (arr[mid] == mid):
      min_index = min(mid,min_index)
      right = mid-1
    elif arr[mid] > mid:
      right = mid - 1
    elif arr[mid] < mid:
      left = mid + 1
  if min_index != float('inf'):
    return min_index
  return -1
arr = [0,0,2,5,6,8]

print(index_equals_value_search(arr))
