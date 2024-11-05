import sqlite3
CONNECTION = sqlite3.connect('FinalProject.sqlite3')


# This function takes and sorts the input data to find which node has the most failed payments
def failedPayments():
    
    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
    
        failedPayments = {} #creates a dictionary to store our failed payment records
    
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
        
            node = lineList[0] #assigns the first section of the split the value node
        
            if "User Failed Payment" in line: #searches the lines to seperate only the 
                                          #lines with the failed payments
                for line in lineList: #iterates through the failed payments
                    #print(line)
                    if node in failedPayments: #if node is already in list add 1 to count
                        failedPayments[node] += 1
            
                    else: #if node isnt in the list add it with a count of 1
                        failedPayments[node] = 1
            
        for node in failedPayments.items(): #prints the nodes from the dictionary list
            print(node)
    
    mostFailed = max(failedPayments, key = failedPayments.get) #prints the highest value among keys in the dictionary

    print(mostFailed, "is the node with the most failed payments.")
    
    
    
# This function counts the number of times each node has an event and prints the data
def nodeEvents():

    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
    
        nodeList = {} #dictionary for the nodes
        nodeList1 = nodeList #copy of dictionary
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
        
            node = lineList[0] #calls the node portion of the list
        
                
            if node in nodeList:
                nodeList1[node] += 1  #if event is in the dict it adds the event

            else:
                nodeList1[node] = 1 #creates dict value if none present


        #print(nodeList)
                 
        for key, value in nodeList.items(): #prints the nodes and number of events from the list
            print(key, value)
            
            # This function stores the unique IP address's from the node events and counts them
def uniqueIP():
    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
        ipList = {} # dictionary for storing the unique ip addresses
    
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
            IP = lineList[1] #identifies the IP address in the string
        
            ipSplit = IP.split(".") #splits the ip address into octets
        
            firstO = ipSplit[0] #identify first octet
            secondO = ipSplit[1] #identify second octet
        
        
            #print(IP) test
        
            if len(firstO) == 3: #check first octet length
                
                if len(secondO) == 3: #check second octet length
                
                    if IP in ipList: #IP is in dictionary skip it
                        continue
                    else:
                        ipList[IP] = IP #if the IP isnt in dict then add it
                    #print(ipList)
            
        for key, value in ipList.items(): #print the dictionary list of keys (IP's) only
            print(key)
            
        print("Total number of unique IP Addresses is ", "\n", len(ipList)) #print the length (number of IP's) of the dictionary
        
        for key, value in ipList.items():
            IPAddressID = key
            IPAddressText = value
    
    #create a cursor from the CONNECTION
            cursor = CONNECTION.cursor()
    #execute a SQL statement to insert a new Assignment record based on the title and description entered by the user
            cursor.execute('INSERT INTO IPAddress (IPAddressID,IPAddressText) VALUES (?,?)', (IPAddressID, IPAddressText))
    #commit the delete to the database
            CONNECTION.commit()
    #close the cursor object
            cursor.close()
        
        # This function asks for an octet value and searches all the Address's first and last octets for the value
def octetSearch():
    
    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
    
        ipParm = input("Enter an octet value for an IP address. \n") #input search value
    
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
        
            IP = lineList[1] #identifies the IP address in the string
            ipSplit = IP.split(".") #splits the ip address into octets
        
            firstO = ipSplit[0] #identifies first octet
            lastO = ipSplit[3]  #identifies last octet
        
            if firstO == ipParm: #if first octet = the value entered print it
                print(IP)
            
            if lastO == ipParm:  #if last octet = the value entered print it
                print(IP)
            
            #anything that doesnt match the value entered isnt printed
            
            
            # This function stores and saves all IP address's with unique first octets and counts how many times each is seen
def uniqueFirst():
    
    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
    
        ipAdd = {} #dictionary for storing the First octet values
    
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
            IP = lineList[1] #identifies the IP address in the string
            ipSplit = IP.split(".") #splits the ip address into octets
        
            firstO = ipSplit[0] #identifies the first octet value
            
            if firstO in ipAdd: #if octet is already in list add 1 to count
                ipAdd[firstO] += 1
            
            else: #if octet isnt in the list add it with a count of 1
                ipAdd[firstO] = 1
                
        for key, value in ipAdd.items(): #prints the First Octet value and the number
            print(key, value)            #of times it is seen in the list
    
    #print(len(ipAdd),"unique first octets found.")  (test)  #prints total number of unique first octets
    
    
    #this Function sorts the data for all unique Events associated with the node's and stores and prints them.
def uniqueEvents():
    
    with open("Applog.txt","r") as myFile: #open the text file
    
        lines = myFile.readlines()  #read the file line for line
        eventMsgs = {}
        for line in lines: #searches line for line to iterate through the list
        
            lineList = line.split(" - ") #splits the list into sections
        
            event = lineList[2]
        
            if event in eventMsgs: #if event is already in list skip it
                continue
            
            else: #if octet isnt in the list add it with a count of 1
                eventMsgs[event] = 1
            
        for key, value in eventMsgs.items(): #print the dictionary list of keys which is the unique event messages
            print(key)
        
        for key, value in eventMsgs.items():
            MessageText = key
            MessageOccurance = value
    
    #create a cursor from the CONNECTION
            cursor = CONNECTION.cursor()
    #execute a SQL statement to insert a new Assignment record based on the title and description entered by the user
            cursor.execute('INSERT INTO EventMessage (MessageText,MessageOccurance) VALUES (?,?)', (MessageText, MessageOccurance))
    #commit the delete to the database
            CONNECTION.commit()
    #close the cursor object
            cursor.close()
            
def showMenu():
    selection = ""
    while selection != "7":
        print("\n*************MENU*************")
        print("1 - Print node with most failed Payments.")
        print("2 - Print total number of events for each node.")
        print("3 - Print and Save list and total number of unique IP addresses.")
        print("4 - Search for octet value.")
        print("5 - Print list and index of unique first octets.")
        print("6 - Print and Save list of unique node events.")
        print("7 - Quit")
        print("")
        selection = input("Please enter a menu number: ")
        
        if selection == "1":
            failedPayments()
        if selection == "2":
            nodeEvents()
        if selection == "3":
            uniqueIP()
        if selection == "4":
            octetSearch()
        if selection == "5":
            uniqueFirst()
        if selection == "6":
            uniqueEvents()
        if selection == "7":
            CONNECTION.close()    