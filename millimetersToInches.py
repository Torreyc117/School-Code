#This function is for converting distance from inches to millimeters
def convertMillimetersToInches(millimeterParm):
    millimeterParm = float(millimeterParm)
    inches = millimeterParm * 0.0393701
    return inches

millimeterParm = input("Enter the number of Inches ")
inchesOutput = convertMillimetersToInches(millimeterParm)
print(millimeterParm,"Millimeters is equal to")
print(inchesOutput,"Inches")