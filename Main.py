world_area = get_world_size() * get_world_size()

def water():
    if get_water() < 0.5:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)
     
def water_with_minimum(minimum):
    if get_water() < minimum:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)

def accelerated_planting(entity_type):
    while not can_harvest():
        if num_items(Items.Fertilizer) == 0:
            trade(Items.Fertilizer, world_area)
        if get_entity_type() != entity_type: 
            plant(entity_type)
        use_item(Items.Fertilizer)
        water()

def use_action_on_every_tile(action):
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

#planting(plant_carrots)
plant_pumpkins()