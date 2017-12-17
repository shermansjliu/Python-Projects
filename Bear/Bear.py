file_object = open("bears.dat","r")

bearNum = 0
for line in file_object:
    lineArr = list(line)
    for char in lineArr:
        if char == "B":
            bearNum += 1
print(bearNum)



#for eveery line in the file object
#split the each line into an array of characters
#for every character check if it is a B
#increase bear count by 1