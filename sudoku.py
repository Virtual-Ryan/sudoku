
# Sudoku solver built without looking at other sudoku builds.

# SIMPLE PUZZLE

grid = {
    11:4, 21:0, 31:2, 41:0, 51:0, 61:0, 71:3, 81:8, 91:0, 12:1, 22:0, 32:9, 42:6, 52:0, 62:7, 72:4, 82:0, 92:0, 13:0, 23:0, 33:8, 43:3, 53:0, 63:0, 73:1, 83:0, 93:6, 14:0, 24:9, 34:0, 44:0, 54:3, 64:0, 74:0, 84:0, 94:4, 15:0, 25:2, 35:3, 45:9, 55:6, 65:4, 75:7, 85:1, 95:0, 16:8, 26:0, 36:0, 46:0, 56:1, 66:0, 76:0, 86:6, 96:0, 17:9, 27:0, 37:7, 47:0, 57:0, 67:6, 77:5, 87:0, 97:0, 18:0, 28:0, 38:5, 48:8, 58:0, 68:9, 78:6, 88:0, 98:2, 19:0, 29:4, 39:6, 49:0, 59:0, 69:0, 79:8, 89:0, 99:9
    }

def print_grid():

    print(grid[11], grid[21], grid[31], grid[41], grid[51], grid[61], grid[71], grid[81], grid[91])
    print(grid[12], grid[22], grid[32], grid[42], grid[52], grid[62], grid[72], grid[82], grid[92])
    print(grid[13], grid[23], grid[33], grid[43], grid[53], grid[63], grid[73], grid[83], grid[93])
    print(grid[14], grid[24], grid[34], grid[44], grid[54], grid[64], grid[74], grid[84], grid[94])
    print(grid[15], grid[25], grid[35], grid[45], grid[55], grid[65], grid[75], grid[85], grid[95])
    print(grid[16], grid[26], grid[36], grid[46], grid[56], grid[66], grid[76], grid[86], grid[96])
    print(grid[17], grid[27], grid[37], grid[47], grid[57], grid[67], grid[77], grid[87], grid[97])
    print(grid[18], grid[28], grid[38], grid[48], grid[58], grid[68], grid[78], grid[88], grid[98])
    print(grid[19], grid[29], grid[39], grid[49], grid[59], grid[69], grid[79], grid[89], grid[99])

# FUNCTIONS----------------------------

#VERTICAL
def starts_with(s):
    x = 0
    for k,v in grid.items():
        if str(k).startswith(s) and v > 0:
            x = x + v
            # print(k,v)
            # print(x)
    return(x)

#HORIZONTAL        
def ends_with(s):
    x = 0
    for k,v in grid.items():
        if str(k).endswith(s) and v > 0:
            x = x + v
            # print(k,v)
            # print(x)
    return(x)

#SQUARE
def square_1(a,b,c):
    x = 0
    for k,v in grid.items():
        if str(k).startswith(a) and v > 0:
            x = x + v
        elif str(k).startswith(b) and v > 0:
            x = x + v
        elif str(k).startswith(c) and v > 0:
            x = x + v
    return(x)

def square_2(a,b,c):
    x = 0
    for k,v in grid.items():
        if str(k).endswith(a) and v > 0:
            x = x + v
        elif str(k).endswith(b) and v > 0:
            x = x + v
        elif str(k).endswith(c) and v > 0:
            x = x + v
    return(x)


# END FUNCTIONS----------------------------


# FUNCTION CALL
starts_with(str(1))
ends_with(str(1))
square_1(str(1), str(2), str(3))
square_2(str(1), str(2), str(3))





vert_1 = starts_with(str(1))
horiz_1 = ends_with(str(1))
square_x = square_1(str(1), str(2), str(3))
square_y = square_2(str(1), str(2), str(3))

print(vert_1, horiz_1, square_x, square_y)