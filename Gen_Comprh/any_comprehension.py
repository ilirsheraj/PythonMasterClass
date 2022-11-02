from data import people, basic_plants_list, plants_list


# Be careful, if the list is empty
# # people = []
# if all([person[1] for person in people]):
# 	print("Sending email")
# else:
# 	print("User must edit the list of recipients")

# Create a boolean for edge cases
people = []
if bool(people) and all([person[1] for person in people]):
	print("Sending email")
else:
	print("User must edit the list of recipients")
print()

if any([plant.plant_type == "Grass" for plant in plants_list]):
	print("This pack contains grass")
else:
	print("No grasses in this pack")
