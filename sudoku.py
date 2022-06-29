# Sudoku solver built without looking at other sudoku builds.

from raw_data import grid, sector, print_grid

test_num = [1,2,3,4,5,6,7,8,9]

# FUNCTIONS----------------------------
def horizontal(x): # ROWS
    t = 0
    temp = []
    for k,v in grid.items():
        if (k - x) % 10 == 0 and v > 0:
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
    return temp 

def square(x):
    t = 0
    temp = []
    for k,v in sector.items():
        # print(k,v)
        for key, value in grid.items():
            if k == key and v == x and value > 0:
                t = t + value
                # print('Square: ', value)
                temp.append(value)
    # print('Square: ', temp)
    return temp

def round_1(): # ITERATES OVER TILES AND RETURNS NON ZERO TILES

    i = 0
    for k,v in grid.items():
        if v == 0: # IF VALUE IS 0
            missing_tiles = []
            tile_list = []
            tiles = []   
            ax = k % 10    
            ay_temp = (k - ax) / 10 
            ay = int(ay_temp)
            for key, val in sector.items():
                if k == key:
                    az = val

            for item in horizontal(ax):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        tile_list.append(tile)

            for item in vertical(ay):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        tile_list.append(tile)

            for item in square(az):
                tiles.append(item)
                for tile in tiles:
                    if tile not in tile_list:
                        tile_list.append(tile)
            
            num = 1 
            for num in test_num: # CREATES MISSING TILES LIST
                if num not in tile_list:
                    missing_tiles.append(num)
            # if len(missing_tiles) == 1:
            if len(missing_tiles) >= 1:
                grid[k] = missing_tiles[0] # REPLACES ZERO TILES WITH FIRST ITEM ON MISSING TILES LIST. (ITERATE THROUGH LIST FOR MORE OPTIONS)
                print('grid[k]: ', grid[k])
                i += 1

            print('k: ', k)
            print('tile_list: ', tile_list)
            print('missing_tiles: ', missing_tiles)
            print('i: ', i)
            print('\n')

    print_grid()



for k,v in grid.items():
    if v == 0: # IF VALUE IS 0
        round_1()

