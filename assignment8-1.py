#rainbow function
import createRainbow
#hashing 
import hashlib

passW = input("Enter your Password: \n")

# 1) encode the string
passW = passW.encode("utf-8")

# 2) create hash object
myHash = hashlib.md5(passW)

# 3) generate the hash string
myHashString = myHash.hexdigest()

#open a file
myFile = open("pswd2.txt","a")

#write the password to the file
myFile.write("\n")
myFile.write(myHashString)

#close the file
myFile.close()