from random import randint, shuffle

# creates 9 lists with 9 numbers in each list
def sudoku():
    grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]
    # while len(grid) < 9:
        # for i in range (0, 10, 1):
        #     randNum = randint(0, 9)
        #     arr = [randNum,randNum,randNum,randNum,randNum,randNum,randNum,randNum,randNum]

        # for i in range(1, 10, 1):
        #     shuffle(arr)
        #     if i == 9:
        #         grid.append(arr)
    return grid

# function to check if each row has 1-9, each col has 1-9 and each 3x3 box has 1-9
def check(grid):
    count = 0
    for i in range(1, 10, 1):
        num = i
        if grid[i][j] == num:
            count += 1
        # check each row
        for i in range(0, 10, 1): #this checks each array 'row' starting at zero
            for j in range(0, 10, 1): #this checks each array 'col' starting at zero
                if grid[i][j] == num:
                    return False

        for i in range(0, 10, 1): #this goes through each array 'row' starting at zero
            for j in range(0, 10, 1): #this goes through each array 'col' starting at zero
                if grid[j][i] == num:
                    return False
        
        # check 3x3 box
        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                if grid[i][j] == num:
                    return False



def get_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)  # row, col