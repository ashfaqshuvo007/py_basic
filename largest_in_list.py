# Find the largest number in a list

#list c
c = [250,20,20,98,3,4]

#create sum of items in list
def largest_in_list(l):
    largestNum = l[0]
    for x in l:
        if  x > largestNum:
            largestNum  = x
    return largestNum
print(largest_in_list(c))