import time

# # gmtime() method always works in UT starting of the epoch
# print(time.gmtime(0))
# print()
#
# # To get the local time we use localtime method
# print(time.localtime())
# print()
#
# # produces the same result as localtime
# print(time.localtime(time.time()))
# print()
#
# # Converts the time in seconds since jan 1 1970
# print(time.time())

# # Returns a tuple, so we can index it
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)
# print("Hour:", time_here[3], time_here.tm_hour)
# print("Minutes:", time_here[4], time_here.tm_min)
# print("Seconds:", time_here[5], time_here.tm_sec)

# Measure the elapsed time
# It will measure the time it takes the programmer to press enter and stop the waiting
# from time import time as my_timer
# perf_counter is the benchmark and very precise clock. Its not local time dependent
# from time import perf_counter as my_timer
# Monotonic is similar to perf_counter
# from time import monotonic as my_timer
# THis calculates cpu time
from time import process_time as my_timer
import random

input("Press enter to start")
# produces an integer 1-6 inclusive
wait_time = random.randint(1, 6)
print(wait_time)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

# If we give small x as argument, we get the current date
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {:4f} seconds".format(end_time - start_time))
