# use terminal in pycharm: pip install pytz
import pytz
import datetime

country = "Europe/Moscow"
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# # List of strings accepted by pytz
# for x in pytz.all_timezones:
# 	print(x)
# print()

# # pytz.country_names is a dictionary with country code as key and country name as value
# # Here is the code to explore it
# for key, val in pytz.country_names.items():
# 	print(key, " : ", val)
# print("*"*30)
# # Get the keys, sort them and then get the countries as well
# for x in sorted(pytz.country_names):
# 	print(x + ":" + pytz.country_names[x])
# print()
#
# for x in sorted(pytz.country_names):
# 	# Introduce get() in order to avoid program crash when timezone does not exist
# 	# It will return `None` for all the cases with no timezone
# 	print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))

# # Let's change the code and check if the key is in
# for x in sorted(pytz.country_names):
# 	print("{}: {}".format(x, pytz.country_names[x]), end=": ")
# 	if x in pytz.country_timezones:
# 		print(pytz.country_timezones[x])
# 	else:
# 		print("No time zone defined")
# print()

# # Print the time for each country
# for x in sorted(pytz.country_names):
# 	print("{}: {}".format(x, pytz.country_names[x]), end=": ")
# 	if x in pytz.country_timezones:
# 		for zone in sorted(pytz.country_timezones[x]):
# 			tz_to_display = pytz.timezone(zone)
# 			local_time = datetime.datetime.now(tz=tz_to_display)
# 			print("\t\t{}: {}".format(zone, local_time))
# 		print(pytz.country_timezones[x])
# 	else:
# 		print("\t\tNo time zone defined")
# print()

# Country timezones
for x, y in pytz.country_timezones.items():
	print(x, ":", y)
