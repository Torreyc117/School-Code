try:
    
    with open("aboutmymac.txt","r") as myFile:
    
        lines = myFile.readlines()
        print(lines)
    
    
        myD = {}
        
    with open("aboutmymac.txt","W") as myFile:  
        
        for line in myFile:
            (key, val) = line.split(",")
            myD[int()] = val
            print(myD)
        
except Exception as e: #if it fails, print an error occured
    print("An error has occured.")       
    
    #incomplete