import better_code
from better_code import area_of_square


area = better_code.area_of_square(40)
area = area_of_square(40)
print(area)

print("Global Namespace")
namespace = globals() #.copy()

# because of loop, the namespace will change so you'll get an error
for name, obj in namespace.items():
	print(name, obj)
