'''
Pancake Sort
Given an array of integers arr:

Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.
Example:

input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it’s called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:

[time limit] 5000ms

[input] array.integer arr

[input] integer k

0 ≤ k
[output] array.integer
'''
def flip(arr, k):
  L = 0
  R = k-1
  while(L <= R):
    arr[L],arr[R] = arr[R],arr[L]
    L+=1
    R-=1
  return arr

def findMaxIndex(arr, k):
  max_num = arr[0]
  max_index = 0
  for k in range(k):
    if arr[k] > max_num:
      max_num = arr[k]
      max_index = k
  return max_index
  
def pancake_sort(arr):
  for index, num in enumerate(arr):
    max_index = findMaxIndex(arr,len(arr) - index)
    #print(arr, index)
    arr = flip(arr, max_index + 1)
    #print(arr)
    arr = flip(arr, len(arr) - index)
  return arr
    
arr = [2, 5, 4, 3, 1]
print(pancake_sort(arr))
