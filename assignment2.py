#defining the message to add a parameter of a number
#whatever the number is it will still invoke the same answer 
#the parameter (number) is added to the print of "enter a number"" 
#and as long as a value is given the program will respond with the answer 1234
def message(number):
    print("Enter a number:", number)

number = 1234
message(1)
print(number)

#this program uses the return function to decide how to print the message
#if wishes is true then the program will read 3,2,1, happy new year
#if wishes is false then there will be no happy newyear printed in the message
#the return function is used on the wishes so that if it is false it returns to
#the invocation and and prints the 3,2,1 skpping the happy new year command.
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    
    print("Happy New Year!")