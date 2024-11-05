#to do: parse/evaluate the filename extension string by
#getting all characters to the right of the "."
#to do: return the filename extension string.
extensionList = []
def parseExtension(fileName):
        extensionParm = fileName.split(".")[1]
        extensionList.append(extensionParm)
        print(extensionList)
    
#fileName = input("please enter a File Name: \n")
# parseExtension(fileName)

def fileExtensionExists(fileList, fileExtension):
    for fileName in fileList:
        
        parseExtension(fileName)
        
        if fileExtension in extensionList:
            return True
           
    return False