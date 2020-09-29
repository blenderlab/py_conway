# Python code to implement Conway's Game Of Life
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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


def update(frameNum, img, grid, N):

    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    newGrid = grid.copy()

    for i in range(N):
        for j in range(N):
            # compute 8-neighbors sum
            # using toroidal boundary conditions - x and y wrap around
            total = grid[i, (j-1)%N]
            total = total  + grid[i, (j+1)%N]
            total = total  + grid[(i-1)%N, j] 
            total = total  + grid[(i+1)%N, j]
            total = total  + grid[(i-1)%N, (j-1)%N]
            total = total  + grid[(i-1)%N, (j+1)%N]
            total = total  + grid[(i+1)%N, (j-1)%N]
            total = total  + grid[(i+1)%N, (j+1)%N]

            # apply Conway's rules
            if grid[i, j]  == ON:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:
                if total == 3:
                    newGrid[i, j] = ON

    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# main() function
def main():


    # set animation update interval
    updateInterval = 1000

    # declare grid
    grid=definegrid()
    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, 10 ), interval=updateInterval)
    plt.show()

# call main
if __name__ == '__main__':
    main()
