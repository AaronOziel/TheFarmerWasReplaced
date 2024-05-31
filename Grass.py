from __builtins__ import *

clear()
while True:
	for i in range(3):
		if can_harvest():			
			harvest()
		move(North)
	move(East)
