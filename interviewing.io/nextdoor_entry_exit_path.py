# Nextdoor
# Your previous Plain Text content is preserved below:
#
# We'll consider the maze to be a 2D integer array. Meaning of numerical values in the array will be as per the following convention:
# 0 -> Wall
# 1 -> Road
# 2 -> Maze entry
# 3 -> Maze exit
#     j - 1
#   [[2, 0, 0, 0],
# i [1, 1, 0, 1],
#   [0, 1, 0, 0],
#   [1, 1, 1, 3]]
#
# Return a list of the coordinates of the path from beginning to end
#
def traverse_maze(maze):
    list_results = []
    entry_found = False
    entry_location = None

    if not maze:
        return []
    if not maze[0]:
        return []

    # search for entry
    for i, arr in enumerate(maze):
        for j, num in enumerate(arr):
            if num == 2:
                entry_found = True
                entry_location = (i, j)
                maze[i][j] = 0
                list_results.append([i, j])

    if not entry_found:
        return []

    # traverse using BFS
    import queue
    q = queue.Queue()
    q.put(entry_location)

    while (not q.empty()):
        i, j = q.get()
        # look left
        if (j - 1) >= 0:
            if maze[i][j - 1] == 3:
                list_results.append([i, j - 1])
                return list_results

            if maze[i][j - 1] == 1:
                maze[i][j - 1] = 0
                list_results.append([i, j - 1])
                q.put((i, j - 1))

        # look right
        if (j + 1) <= len(maze[0]) - 1:
            if maze[i][j + 1] == 3:
                list_results.append([i, j + 1])
                return list_results

            if maze[i][j + 1] == 1:
                maze[i][j + 1] = 0
                list_results.append([i, j + 1])
                q.put((i, j + 1))

        # look top
        if (i - 1) >= 0:
            if maze[i - 1][j] == 3:
                list_results.append([i - 1, j])
                return list_results

            if maze[i - 1][j] == 1:
                maze[i - 1][j] = 0
                list_results.append([i - 1, j])
                q.put((i - 1, j))

        # look bottom
        if (i + 1) <= len(maze) - 1:
            if maze[i + 1][j] == 3:
                list_results.append([i + 1, j])
                return list_results

            if maze[i + 1][j] == 1:
                maze[i + 1][j] = 0
                list_results.append([i + 1, j])
                q.put((i + 1, j))

    return []


# Working maze
maze_list_1 = [[2, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 3]]
print(traverse_maze(maze_list_1))

#   [[2, 0, 0, 0],
#   [1, 1, 0, 1],
#   [0, 1, 0, 0],
#   [1, 1, 1, 1]]
# No exit
maze_list_2 = [[2, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]
print(traverse_maze(maze_list_2))

#   [[1, 0, 0, 0],
#   [1, 1, 0, 1],
#   [0, 1, 0, 0],
#   [1, 1, 1, 3]]
# No entry
maze_list_3 = [[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 3]]
print(traverse_maze(maze_list_3))

#   [[2, 0, 0, 0],
#   [1, 1, 0, 1],
#   [0, 0, 0, 0],
#   [1, 1, 1, 3]]
# No connecting path
maze_list_4 = [[2, 0, 0, 0], [1, 1, 0, 1], [0, 0, 0, 0], [1, 1, 1, 3]]
print(traverse_maze(maze_list_4))

# 2x3 maze
#   [ [2, 1, 0],
#     [0, 1, 3]]
maze_list_5 = [[2, 1, 0], [0, 1, 3]]
print(traverse_maze(maze_list_5))

# Empty
maze_list_6 = [[]]
print(traverse_maze(maze_list_6))

# Only entry
maze_list_7 = [[2]]
print(traverse_maze(maze_list_7))
















