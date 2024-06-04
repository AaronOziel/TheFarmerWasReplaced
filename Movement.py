def simplistic_move(x, y): # x: int, y: int
    # Rudamentary input sanitization
    if x > get_world_size() or y > get_world_size():
        return False
        
    # The drone will not use world wrapping to its advantage
    while get_pos_x() != x:
        if x < get_pos_x():
            move(West)
        else:
            move(East)
    while get_pos_y() != y:
        if y < get_pos_y():
            move(South)
        else:
            move(North)

def quick_move(x, y): # x: int, y: int
    # Rudamentary input sanitization
    if x > get_world_size() or y > get_world_size():
        return False       
    
    left = True # West
    # If destination is on the negative, go right
    if get_pos_x() - x < 0:
        left = False
    x_delta = abs(get_pos_x() - x)
    # If going the opposite direction is shorter, flip direction
    if get_world_size() - x_delta <= x_delta:
        left = not left
    # Convert boolean into direction
    if left:
        direction = West
    else:
        direction = East
    # Go there
    while get_pos_x() != x:
        move(direction)
    
    down = True # South
    # If destination is on the negative, go up
    if get_pos_y() - y < 0:
        down = False
    y_delta = abs(get_pos_y() - y)
    # If going the opposite direction is shorter, flip direction
    if get_world_size() - y_delta <= y_delta:
        down = not down
    # Convert boolean into direction
    if down:
        direction = South
    else:
        direction = North
    # Go there
    while get_pos_y() != y:
        move(direction)