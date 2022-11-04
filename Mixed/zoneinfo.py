from datetime import datetime, timezone
import zoneinfo


utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo("America/New_York")
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)
