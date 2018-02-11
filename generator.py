import random

# References:
# Prim's Algorithm Implementation in Ruby: http://weblog.jamisbuck.org/2011/1/10/maze-generation-prim-s-algorithm

INFINITY = 10
UNMARKED = -1
OPEN = 0x10
NEIGHBOR = 0x20
N, S, E, W = 1, 2, 4, 8
seed = 111111
SIZE = 33

# maze maker
def mazeInit(size):
    maze = [[0 for x in range(size)] for y in range(size)]
    return maze

# needed to print maze
def empty(cell):
    return cell == 0 or cell == NEIGHBOR

# algorithm setup
def addNeighbors(x, y, maze, neighbors):
    # print "addNeighbors()"
    # print "len(maze): ", len(maze)
    # print "len(neighbors): ", len(neighbors)
    # print "x: ", x
    # print "y: ", y
    if x >= 0 and y >= 0 and y < len(maze)-1 and x < len(maze[y])-1 and maze[y][x] == 0:
        maze[y][x] = NEIGHBOR
        neighbors.append((x,y))

# mark open
def mark(x, y, maze, neighbors):
    maze[y][x] = OPEN
    addNeighbors(x-1, y, maze, neighbors)
    addNeighbors(x+1, y, maze, neighbors)
    addNeighbors(x, y-1, maze, neighbors)
    addNeighbors(x, y+1, maze, neighbors)


getNeighbors = lambda x, y : [(x2,y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1,y+2)
                               if(-1 < x <= SIZE and
                                  -1 < y <= SIZE and
                                  (x != x2 or y != y2) and
                                  (0 <= x2 <= SIZE) and
                                  (0 <= y2 <= SIZE))]

def neighbors(x,y,maze):
    n = []
    if x > 0 and maze[y][x-1] & OPEN != 0:
        n.append([x-1,y])
    if x+1 < len(maze[y]) and maze[y][x+1] & OPEN != 0:
        n.append([x+1, y])
    if y > 0 and maze[y-1][x] & OPEN != 0:
        n.append([x,y-1])
    if y+1 < len(maze) and maze[y+1][x] & OPEN != 0:
        n.append[x,y+1]
    return n


def getDirection(fx,fy,tx,ty):
    if fx < tx :
        return E
    if fx > tx :
        return W
    if fy < ty :
        return S
    if fy > ty :
        return N

def getOppositeDirection(direction):
    if E:
        return W
    if W:
        return E
    if N:
        return S
    if S:
        return N

def displayMaze(maze):
    for row, y in zip(maze,maze[0]):
        output = "|"
        for x, cell in zip(row,row):
            if cell == NEIGHBOR:
                output+= "0"
            if empty(cell) and y+1 < len(maze) and empty(maze[y+1][x]):
                output += " "
            else:
                output += (" " if (cell & S != 0) else "_")

            if empty(cell) and x+1 < len(row) and empty(row[x+1]):
                output +=(" " if (y+1 < len(maze) and (empty(maze[y+1][x]) or empty(maze[y+1][x+1]))) else "_")
            elif cell & E != 0:
                output +=(" " if ((cell | row[x+1]) & S != 0) else "_")
            else:
                output += "|"
        print(output)

# prims algorithm

maze = mazeInit(SIZE)
neighbors = []
steps = 0
random.seed(seed)
mark(random.randint(0,len(maze)-1),random.randint(0,len(maze)-1), maze, neighbors)
while(neighbors):
    x, y = neighbors.pop(random.randint(0, len(neighbors)-1))
    n = getNeighbors(x,y)
    randi= random.randint(0, len(n)-1)
    # print "len(n): ", len(n)
    # print "randi: ", randi
    # print "n[]: ", n
    # print "n[randi]: ", n[randi]
    nx = n[randi][0]
    ny = n[randi][1]

    dir = getDirection(x,y,nx,ny)
    maze[y][x] = dir
    # print "len(maze): ", len(maze), "| len(maze[0]): ", len(maze[0])
    # print "ny: ", ny, "   nx: ",nx
    maze[ny][nx] = getOppositeDirection(dir)

    mark(x, y, maze, neighbors)

    displayMaze(maze)
    steps += 1

    print "\nsteps: ", steps
    print "**************************\n"


displayMaze(maze)
