def planting(plant): # function
    clear()
    do_a_flip()
    
    while True:
        for i in range(get_world_size()):
            if can_harvest():            
                harvest()
                water()
                plant()
            move(South)
        move(East)

def plant_grass():
    pass
          
def plant_carrots():
    if get_ground_type() == Grounds.Turf:
        till()
    if num_items(Items.Carrot_Seed) == 0:
        trade(Items.Carrot_Seed, get_world_size() * get_world_size())
    plant(Entities.Carrots)

def plant_trees():
    if (get_pos_x() % 2 == 0 and get_pos_y() % 2 == 1) or (get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0):
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)