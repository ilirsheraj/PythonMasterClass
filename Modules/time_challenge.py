# Create a program that allows a user to choose one of up to 9 time zones from a menu.
# You can choose any zones you want from the all_timezones list.
# The program will then display the time in that timezone, as well as local time and UTC time.
# Entering 0 as the choice will quit the program.
# Display the dates and times in a format suitable for the user of your program to understand,
# and include the timezone name when displaying the chosen time.

import pytz
import datetime

time_zones = {
	"1": "America/Havana",
	"2": "America/Los_Angeles",
	"3": "Asia/Bangkok",
	"4": "Asia/Istanbul",
	"5": "Asia/Tokyo",
	"6": "Atlantic/Bermuda",
	"7": "Australia/Queensland",
	"8": "Europe/Minsk",
	"9": "Europe/Tirane",
}

print("Please choose one of the following time zones or 0 to quit: ")
for num, tzs in time_zones.items():
	print("\t{}: {}".format(num, tzs))

while True:
	choice = input()
	if choice == "0":
		break
	elif choice in time_zones.keys():
		t_zones = pytz.timezone(time_zones[choice])
		time_globe = datetime.datetime.now(tz=t_zones)
		print("The local time in {} is {}, {}".
			  format(time_zones[choice], time_globe.strftime("%A %x %X %z"), time_globe.tzname()))
		print("The local time in {} is {}".
			  format(time_zones[choice], datetime.datetime.now(tz=t_zones)))
		print("The UTC time in {} is {}".
			  format(time_zones[choice], datetime.datetime.utcnow()))

	else:
		print("Your choice is not correct, Please choose one of the following time zones or 0 to quit: ")
		for num, tzs in time_zones.items():
			print("\t{}: {}".format(num, tzs))
