def convertPoundsToKilograms(lbsParm):
    lbsParm = float(lbsParm)
    kilos = lbsParm * 0.453592
    return kilos
    
lbsParm = input("Enter your weight in lbs ")
kilosOutput = convertPoundsToKilograms(lbsParm)
print(lbsParm,"lbs is equal to")
print(kilosOutput,"kilos")

def convertInchesToMeters(inchesParm):
    inchesParm = float(inchesParm)
    meters = inchesParm * 0.0254
    return meters
    
inchesParm = input("Emter your height in inches ")    
metersOutput = convertInchesToMeters(inchesParm)
print(inchesParm,"inches is equal to")
print(metersOutput,"meters")

#function to calculate BMI Body Mass Index.  A BMI of 25 or more is considered overweight
def calculateBMI(poundsParm, heightInchesParm):
    kilos = convertPoundsToKilograms(poundsParm)
    heightInchesParm = float(heightInchesParm)
    meters = convertInchesToMeters(heightInchesParm)
    bmi = kilos/ (meters**2)
    return bmi
    
kilos = kilosOutput
meters = metersOutput
bmiOutput = calculateBMI(lbsParm, inchesParm)
print("Your BMI is ",bmiOutput)

