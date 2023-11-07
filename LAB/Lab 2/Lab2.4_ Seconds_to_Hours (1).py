sec = int(input ("Enter the number of seconds: "))

hours = sec // 3600
rh_sec = sec % 3600
min = rh_sec // 60
r_sec = rh_sec % 60

print("There are", hours, "Hours,", min, "Minutes,", r_sec,"Seconds in", sec, "Seconds.")