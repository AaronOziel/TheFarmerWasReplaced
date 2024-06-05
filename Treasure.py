# Treasure! Oh boy, path finding algorithms!
def create_maze():
    clear()
    till()
    water()
    plant(Entities.Bush)
    while get_entity_type() != Entities.Hedge:
        trade(Items.Fertilizer)
        use_item(Items.Fertilizer)
    
def turn(facing, adjust): # facing: int, adjust: int -> int
    facing += adjust
    if facing < 0:
        facing += 4
    return facing % 4

def find_treasure_2():
    go = [North, East, South, West]
    facing = 0
    
    # Move the treasure if there already is one
    if num_items(Items.Fertilizer) < 100:
        trade(Items.Fertilizer, 105 - num_items(Items.Fertilizer))
    while get_entity_type() == Entities.Treasure:
        use_item(Items.Fertilizer)
  
    # Fine the new treasure
    while get_entity_type() != Entities.Treasure: 
        # 1st, attempt to turn right
        right = turn(facing, 1)
        if move(go[right]):
            facing = right
        # 2nd, if right doesn't work, go forward
        elif move(go[facing]):
            continue
        #3rd, lastly if right and forward do not work, turn left
        else: 
            facing = turn(facing, -1)