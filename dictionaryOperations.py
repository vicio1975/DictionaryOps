# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:35:45 2018

@author: bmusammartanov
"""

thisdict =	{
  "brand": "Fiat",
  "model": "Panda",
  "year": 2014
}

##Show values of the dictionary
print("\nfirst way")
for i in thisdict:
    print(thisdict[i])

print("\nsecond way")
for i,j in thisdict.items():
    print(i,j)

print("\nThird way")
for i in thisdict.values():
    print(i)

##Check if a key exists
key2find = input("\nWhat key are you looking for: ")
key2find = key2find.lower()
if key2find in thisdict:
    print("... {} is in the dictionary".format(key2find))
else: print("... {} is not in the dictionary".format(key2find))

##Dictionary Length
print("\n## Dictionary Length ##")
print("The dictionary has {} keys".format(len(thisdict)))

##Adding Items
print("\nAdding the 'color' key")
thisdict["color"]="red"
print("The new dictionary has {} keys".format(len(thisdict)))
for i,j in thisdict.items():
    print(i,j)

##Removing Items
print("\nRemoving the 'color' key")
thisdict.pop("color")
print("The new dictionary has {} keys".format(len(thisdict)))
for i,j in thisdict.items():
    print(i,j)

print("\nsecond way to remove a key")
thisdict["color"]="red"
del thisdict["color"]
print("The new dictionary has {} keys".format(len(thisdict)))
for i,j in thisdict.items():
    print(i,j)

##Clear the dictionary
print("\nClearing the dictionary")
thisdict.clear()
print(thisdict)

##Build a dictionary
print("\nBuilding a new dictionary")
thisdict2 = dict(brand="Lancia",model="Y",year=2000,color="red")
print(thisdict2)
for i,j in thisdict2.items():
    print(i,j)
thisdict =	{
  "brand": "Fiat",
  "model": "Panda",
  "year": 2014
}

##Merge 2 dictionaries
print("Merging 2 dictionaries:")    
thisdict3 = {**thisdict, **thisdict2}
for i in thisdict3.items():
    print(i)


input("Press a key to close the terminal!")
