#This function meant to convert a number of cups to tablespoons
def convertCupsToTablespoons(cupsParm):
    cupsParm = float(cupsParm)
    tablespoon = cupsParm / 0.0625
    return tablespoon
    
cupsParm = input("Enter the number of Cups ")
tablespoonOutput = convertCupsToTablespoons(cupsParm)
print(cupsParm,"Cups is equal to")
print(tablespoonOutput,"tablespoons")