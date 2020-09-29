# Python code to implement Conway's Game Of Life
import os
import time
import numpy as np

def clear(): os.system('clear') #cls on Windows

# setting up the values for the grid
ON = 1
OFF = 0

def definegrid():
    g = np.array([
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ])
    return(g)

def draw_grid(grid,N):
    for i in range (N):
        for j in range(N):
            if grid[i,j]==ON:
                print("O",end='')
            else:
                print(" ",end='')
        print('')

def update(g, N):

    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = g.copy()

    for i in range(N):
        for j in range(N):
            # compute 8-neighbors sum
            # using toroidal boundary conditions - x and y wrap around
            total = g[i, (j-1)%N]
            total = total  + g[i, (j+1)%N]
            total = total  + g[(i-1)%N, j]
            total = total  + g[(i+1)%N, j]
            total = total  + g[(i-1)%N, (j-1)%N]
            total = total  + g[(i-1)%N, (j+1)%N]
            total = total  + g[(i+1)%N, (j-1)%N]
            total = total  + g[(i+1)%N, (j+1)%N]

            # apply Conway's rules
            if g[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    g[:] = newGrid[:]
    return g


# main() function
def main():
    # declare grid
    grid=definegrid()
    N=10
    while 1:
        clear()
        draw_grid(grid,N)
        time.sleep(0.1)
        grid=update(grid,N)

# call main
if __name__ == '__main__':
    main()
