#Multiply the numbers in a list.

#list c
c = [250,20,20,98,3,4]

#create sum of items in list
def multi(c):
    multiNum = 1
    for x in c:
        multiNum *= x
    return multiNum


print(multi(c))