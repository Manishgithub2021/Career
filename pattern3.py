"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
for j in range(0,4):
    for i in range(0,4-j):
        print(" ",end="")
    for _ in range(0,j+1):
        print("*",end=" ")
    print()
