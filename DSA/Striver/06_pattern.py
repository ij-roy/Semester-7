"""
12345
1234
123
12
1
"""

N = int(input("Input Size: "))
for i in range(N,-1,-1):
    for j in range(i):
        print(f"{j+1}",end="")
    print()