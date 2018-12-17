MAX_X = 20
MAX_Y = 20


def numPaths(x,y):

    path_grid = [[0 for num in range(0,MAX_X+1)] for num in range(0,MAX_Y+1)]

    for x in range(0,MAX_X+1):
        for y in range(0,MAX_Y+1):
            if y == 0:
                path_grid[x][y] = 1
            elif 0 < y < x:
                path_grid[x][y] = path_grid[x][y - 1] + path_grid[x - 1][y]
            elif x == y:
                path_grid[x][y] = 2 * path_grid[x][y - 1]
    return path_grid


#MAIN
grid = numPaths(0,0)
for sub_list in grid:
    print(sub_list)