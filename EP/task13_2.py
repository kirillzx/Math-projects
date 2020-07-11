#function for pretty print Matrix
def pr_matrix(matrix):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in matrix]))

#function for check neighbours near the current cell
def get_neighbours(cell, world):
    row_SIZE = len(world)
    col_SIZE = len(world[1])
    neighbours = []
    rows = [cell[0]-1, cell[0], cell[0]+1] # All possible rows
    cols = [cell[1]-1, cell[1], cell[1]+1] # All possible cols
    for r in rows:
        if (r < row_SIZE and r >= 0): # Checks if the cell is at the edge
            for c in cols:
                if (c < col_SIZE and c >= 0): # Checks if the cell is at the edge
                    if ((r!=cell[0]-1 and r!=cell[0]+1) or (c!=cell[1]-1 and c!=cell[1]+1)):
                            neighbour = [r, c]
                            if (neighbour!=[cell[0], cell[1]]): # Remove the current cell from the neighbours list
                                neighbours.append(neighbour)
    return neighbours

def breadth_first(world, start):
    world[start[0]][start[1]] = 1
    queue = []
    queue.append(start)

    while len(queue)!=0:
        cell = queue.pop(0)
        neighbours = get_neighbours(cell, world)
        for i in range(len(neighbours)):
            if world[neighbours[i][0]][neighbours[i][1]] == 0:
                world[neighbours[i][0]][neighbours[i][1]] = world[cell[0]][cell[1]] + 1
                queue.append(neighbours[i])
    return world

def get_path(matrix, begin, end):
    current = end
    path = [(end[0], end[1])]
    while current != begin:
        x = current[0]
        y = current[1]
        current_counter = matrix[x][y]

        if matrix[x+1][y] == current_counter - 1:
            current = (x+1, y)
        elif matrix[x-1][y] == current_counter - 1:
            current = (x-1, y)
        elif matrix[x][y+1] == current_counter - 1:
            current = (x, y+1)
        elif matrix[x][y-1] == current_counter - 1:
            current = (x, y-1)

        path.append((current[0], current[1]))

    return path

'''Test'''
world = [[-1, -1, -1, -1, -1, -1],
         [-1,0, 0, 0, 0, -1],
		 [-1,0, 0, -1, -1, -1],
		 [-1,0, 0, -1, 0, -1],
		 [-1,0, 0, 0, 0, -1],
         [-1,0, -1, 0, 0, -1],
         [-1, -1, -1, -1, -1, -1]]
start = (1, 2) # list of 2 values [row, col]
goal = (4, 4) # list of 2 values [row, col]

matrix = breadth_first(world, start)
pr_matrix(matrix)
print(get_path(matrix, start, goal))
