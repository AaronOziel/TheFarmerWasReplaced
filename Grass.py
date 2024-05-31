clear()
do_a_flip()

while True:
    for i in range(get_world_size()):
        if can_harvest():            
            harvest()
        move(South)
    move(East)