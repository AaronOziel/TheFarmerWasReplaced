def plant_pumpkins():
    clear()
    do_a_flip()
    
    # Till + Water field
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            water()
            if get_ground_type() == Grounds.Turf:
                till()
            move(South)
        move(East)

            
    # Plant until all pumpkins grow successfully    
    while True:
        all_grown = True
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if get_entity_type() != Entities.Pumpkin:
                    all_grown = False
                    if num_items(Items.Pumpkin_Seed) == 0:
                        trade(Items.Pumpkin_Seed, get_world_size()*get_world_size())
                    plant(Entities.Pumpkin)
                    water()
                else:
                    all_grown = all_grown and can_harvest()      
                move(South)
            move(East)        
        if all_grown:
            harvest()

