"""
1
12
123
1234
12345
"""

N = int(input("Input Size: "))
for i in range(N):
    for j in range(i+1):
        print(f"{1+j}",end="")
    print()