def countLetters(listParm):
    d = {} #empty directory
  
    letter = [x for x in str(listParm) if x.isalpha()] #converts list into a string without punctuation
    
    letter.sort() #sorts list alphabetically
    
    
    for items in letter: #checks if letter is in the dictionary if not 
    #it is added with a counter for every instance of the letter
        d[items] = d.get(items, 0) + 1
    
    
    for key, value in d.items(): #prints the dictionary list
        print(key, value) 