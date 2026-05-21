"""
A
AB
ABC
ABCD
ABCDE
"""
N = int(input("Input Size: "))
for i in range(N):
    for j in range(i+1):
        print(chr(j+65),end="")
    print()
    
    