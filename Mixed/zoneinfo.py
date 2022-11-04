from datetime import datetime, timezone
import zoneinfo


utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = datetime.ZoneInfo("America/New_York")
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)

france_tz = zoneinfo.ZoneInfo("Europe/Paris")
france_now = utc_now.astimezone(france_tz)
print(france_now)

# Return all the available keys
print()
print("Available timezone keys")
print("-" * 23)

for zone_key in sorted(zoneinfo.available_timezones()):
	print(zone_key)
