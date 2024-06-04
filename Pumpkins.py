def plant_pumpkins():
    till_field()             
    # Plant until all pumpkins grow successfully
    while True:
        # Prepare enough seeds to plant the whole field
        if num_items(Items.Pumpkin_Seed) < world_area:
            trade(Items.Pumpkin_Seed, world_area)
        # Make a lambda function to allow using a function with an arguement
        def plant_pumpkin_seed():
            plant(Entities.Pumpkin)
        # Plant the whole filed once, ignoring success
        use_action_on_every_tile(plant_pumpkin_seed)
        
        # Traverse field and re-plant and insta-gro all failed pumpkins
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if get_entity_type() != Entities.Pumpkin:
                    trade(Items.Pumpkin_Seed, 100 - num_items(Items.Pumpkin_Seed))
                    accelerated_planting(Entities.Pumpkin)
                move(South)
            move(East)
        # Should be no need to check if the field is full, just harvest
        harvest()