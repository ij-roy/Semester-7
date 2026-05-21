"""
*
**
***
****
*****
"""

N = int(input("Input Size: "))
for i in range(N+1):
    for j in range(i):
        print("*",end="")
    print()