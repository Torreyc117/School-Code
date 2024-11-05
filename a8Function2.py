import hashlib

def createRainbow(fileParm):
    
    
    with open (fileParm,"r", encoding = "ISO-8859-1") as myFile:
    #open the text file to read    
        
        
        for line in myFile.readlines():
            #read the file line by line
            
            line = line.encode("utf-8")
            #encode the string
            
            myHash = hashlib.md5(line)
            #create hash object
            
            myHashString = myHash.hexdigest()
            #generate string
            
            myFile = open("englishRainbow.txt","a")
            #open text file to print hashes to
            
            myFile.write("\n")
            #new line
            
            myFile.write(myHashString)
            #print hash string
