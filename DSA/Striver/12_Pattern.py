"""
1      1
12    21
123  321
12344321
"""
N = int(input("Input Size: "))
for i in range(N):
    for j in range(N):
        print(j+1 if j<=i else " ",end="")
    for j in range(N-1,-1,-1):
        print(j+1 if j<=i else " ",end="")
    print()
    
    