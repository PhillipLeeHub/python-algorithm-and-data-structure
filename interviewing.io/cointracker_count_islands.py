# 
# '''
# Given a 2D array of 1s and 0s, count the number of "islands of 1s" (groups of connecting 1s)
# 
# For example, given:
# [
#  [1, 1, 0, 0, 0],
#  [0, 1, 0, 0, 1],
#  [1, 0, 0, 1, 1],
#  [0, 0, 0, 0, 0],
#  [1, 0, 1, 0, 1]
# ]
# 
# Output = 6
# '''
'''
Time: o(n)
'''
def count_island(island_map):
    island_count = 0
    i = 0
    while(i < len(island_map)):
        j = 0
        while( j < len(island_map[0])):
              if island_map[i][j] == 1:
                zero_out(island_map, i,j)
                island_count +=1
              j+=1
        i+=1
        print(island_map)
    return island_count
      
def zero_out(island_map, i, j):
    if i < 0 or i >= len(island_map):
          return
    if j < 0 or j >= len(island_map[0]):
          return
    if island_map[i][j] == 0:
        return 
    
    island_map[i][j] = 0    
  
    zero_out(island_map, i+1, j)
    zero_out(island_map, i-1, j)
    zero_out(island_map, i, j+1)
    zero_out(island_map, i, j-1)
     
              
island_map = [
 [1, 1, 0, 0, 0],
 [0, 1, 0, 0, 1],
 [1, 0, 0, 1, 1],
 [0, 0, 0, 0, 0],
 [1, 0, 1, 0, 1]
]           
print(count_island(island_map))  

              
              
