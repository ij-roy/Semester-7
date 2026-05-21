"""
****
*  *
*  *
****
"""
N = int(input("Input Size: "))
for i in range(N):
    for j in range(N):
        print("*" if i==0 or j==0 or i == N-1 or j == N-1 else " ",end="")
    print()