
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

# VARIABLES



all_num = [1,2,3,4,5,6,7,8,9]
tiles = []
tile_list = []

# REFERENCE LIST
# ITERATE ALL TILES AND ATTEMPT NUMBERS
for k,v in grid.items():
    if v == 0:
        print('k: ', k)
        row_num = k % 10    
        col_num = (k - row_num) / 10
        for key, val in sector.items():
            if k == key:
                sqa_num =(val)
        
        # CODE: all_num - tile list = numbers to attempt
        #  EX: 3 or 5, pick one and continue
        # If next round fails go back to previous round and place new next valid number
        # Keep track of failed numbers by adding them to the column or row they belong in GRID

        break



ax = row_num
ay = int(col_num)
az = sqa_num



# NUMBER COMPILER CHECKLIST -----------------------------------------
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


# END NUMBER COMPILER CHECKLIST -----------------------------------------

print('row: ', row_num)
print('col: ', int(col_num))
print('sqa: ', sqa_num)

print('Tile list: ', tile_list)