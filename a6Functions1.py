def countIPAddress(listParm):
    ipD = {} #empty dictionary
    
    listParm = [i.split(".")[0] for i in listParm] #splitting ip at first octet
    listParm.sort() #sorting the IP list numerically 
    
    for item in listParm:
        
        if item in ipD: #if item is already in list add 1 to count
            ipD[item] += 1
            
        else: #if item isnt in the list add it with a count of 1
            ipD[item] = 1
            
    for key, value in ipD.items():
        print(key, value) #print the values of the dictionary side by side