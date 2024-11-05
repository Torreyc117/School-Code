import a11function

while True:
    print("--------------------MENU--------------------")
    print("Press 1 to search for Cross-Site.")
    print("Press 2 to search for Injection.")
    print("Press 3 to search for Overflow.")
    print("Press 4 to specify a custom search.")
    print("Type quit to exit this program.")
    print("\n")
    userV = input("Select an option. \n").lower()
   
    if userV == "1":
        a11function.searchCVE("https://cve.circl.lu/api/last", str("Cross site").lower)
        
    if userV == "2":
        a11function.searchCVE("https://cve.circl.lu/api/last", str("Injection").lower)
        
    if userV == "3":
        a11function.searchCVE("https://cve.circl.lu/api/last", str("Overflow").lower)
        
    if userV == "4":
        a11function.searchCVE("https://cve.circl.lu/api/last", input("Type search term. \n"))
        
    if userV == "quit":
        break
    
    