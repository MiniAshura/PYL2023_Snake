def game_map(coordinates):

    grid = [] #emty
    for _ in range(10):
        row = []
        for _ in range(10):
            row.append('.')  
        grid.append(row) #dots

    
    for X, Y in coordinates:
        if 0 <= X < 10 and 0 <= Y < 10:  
            grid[X][Y] = 'X' # Replace dots with X 
    
    
    for row in grid:
        print(' '.join(row))

# for testing this function use ex.: game_map([(0,0),(0,1),(0,2)])
        
def movement(coordinates, direction):
    
    last_X, last_Y = coordinates[-1]
    
    
    if direction == 'n':  # North
        new_coor = (last_X - 1, last_Y)
    elif direction == 's':  # South
        new_coor = (last_X + 1, last_Y)
    elif direction == 'e':  # East
        new_coor = (last_X, last_Y + 1)
    elif direction == 'w':  # West
        new_coor = (last_X, last_Y - 1)
    else:
        print("Invalid input, try again")
        return
    coordinates.append(new_coor)

coordinates = [(0,0),(0,1),(0,2)]
go_on = True

while go_on:
    game_map(coordinates)  
    user_direction = input("What is your movement (north, south, east, west)? Type 'end' to stop the game: ").lower()
    
    map= {'north': 'n', 'south': 's', 'east': 'e', 'west': 'w'}
    
    if user_direction == 'end':
        go_on = False
        print("Game over.")    
    elif user_direction in map:
        movement(coordinates, map[user_direction])
    else:
        print("Invalid input, try again.")