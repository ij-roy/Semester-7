"""
    * 
   ***
  *****
 *******
*********
"""

N = int(input("Input Size: "))
for i in range(N,-1,-1):
    for j in range(i):
        print(" ",end="")
    for k in range((N-i)*2 - 1):
        print("*",end="")
    print()