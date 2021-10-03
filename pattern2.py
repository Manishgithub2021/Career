"""
*****
****
***
**
*
"""

def patternstar(no_of_row):
    for y in range(no_of_row,0,-1):
        for x in range(no_of_row,no_of_row-y,-1):
            print("* ",end="")
        print()
def patternnumber(no_of_row):
    for y in range(0,no_of_row):
        for x in range(0,no_of_row-y):
            print(f"{x+1} ",end="")
        print()
def patternnumbercontinuous(no_of_row):
    counter=0
    for y in range(0,no_of_row):
        for x in range(0,no_of_row-y):
            counter+=1
            print(f"{counter} ",end="")
        print()
patternstar(5)
patternnumber(5)
patternnumbercontinuous(5)
