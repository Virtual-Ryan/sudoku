
# Sudoku solver built without looking at other sudoku builds.

from raw_data import grid, sector, print_grid



# FUNCTIONS----------------------------

#VERTICAL
def vertical(x,y):
    t = 0
    for k,v in grid.items():
        if k in range(x,y) and v > 0:
            # print(k, v)
            t = t + v
    return t

def horizontal(y):
    t = 0
    for k,v in grid.items():
        if (k - y) % 10 == 0 and v > 0:
            # print(k,v)
            t = t + v
    return t

def square(s):
    t = 0
    for k,v in sector.items():
        # print(k,v)
        for key, value in grid.items():
            if k == key and v == s and value > 0:
                # print(value)
                t = t + value
    return t


# END FUNCTIONS----------------------------

vert_1 = vertical(11,20) # Columns 11-20, 21-30 and so on.
horiz_1 = horizontal(1) # N - n divisible by 10
square_x = square(1) # No math options, brought in a cheat sheet.

print(f'Vertical: {vert_1}, Horizontal: {horiz_1}, Square: {square_x}')

print_grid()