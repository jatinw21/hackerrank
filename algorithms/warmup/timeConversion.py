#!/usr/bin/env python3
import re

time = input().strip()

# 12:00:00AM - 00:00:00
# 12:00:01AM - 00:00:00
# 12:59:59AM - 00:59:59
# 01:00:00AM - 01:00:00
# 11:59:59AM - 11:59:59
# 12:00:00PM - 12:00:00
# 12:59:59PM - 12:59:59
# 01:00:00PM - 13:00:00
# 11:59:59PM - 23:59:59

# NOTE: way to regex match and group capture like perl
match = re.search('^(\d\d):(\d\d):(\d\d)([AP]M)', time)

# NOTE: way to retrieve matched groups (starts from 1, not 0)
# NOTE: cast to int to later do int comparison
hour, minute, sec, ampm = int(match.group(1)), int(match.group(2)), int(match.group(3)), match.group(4)

# NOTE:if we don't want to print default spaces with print for diff variables, add sep=""
# DEBUG
# print(hour, minute, sec, ampm)

# NOTE: coz string comparison, don't forget to add '' around AM otherwise python
# check equality with non-existent variable AM
if hour == 12 and ampm == 'AM':
    # NOTE: zfill used to pad with 0 but it only works with str so casted to str
    print("00:", str(minute).zfill(2),":", str(sec).zfill(2), sep="")
elif (hour > 0 and hour < 12 and ampm == AM) or (hour == 12 and ampm == 'PM'):
    print(str(hour).zfill(2), str(minute).zfill(2), str(sec).zfill(2), sep=":")
elif hour < 12 and hour > 0 and ampm == 'PM':
    print(hour + 12, str(minute).zfill(2), str(sec).zfill(2), sep=":")
