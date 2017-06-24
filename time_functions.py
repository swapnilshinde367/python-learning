# pylint: skip-file
# time and calendar module and some functions

import time
import calendar

# Print timestamp
print time.time()

# Print current date and time
objTime = time.localtime( time.time() )
print objTime

# Print formatted current date and time
print time.asctime( time.localtime(time.time() ) )

# Print calendar for a month

print calendar.month( objTime.tm_year, objTime.tm_mon )