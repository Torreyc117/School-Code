year = int(input("Enter a year: "))

#
# Write your code here.
#

    #program proceeds to check through all the questions till it fails
    #then provids its answer
    #if year isnt within the calandar, stops program and reports
if year < 1582:	
    print(year, "is not within the Gregorian calandar period.")
    
if year % 4 != 0 :
    if year % 100 != 0:
        if year % 400 != 0:
            print(year, "is a common year.")
        else:
            print(year, "is a leap year.")
    else: 
        print(year, "is a common year.")
else:
    print(year, "is a leap year.")


    