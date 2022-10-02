# Write a small program to display information on the
# 4 clocks whose functions we have just looked at:
# time(), perf_counter, monotonic() and process_time()
# Use the documentation on the get_clock_infor() function
# to work out on how to call it for each of the clocks.

import time
print("time():\t\t\t", time.get_clock_info("time"))
print("perf_counter():\t", time.get_clock_info("perf_counter"))
print("monotonic():\t", time.get_clock_info("monotonic"))
print("process_time():\t", time.get_clock_info("process_time"))
