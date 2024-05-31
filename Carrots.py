from __builtins__ import *

clear()
while True:
	for i in range(3):
		if can_harvest():			
			harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			if num_items(Items.Carrot_Seed) == 0:
				trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
		move(North)
	move(East)
