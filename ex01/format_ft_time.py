import time


print(
    "Seconds since January 1, 1970:",
    time.time(),
    "or",
    "{:e}".format(time.time()),
	"in scientific notation",
)

date = time.localtime(time.time())
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

print(months[date.tm_mon - 1], date.tm_mday, date.tm_year)
