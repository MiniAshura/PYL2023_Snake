import random


go_on = True
eat = True

map_width = 20
map_height = 20

def game_map(coordinates, food, width, height):

    grid = []
    for _ in range(width):
        row = []
        for _ in range(height):
            row.append('.')  
        grid.append(row) #dots
    

    
    for X, Y in coordinates:
        if 0 <= X < height and 0 <= Y < width:  
            grid[X][Y] = 'X' # Replace dots with X 
    
    for X, Y in food:
        if 0 <= X < height and 0 <= Y < width:  
            grid[X][Y] = 'F'
    
    for row in grid:
        print(' '.join(row))

# for testing this function use ex.: game_map([(0,0),(0,1),(0,2)])
        
def movement(coordinates, direction, food, width, height):
    
    last_X, last_Y = coordinates[-1]
    
    direction_map = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
    dx, dy = direction_map[direction]
    new_coor = (last_X + dx, last_Y + dy)
    
    if 0 <= new_coor[0] < height and 0 <= new_coor[1] < width:
        if new_coor in food:
            food.remove(new_coor)
            coordinates.append(new_coor)
            food.append(snake_food(coordinates + food))
        elif new_coor not in coordinates:
            coordinates.append(new_coor)
            coordinates.pop(0)
        else:
            return False  # Snake ran into itself
        return True
    return False

    
def snake_food(no_food):
    while eat:
        food_point = (random.randint(0, height - 1), random.randint(0, width -1))
        if food_point not in no_food:
            return food_point

coordinates = [(0,0),(0,1),(0,2)]
food = [snake_food(coordinates, map_width, map_height)]


while go_on:
    game_map(coordinates, food, map_width, map_height)
    user_direction = input("What is your movement (north, south, east, west)? Type 'end' to stop the game: ").lower()
    
    map= {'north': 'n', 'south': 's', 'east': 'e', 'west': 'w'}
    
    if user_direction == 'end':
        go_on = False
        print("Game over.")    
    elif user_direction in map:
        movement(coordinates, map[user_direction])
    elif user_direction not in map:
        print("Wrong move, try again.")
    else:
        print("Invalid input, try again.")


