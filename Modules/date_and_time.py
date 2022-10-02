# import time
#
# # Let's get the beginning of the epoch for this system
# print("The epoch of this system starts at " + time.strftime("%c", time.gmtime(0)))
# print("The current time zone is {} with an offset of {} seconds".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight Saving Time is in effect for the location")
#     print("\tThe DST timezone is " + time.tzname[1])
#
# print("Local time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# print("UTC time is " + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# Let's work with datetime module
import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

# We can also provide a timezone: It is left to developers
