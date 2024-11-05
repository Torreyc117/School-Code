aboutMyMacDictionary = {"Model":"Macbook pro","Processor":"2.4 GHz 9-core", "Memory":"16 GB"}
myMacD = str(aboutMyMacDictionary)
myMac = myMacD.replace(",","\n")
myMac = myMac.replace("{","")
myMac = myMac.replace("}","")

#open a file to add the dictionary to (as a string)
with open("aboutmymac.txt","w") as myFile:
    myFile.write(str(myMac))

try: #try to read the file printing the items as key and value
    with open("aboutmymac.txt","r") as myFile:
        print(myFile.read())
        
    
except Exception as e: #if it fails, print an error occured
    print("An error has occured.")
