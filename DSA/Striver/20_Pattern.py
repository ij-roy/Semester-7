"""
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""
N = int(input("Input Size: "))
for i in range(N-1,-1,-1):
    for j in range(N-i):
        print("*",end="")
    for l in range(2*i):
        print(" ",end="")
    for k in range(N-i):
        print("*",end="")
    print()
for i in range(1,N):
    for j in range(N-i):
        print("*",end="")
    for l in range(2*i):
        print(" ",end="")
    for k in range(N-i):
        print("*",end="")
    print()