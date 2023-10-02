def possibleMoves(tablero, position, remaining_moves):

    X = [2, 1, -1, -2, -2, -1, 1, 2]
    Y = [1, 2, 2, 1, -1, -2, -2, -1]

    if remaining_moves == 0:
        return 1

    count = 0

    for i in range(8):
        x = position[0] + X[i]
        y = position[1] + Y[i]

        if(x >= 0 and y >= 0 and x < 4 and y < 3 and tablero[x][y] == 1):
            count += possibleMoves(tablero, [x, y], remaining_moves - 1)
        
    return count


tablero = [[1, 1, 1],
          [1, 1, 1],
          [1, 1, 1],
          [0, 1, 0]]

remaining_moves = 21

total_moves = 0

for row in range(len(tablero)):
    for column in range(len(tablero[row])):
        if (tablero[row][column] == 1):
            total_moves += possibleMoves(tablero, [row, column], remaining_moves)   
        
print(total_moves)


