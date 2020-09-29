# loading the numpy libray
import numpy
import pygame

# setting the values :
ON = 1
OFF = 0

# size of array :
N=10
CELLSIZE = 32
H_CELLSIZE = CELLSIZE / 2

# define a 2D array (10x10):
grid = numpy.array([
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,0,0]
    ])

#Start pyGame Engine :
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1500)


# draw the 'g' grid, of size 'N' :
def draw_grid(g,N):
    for numligne in range(0,N):
        # display all cells in a row :
        for numcol in range(0,N):
            print(g[numligne,numcol],end='')
        # finally : add a carriage return :
        print()

# define rulez for grid 'g' of size 'N' :
def update(g,N):
    newgrid = g.copy()
    for numligne in range(0,N):
        for numcol in range(0,N):
            #count neighbors  :
            total = g[(numligne-1)%N,(numcol-1)%N]
            total = total + g[(numligne-1)%N,numcol]
            total = total +     g[(numligne-1)%N,(numcol+1)%N]
            total = total +     g[(numligne),(numcol-1)%N]
            total = total +     g[(numligne),(numcol+1)%N]
            total = total +     g[(numligne+1)%N,(numcol-1)%N]
            total = total + g[(numligne+1)%N,(numcol)]
            total = total + g[(numligne+1)%N,(numcol+1)%N]

            # applying Conway's rulez !
            if g[numligne,numcol]==ON:
                if (total<2) or (total >3) :
                    newgrid[numligne,numcol]=OFF
            if g[numligne,numcol]==OFF:
                if (total==3):
                    newgrid[numligne,numcol]=ON
    g[:] = newgrid[:]
    return g


def board_to_scr(pos):
    x, y = pos
    return (x * CELLSIZE + H_CELLSIZE, y * CELLSIZE + H_CELLSIZE)


while True:
	# Check if we want to exit : 
	if pygame.event.get(pygame.QUIT): 
		break

	# Let's clean the screen :
	screen.fill(pygame.color.Color('white'))
	for numligne in range(0,N):
		for numcol in range(0,N):
			pygame.draw.circle(screen, pygame.color.Color('black'), board_to_scr(cell), H_CELLSIZE, 0)

	pygame.display.flip()
	grid = update(grid,N)
	clock.tick(60)
	













