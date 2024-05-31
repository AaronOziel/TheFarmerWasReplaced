def water():
    if get_water() < 0.5:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)
     
def water_with_minimum(minimum):
    if get_water() < minimum:
        while(get_water() < 0.75):
            use_item(Items.Water_Tank)

planting(plant_carrots)