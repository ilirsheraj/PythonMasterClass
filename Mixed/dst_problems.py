from datetime import datetime, timezone, timedelta
import zoneinfo


uk_tz = zoneinfo.ZoneInfo('Europe/London')
america_tz = zoneinfo.ZoneInfo('America/New_York')

year = 2022
month = 3
day = 27
hour = 0
minute = 25

td = timedelta(minutes=5)

utc_time = datetime(year, month, day, hour, minute, tzinfo=timezone.utc)
utc_time = utc_time + td
uk_time = datetime(year, month, day, hour, minute, tzinfo=uk_tz)
uk_time = uk_time + td
uk_to_utc = uk_time.astimezone(timezone.utc)
print(f'Line 19/20 - utc_time:\t {utc_time}')
print(f'Line 21/22 - uk_time:\t {uk_time}')
print(f'Line 23 - uk --> utc:\t {uk_to_utc}')

ny1 = uk_time.astimezone(america_tz)
ny2 = utc_time.astimezone(america_tz)
print()
print(f'uk --> ny:\t {ny1}')
print(f'utc --> ny:\t {ny2}')
print(ny1 == ny2)

# <------------------------------------------->
print()
print('*' * 40)
print(f'Check: uk time equals UTC time: {uk_time == utc_time}')
print(f'Check: uk in UTC equals UTC time: {uk_to_utc == utc_time}')
print('-' * 40)