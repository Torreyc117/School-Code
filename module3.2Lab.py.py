secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

number = int(input("Enter your guess, if you guess wrong you will be stuck in my game till you get it right. "))

while number != secret_number:
    if number % 2 == 1:
        print("you entered an odd number")
    else:
        print("you entered an even number")
        
    print("you guessed ", number)
    print("Ha ha! You're stuck in my loop!")
    number = int(input("guess another number. "))
    
    
print(secret_number, "is the secret number!")
print("Well done, muggle! You are free now.")