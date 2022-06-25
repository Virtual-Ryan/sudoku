
# Sudoku solver built without looking at other sudoku builds.

from raw_data import grid, sector, print_grid

# FUNCTIONS----------------------------

#VERTICAL
def vertical(x):
    t = 0
    temp = []
    x = (x * 10) + x
    for k,v in grid.items():
        y = x + 9
        if k in range(x,y) and v > 0:
            t = t + v
            # print('Vertical: ', k, v)
            temp.append(v)
    # print('Vertical: ', temp)
    return temp

def horizontal(y):
    t = 0
    temp = []
    for k,v in grid.items():
        if (k - y) % 10 == 0 and v > 0:
            t = t + v
            # print('Horizontal: ', k,v)
            temp.append(v)
    # print('Horizontal: ', temp)
    return temp

def square(s):
    t = 0
    temp = []
    for k,v in sector.items():
        # print(k,v)
        for key, value in grid.items():
            if k == key and v == s and value > 0:
                t = t + value
                # print('Square: ', value)
                temp.append(value)
    # print('Square: ', temp)
    return temp

# END FUNCTIONS----------------------------


# FUNCTION CALLS COMBINED WITH VARIABLE ASSIGNMENTS IN A DEF:
ax = 1
ay = 1
az = 1

vert_1 = vertical(ax) # Columns 11-20, 21-30 and so on.
horiz_1 = horizontal(ay) # N - n divisible by 10
square_x = square(az) # No math options, brought in a cheat sheet.


# print(f'Vertical: {vert_1},\nHorizontal: {horiz_1},\nSquare: {square_x}')

# print_grid()

all_num = [1,2,3,4,5,6,7,8,9]
tiles = []
tile_list = []

# PSEUDO:

# for k,v in grid.items():
#     if v == 0:
#         # print(k)
#         for item in vertical(ax), horizontal(ay), square(az):
#             for i in item:
#                 tiles.append(item)
#         # tiles.append(horizontal(ay))
#         # tiles.append(square(az))
#         print(tiles)
#         break


for k,v in grid.items():
    if v == 0:
        # for x in range(9):
        #     print(*vertical(ax))
        for item in vertical(ax):
            tiles.append(item)
            for tile in tiles:
                if tile not in tile_list:
                    tile_list.append(tile)

        for item in horizontal(ay):
            tiles.append(item)
            for tile in tiles:
                if tile not in tile_list:
                    tile_list.append(tile)

        for item in square(az):
            tiles.append(item)
            for tile in tiles:
                if tile not in tile_list:
                    tile_list.append(tile)

            # tiles.append(horizontal(ay))
            # tiles.append(square(az))
        print(tile_list)
        break

print('All done')
