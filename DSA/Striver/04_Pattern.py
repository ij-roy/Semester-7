"""
1
22
333
4444
55555
"""

N = int(input("Input Size: "))
num = 1
for i in range(N):
    for j in range(i+1):
        print(f"{num}",end="")
    print()
    num+=1