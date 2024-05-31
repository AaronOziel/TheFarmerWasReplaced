clear()
do_a_flip() 

while True:
    for i in range(get_world_size()):
        if can_harvest():            
            harvest()
            water()
            if get_ground_type() == Grounds.Turf:
                till()
            if num_items(Items.Carrot_Seed) == 0:
                trade(Items.Carrot_Seed)
            plant(Entities.Carrots)
        move(South)
    move(East)