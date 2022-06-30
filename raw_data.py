# A place for long unsightly code

# THIS IS THE PUZZLE INPUT
gridx = {
    11:4, 21:0, 31:2, 41:0, 51:0, 61:0, 71:3, 81:8, 91:0,
    12:1, 22:0, 32:9, 42:6, 52:0, 62:7, 72:4, 82:0, 92:0, 
    13:0, 23:0, 33:8, 43:3, 53:0, 63:0, 73:1, 83:0, 93:6, 
    14:0, 24:9, 34:0, 44:0, 54:3, 64:0, 74:0, 84:0, 94:4, 
    15:0, 25:2, 35:3, 45:9, 55:6, 65:4, 75:7, 85:1, 95:0, 
    16:8, 26:0, 36:0, 46:0, 56:1, 66:0, 76:0, 86:6, 96:0, 
    17:9, 27:0, 37:7, 47:0, 57:0, 67:6, 77:5, 87:0, 97:0, 
    18:0, 28:0, 38:5, 48:8, 58:0, 68:9, 78:6, 88:0, 98:2, 
    19:0, 29:4, 39:6, 49:0, 59:0, 69:0, 79:8, 89:0, 99:9
    }

grid = {
    11:0, 21:9, 31:0, 41:0, 51:0, 61:0, 71:6, 81:5, 91:1,
    12:3, 22:7, 32:0, 42:0, 52:8, 62:0, 72:0, 82:0, 92:0, 
    13:0, 23:0, 33:1, 43:9, 53:0, 63:0, 73:0, 83:0, 93:0, 
    14:0, 24:0, 34:0, 44:0, 54:0, 64:6, 74:3, 84:0, 94:0, 
    15:6, 25:3, 35:0, 45:2, 55:0, 65:0, 75:0, 85:0, 95:0, 
    16:4, 26:0, 36:0, 46:0, 56:5, 66:0, 76:9, 86:0, 96:6, 
    17:0, 27:0, 37:0, 47:0, 57:4, 67:0, 77:0, 87:2, 97:0, 
    18:0, 28:0, 38:0, 48:5, 58:3, 68:0, 78:0, 88:0, 98:4, 
    19:0, 29:5, 39:0, 49:8, 59:0, 69:0, 79:0, 89:0, 99:0
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

# THIS DIVIDES THE GRID INTO 9 EQUAL SECTORS
sector = {    
    11:1, 21:1, 31:1, 12:1, 22:1, 32:1, 13:1, 23:1, 33:1, 
    41:2, 51:2, 61:2, 42:2, 52:2, 62:2, 43:2, 53:2, 63:2, 
    71:3, 81:3, 91:3, 72:3, 82:3, 92:3, 73:3, 83:3, 93:3, 
    14:4, 24:4, 34:4, 15:4, 25:4, 35:4, 16:4, 26:4, 36:4, 
    44:5, 54:5, 64:5, 45:5, 55:5, 65:5, 46:5, 56:5, 66:5, 
    74:6, 84:6, 94:6, 75:6, 85:6, 95:6, 76:6, 86:6, 96:6, 
    17:7, 27:7, 37:7, 18:7, 28:7, 38:7, 19:7, 29:7, 39:7, 
    47:8, 57:8, 67:8, 48:8, 58:8, 68:8, 49:8, 59:8, 69:8, 
    77:9, 87:9, 97:9, 78:9, 88:9, 98:9, 79:9, 89:9, 99:9, 
    }

