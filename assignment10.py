import os
import hashlib

def listFiles(startDirectory):
    fileDirList = os.listdir()
    for name in fileDirList:
        if os.path.isfile(name):
            #print(name + "is a file")
        #else:
            #print(name + "is not a file.")
            
            with open(name,"rb") as myFile: #open file as binary to read
                
                lines = myFile.read() #reads contents of file
                
                myHash = hashlib.md5(lines) #create hash object
                
                myHashString = myHash.hexdigest() #generate hash string
                
                myFile = open("filehashes.txt","a") #open text for file location
                
                myFile.write("\n") #new line between hash's
                
                myFile.write(name + "\t" + myHashString) # prints file name and contents hash with a tab between
                
myPath = "/home/ec2-user/environment/week10/"
listFiles(myPath)