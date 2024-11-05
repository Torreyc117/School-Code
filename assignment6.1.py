aboutMyMacDictionary = {"Model":"Macbook pro","Processor":"2.4 GHz 9-core", "Memory":"16 GB"}

#to do 1
#add key "Graphics" with value "Radeon Pro 555x 4 GB"

aboutMyMacDictionary["Graphics"] = "Radeon Pro 555x 4 GB"
#to do 2
#add key "Seriel Number" with value "XSD123WD56Z"

aboutMyMacDictionary["Seriel Number"] = "XSD123WD56Z"

#to do 3
#Change value for key "Memory" to value "32 GB"

aboutMyMacDictionary["Memory"] = "32GB"

#to do 4
#Change value for key "Model" to "Macbook Air"

aboutMyMacDictionary["Model"] = "Macbook Air"

#to do 5
#Use a for loop to change each dictionary value to upper case

for item in aboutMyMacDictionary:
    aboutMyMacDictionary[item] = aboutMyMacDictionary[item].upper()
    print(aboutMyMacDictionary[item])

#to Do 6
#Use a for loop to print each key and value.   Output must be in the form of key " - " value.  For example:
# Model - Mackbook Air 

aboutMyMacDictionaryItems = aboutMyMacDictionary.items()

print(aboutMyMacDictionaryItems)

for key, value in aboutMyMacDictionaryItems:
    print(key, "-", value)