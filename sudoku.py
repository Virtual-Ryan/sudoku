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


used_k_list = []

def rounds(n): # ITERATES OVER TILES AND RETURNS NON ZERO TILES
    # used_k_list = [] # WE MOVED THIS BACK SO WE HAD AN EXHAUSTIVE LIST OF ALL K CHANGED
    i = 0
    for k,v in grid.items():
        if v == 0: # IF VALUE IS 0
            missing_tiles = []
            tile_list = []
            tiles = []
            # used_k_list = []   
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
            
            if len(missing_tiles) == n: # THIS NEEDS TO BE SWITCHED TO PRIORITIZE FROM SMALLEST TO LARGEST.
                grid[k] = missing_tiles[0] # REPLACES ZERO TILES WITH FIRST ITEM ON MISSING TILES LIST. (ITERATE THROUGH LIST FOR MORE OPTIONS)
                print('TRUE grid[k]: ', grid[k])
                print('k: ', k)
                print('missing_tiles: ', missing_tiles)
                if k not in used_k_list:
                    used_k_list.append(k)
                    print_grid()
                    print('\n')
                    rounds(n)

            elif len(missing_tiles) == 0 and grid[k] == 0:
                if k not in used_k_list:
                    used_k_list.append(k) # APPENDING BROKEN K FOR MATH PURPOSES 


                    print('missing_tiles: ', missing_tiles)
                    print('tile_list: ', tile_list)
                    print('BREAK grid[k]: ', grid[k])
                    print('k: ', k)
                    print_grid()
                    print('\n')
                    continue             

            # print('END grid[k]: ', grid[k])


            # print('tile_list: ', tile_list)
            # print('i: ', i)
rounds(2)
print('used_k_list: ', used_k_list)         






# print_grid()
#     print(temp_list)
#     # print(j)
#     print_grid()