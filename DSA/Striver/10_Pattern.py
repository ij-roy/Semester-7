"""
*
**
***
****
***
**
*
"""
N = int(input("Input Size: "))
for i in range(N-1):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(N-1,-1,-1):
    for j in range(i+1):
        print("*",end="")
    print()   