
# THIS IS A FAR MORE ELEGANT SOLUTION THAN MY OWN. :)

grid = [
[0, 9, 0, 0, 0, 0, 6, 5, 1],
[3, 7, 0, 0, 8, 0, 0, 0, 0],
[0, 0, 1, 9, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 6, 3, 0, 0],
[6, 3, 0, 2, 0, 0, 0, 0, 0],
[4, 0, 0, 0, 5, 0, 9, 0, 6],
[0, 0, 0, 0, 4, 0, 0, 2, 0],
[0, 0, 0, 5, 3, 0, 0, 0, 4],
[0, 5, 0, 8, 0, 0, 0, 0, 0]
]

# PRINT GRID
def print_grid():
    for line in grid:
        # print(line)
        print(' '.join(map(str, line)))

# VERBATIM FROM COMPUTERPHILE SUDOKU SOLUTION

def possible(row, column, number):
    global grid # MAKES GRID A GLOBAL VARIABLE ( SO WE CAN USE IT INSIDE FUNCTIONS)
    for i in range(0,9): # IS THE NUMBER IN THE ROW?
        if grid[row][i] == number:
            return False

    for i in range(0,9):
        if grid[i][column] == number:
            return False

    x0 = (column // 3) * 3 # // DIVIDES AND ROUNDS DOWN, WHO KNEW?
    y0 = (row // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True



def solve():
    global grid
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column] == 0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0
                return
    
    print_grid()
    input('More?')

solve()



