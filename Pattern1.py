"""
*
**
***
****
*****
"""

def patternstar(no_of_row):
    for x in range(no_of_row):
        for i in range(0,x+1):
            print("* ",end="")
        print()
def patternnumber(no_of_row):
    for x in range(no_of_row):
        for i in range(0,x+1):
            print(f"{i+1} ",end="")
        print()
def patternnumbercontinuous(no_of_row):
    counter=0
    for x in range(no_of_row):
        for i in range(0,x+1):
            counter=counter+1
            print(f"{counter} ",end="")
        print()

patternstar(5)
print()
print("*"*20)
patternnumber(5)
print()
print("*"*20)
patternnumbercontinuous(5)