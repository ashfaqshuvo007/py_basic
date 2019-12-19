#list c
c = [250,20,20,98,3,4]

#create sum of items in list
def sum(c):
    sumNum = 0
    for x in c:
        sumNum += x
    return sumNum


print(sum(c))