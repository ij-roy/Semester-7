"""
ABCDE
ABCD
ABC
AB
A
"""
N = int(input("Input Size: "))
for i in range(N,-1,-1):
    for j in range(i):
        print(chr(j+65),end="")
    print()
    
