#converting inches to centimeters
def convertInchesToCentimeters(inchesParm):
    inchesParm = float(inchesParm)
    centimeters = inchesParm * 2.54
    return centimeters
    
inchesParm = input("Enter the number of inches ") 
centimetersOutput = convertInchesToCentimeters(inchesParm)
print(centimetersOutput,"centimeters")