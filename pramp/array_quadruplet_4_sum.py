'''
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer s

[output] array.integer
'''
def find_array_quadruplet(arr, s):
  '''
  input:  [2, 7, 4, 0, 9, 5, 1, 3]
  sorted: [0, 1, 2, 3, 4, 5, 7, 9]
           p1
              p2
                 p3
                                p4
  Move (ping pong) p3 and p4 until s is found.
  '''
  arr.sort()
  p1 = 0 
  p2 = p1+1 
  p3 = p2+1
  p4 = len(arr)-1
  
  
  while(p1 <= len(arr)-4):
    p2 = p1+1
    while(p2 <= len(arr)-3):
      p3 = p2+1
      p4 = len(arr)-1
      while(p3 < p4):
        running_sum = arr[p1] + arr[p2] + arr[p3] + arr[p4]
        
        if running_sum == s:
          return [arr[p1], arr[p2], arr[p3], arr[p4]]
        elif running_sum < s:
          p3+=1
        else:
          p4-=1
      p2+=1
    p1+=1
  return []
