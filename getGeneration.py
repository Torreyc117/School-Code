#Function to designate generational name based on birth year
def getGeneration(birthYearParm):
    if birthYearParm < 1946:
        return ("silent generation.")
    if birthYearParm < 1965:
        return ("boomer generation.")
    if birthYearParm < 1981:
        return ("gen X generation.")
    if birthYearParm < 1998:
        return ("millenial generation.")
    if birthYearParm > 1998:
        return ("post-millennial generation.")
        
birthYearParm = input("Please enter your birth year in YYYY format: ")

birthYearParm = int(birthYearParm)

print(birthYearParm, "is your birth year, your generation is the ")

print(getGeneration(birthYearParm))