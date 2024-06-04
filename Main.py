def water():
    if get_water() < 0.5:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)
     
def water_with_minimum(minimum): # minimum: float w/range 0 ~ 1
    if get_water() < minimum:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)

def accelerated_planting(entity_type): # entity_type: Entities
    while not can_harvest():
        if num_items(Items.Fertilizer) == 0:
            trade(Items.Fertilizer, world_area)
        if get_entity_type() != entity_type: 
            plant(entity_type)
        use_item(Items.Fertilizer)
        water()

def use_action_on_every_tile(action): # action: func
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            action()
            move(South)
        move(East)

def till_field():
    clear()
    use_action_on_every_tile(till)

def harvest_all():
    use_action_on_every_tile(harvest)
    
def quick_move(x, y): # x: int, y: int
    # Rudamentary input sanitization
    if x > get_world_size() or y > get_world_size():
        return False       
    
    left = True # Defualt is West
    # If destination is negative, go right
    x_delta = get_pos_x() - x
    if x_delta < 0:
        left = False
    # If going the opposite direction is shorter, flip direction
    x_delta = abs(x_delta)
    if get_world_size() - x_delta <= x_delta:
        left = not left
    # Convert boolean into direction
    # Note: The following code is allowed in real python and saves ~3 lines
    # direction = West if left else East
    if left:
        direction = West
    else:
        direction = East
    # Go there
    while get_pos_x() != x:
        move(direction)
    
    down = True # Default is South
    # If destination is negative, go up
    y_delta = get_pos_y() - y
    if y_delta < 0:
        down = False
    # If going the opposite direction is shorter, flip direction
    y_delta = abs(y_delta)
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