income = float(input("Enter the annual income: "))

#
# Write your code here.
#
def calculatePIT(income):
    if income > 85528: #equation if income is more than the tax level
        income = float(income)
        tax = ((income - 85528) * .32) + 14839
        return tax
    elif income < 85528: #equation if the income was less than the tax level
        income = float(income)
        tax = income * .18 - 556.2
        return tax
    elif income > 1000000:          #tax relief = (1,000,000 - 85528) * .32
        income = float(income)      #             292,631 + 14839 = 307,470
        tax = (income - 307470) * .40#            32% + 18% max tax deductions
        
taxOutput = calculatePIT(income)

tax = round(taxOutput, 0) 
#tax rounded to 0

#any negative tax returns = 0. no money returned

print("The tax is:", tax, "thalers")