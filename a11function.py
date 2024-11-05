import urllib.request
import json

def searchCVE(urlParm, phraseParm):
#web request
    resp = urllib.request.urlopen(urlParm)
    data = resp.read() #reads the text and assigns as str to data

#read the data and load a json object
#json validation...
    jsonObj = json.loads(str(data.decode("utf-8")))
    
    

    for item in jsonObj:
        
        #print(item["summary"])
        if "summary" in item.keys(): #check the summary at the top level
        #is the phrase you are searching for in the capec summary ?
            for phraseParm in item.values():
                print(item["id"])
                #print(item["cvss"])
                #print(item["Published"])
                print(item["summary"])
                print("---------------------------------------------------------")
                break
            
        '''if "capec" in item.keys():
                
            if len(item["capec"])> 0:
                    
                for embeddedItem in item["capec"]:
    
                    for phraseParm in item.values():
                        print(item["id"])
                        print(item["cvss"])
                        print(item["Published"])
                        #print(item["summary"])
                        print("---------------------------------------------------------")
                        break'''