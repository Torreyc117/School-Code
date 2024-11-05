def validatePassword(passW):
    
        
    if passW[0].isdigit():
        print("The first letter is a number, Choose a stronger password.")
            
    else:
        print("The first letter is not a number.")
        
    if len(passW) >= 10:
        print("The password length is at least 10.")    
    
    else:
        print("Password not long enough.")
    
    if "qwerty" not in passW:
        print("qwerty is not present.")
            
    if "1234" not in passW:
        print("1234 is not present.")
        
    for char in passW:
        
        if char in "01234567890":
            print("There is a number.")
        
        if char in "!@#$%^&*()+=":
            print("There is a symbol.")
            
        if char.isupper():
            print("There is an upper case letter.")
                
            
            
        
