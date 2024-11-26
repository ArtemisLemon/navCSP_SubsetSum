import math

#python graphdata.py >> graphdata
def numberOfElements(x,y):
    if y==0:
        return 0
    return numberOfElements(x,y-1)+x**(1+y)

for i in range(1,21):
    for j in range(1,21):
        out = numberOfElements(i,j)
        print("({},{},{}) ".format(i,j, out),end="")
    print("")
    print("")