"""
1
01
101
0101
10101
"""
N = int(input("Input Size: "))
for i in range(N):
    for j in range(i+1):
        print(f"{((i+j+1)%2)}",end="")
    print()