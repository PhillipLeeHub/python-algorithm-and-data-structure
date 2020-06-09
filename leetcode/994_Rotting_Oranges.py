'''
994. Rotting Oranges Medium
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''
def orangesRotting(self, grid: List[List[int]]) -> int:
	days = 0
	while(True):
		if self.elapseMinute(grid) == 0:
			# Check if fresh oranges remain (edge case)
			# Impossible to infect all fresh oranges
			if self.isFreshOranges(grid):
				return -1

			# No more infections, exit loop
			break;

		else: 
			# Infection present, add to day count 
			days+=1

	# Return days
	return days

# returns number of oranges infected this minute
def elapseMinute(self, grid):
	# Tracks already seen rotten oranges
	seen_oranges = {}

	# Initialize infected orange count to 0
	infected_min_count = 0

	# Loop through entire grid
	for i in range(len(grid)):
		for j in range(len(grid[0])):

			# Check for rotten orange cell AND
			# If we have not infected this orange this same minute
			if grid[i][j] == 2 and (i, j) not in seen_oranges:
				# Rotten orange, infect adj oranges
				infected_min_count+=self.infect_adj(grid, i, j, seen_oranges)

	# return the number of infected oranges for this minute
	return infected_min_count

# Infect adjacent cells
# Returns number of oranges infected
def infect_adj(self, grid, i, j, seen_oranges):      
	infected_adj_count = 0
	# Infect the orange
	grid[i][j] = 2

	_i = i + 1
	_j = j
	infected_adj_count+=self.infect_orange(_i, _j, grid, seen_oranges)

	_i = i - 1
	_j = j
	infected_adj_count+=self.infect_orange(_i, _j, grid, seen_oranges)

	_i = i
	_j = j + 1
	infected_adj_count+=self.infect_orange(_i, _j, grid, seen_oranges)

	_i = i
	_j = j - 1
	infected_adj_count+=self.infect_orange(_i, _j, grid, seen_oranges)
	return infected_adj_count

# Returns 1 if infected, else 0
def infect_orange(self, _i, _j, grid, seen_oranges):
	# Check range
	if (0 <= _i < len(grid)) and (0 <= _j < len(grid[0])):
		# Check for fresh orange
		if grid[_i][_j] == 1:
			# Infect into rotten orange
			grid[_i][_j] = 2

			# Note this rotten orange has been seen
			seen_oranges[(_i,_j)] = 1
			return 1

	return 0

# Returns true if grid has fresh at least 1 fresh orange
def isFreshOranges(self, grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 1:
				return True
	return False
