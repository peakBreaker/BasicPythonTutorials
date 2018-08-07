# lists and loops

## Lists
myList = [1,5,6,9,10,1234]
print(myList) # debugs out: [1, 5, 6, 9, 10, 1234]

## Lists start at 0
print("first value of myList is %i" % myList[0])

mySum = 0
for value in myList:
    mySum = mySum + value # This can be shortened to mySum+=value

print("Sum of all values in myList is %i" % mySum)
