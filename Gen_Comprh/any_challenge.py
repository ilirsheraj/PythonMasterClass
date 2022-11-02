from data import people, plants_list, plants_dict


if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
	print("This dict contains Grasses")
else:
	print("No Grasses in the dict")

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
	print("This dict contains Grasses")
else:
	print("No Grasses in the dict")

# Check for cactus
if any(plants_dict[key].plant_type == "Cactus" for key in plants_dict):
	print("This dict contains Cactus")
else:
	print("No Cacti in the dict")