
# Sudoku solver built without looking at other sudoku builds.

from raw_data import grid, sector, print_grid

# FUNCTIONS----------------------------
# Returns list of non zero numbers existing in the row/col/square to run against test numbers

def horizontal(y): # ROWS
    t = 0
    temp = []
    for k,v in grid.items():
        if (k - y) % 10 == 0 and v > 0:
            t = t + v
            # print('Horizontal: ', k,v)
            temp.append(v)
    # print('Horizontal: ', temp)
    return temp

def vertical(x): #COLUMNS!! # k:97 =
    t = 0
    temp = []
    x = (x * 10) + 1 
    for k,v in grid.items():
        y = x + 9
        if k in range(x,y) and v > 0:
            t = t + v
            # print('Vertical: ', k, v)
            temp.append(v)
    # print('Vertical: ', temp)
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

# VARIABLES

test_num = [1,2,3,4,5,6,7,8,9]

# REFERENCE LIST
# ITERATE ALL TILES AND TEST NUMBERS IN TILES THAT EQUAL ZERO

def round_1():
    i = 0
    for k,v in grid.items():
        if v == 0:
            missing_tiles = []
            tile_list = []
            tiles = []         # if k == 44:
            row_num = k % 10    
            col_num = (k - row_num) / 10
            for key, val in sector.items():
                if k == key:
                    sqa_num =(val)

            ax = row_num
            ay = int(col_num)
            az = sqa_num

            for item in horizontal(ax):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        # print('HORI: ', tile)
                        tile_list.append(tile)

            for item in vertical(ay):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        # print('VERT: ', tile)
                        tile_list.append(tile)

            for item in square(az):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        # print('SQUA: ', tile)
                        tile_list.append(tile)
            
            num = 1 
            for num in test_num:     # TESTING NUMBERS
                if num not in tile_list:
                    missing_tiles.append(num)
            if len(missing_tiles) == 1:
                grid[k] = missing_tiles[0]
                # print('print: ', k,v) # TESTING
                i += 1

            # print('k: ', k)
            # print('tile_list: ', tile_list)
            # print('missing_tiles: ', missing_tiles)
            # print('i: ', i)
    
    print('\n')

    print_grid()

round_1()
round_1()
round_1()
round_1()

# potentially look at different method altogether.
# everything has to add to 45 and everything has to include a exclusive single digit (not including 0)

# EXPERIMENTAL FIND AND PICK FROM 2 OPTIONS

