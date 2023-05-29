print("Enter the day the call started at:")
day = input()
print("Enter the time the call started at (hhmm):")
time = int(input())
print("Enter the duration of the call (in minutes):")
minutes = float(input())
        
if (day == "Monday","Tuesday","Wednesday","Thursday","Friday"):
    if (800 <= time <= 1800):
        charges = float(0.40)
    else:
        charges = float(0.25)
else:
    charges = 0.15

print("This call will cost $",charges*minutes)
