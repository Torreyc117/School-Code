from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

#http request to a site
resp = urllib.request.urlopen("http://ec2-3-92-65-134.compute-1.amazonaws.com/www.ferris.edu/online/future-students/index.html")
print(type(resp))

print(resp.status)

#print(resp.headers)

#examining html obhects . tags such img, a, etc...

soup = BeautifulSoup(resp, "html.parser")

tags = soup("a") #links

for item in tags: #Ferris Links
    
    with open("ferrislinks.txt","a") as myFile: #create ferris links text file
        
        myFile.write("\n")
        
        myFile.write(item.get('href',None))

for item in tags: #nursing links
   
    if "nursing" in str(item).lower(): #search for nursing in the list of links
    
        with open ("nursing.txt","a") as myFile: #create/open nursing text file
        
            myFile.write("\n")
            
            myFile.write(item.get('href',None))
            
tags = soup("img") #images

for item in tags: #ferris images
    
    with open("ferrisimages.txt","a") as myFile: # create/open image file
        
        myFile.write("\n")
        
        myFile.write(item.get('src',None))

for item in tags:  #nursing images
   
    if "nursing" in str(item).lower(): #search for nursing in list of images
    
        with open ("nursing.txt","a") as myFile: #open nursing file
        
            myFile.write("\n") #add new line
            
            myFile.write(item.get('src',None)) #print image link
            
