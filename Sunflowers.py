# Finally, Sunflowers!
def plant_sunflowers():
    # Prep field
    till_field()
    # Buy seeds and plant
    trade(Items.Sunflower_Seed, 105 - num_items(Items.Sunflower_Seed))
    # Define a sunflower seed planting lambda     
    def plant_sunflower_seed():
        plant(Entities.Sunflower)
        water()
    use_action_on_every_tile(plant_sunflower_seed)
    
    # Measure!
    field_measurements = []
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            field_measurements.append((measure(), get_pos_x(), get_pos_y()))
            move(South)
        move(East)
    
    max_petals, x, y = max(field_measurements)
    while max_petals >= 10:
        quick_move(x,y)
        harvest()
        # Remove record of flower just harvested
        field_measurements.remove((max_petals, x, y))
        # Replant flower and measure its petals
        trade(Items.Sunflower_Seed, 105 - num_items(Items.Sunflower_Seed))
        accelerated_planting(Entities.Sunflower)
        field_measurements.append((measure(), x, y))
        # Find new max flower
        max_petals, x, y = max(field_measurements)
        