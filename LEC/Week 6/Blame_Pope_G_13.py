def leapyearcheck():
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False
    


#                                                           0123456789
themegadate = input("Enter the date to check (in the format MM/DD/YYYY): ")

#splitting the date to month, day, and year
month = int(themegadate[0:2])
day   = int(themegadate[3:5])
year  = int(themegadate[6:])


if month in [4,6,9,11]:
    
    if 1 <= day <= 30:
        print(themegadate, "is a valid date in the Gregorian Calendar.")
    else:
        print(themegadate, "is not a valid date")
        
#for 31 days
elif month in [1,3,5,7,8,10,12]:
    
    if 1 <= day <=31:
        print(themegadate, "is a valid date in the Gregorian Calendar.")
    else:
        print(themegadate, "is not a valid date")
        
#for Feb 28 or 29
elif month == 2:
    if 1 <= day <= 28:
        leapyearcheck()
    elif 1 <= day <= 29:
        print(themegadate, "is a valid date in the Gregorian Calendar.")
else:
    print(month, "is not a valid month")