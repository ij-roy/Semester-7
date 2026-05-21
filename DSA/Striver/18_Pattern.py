"""
E
D E
C D E
B C D E
A B C D E
"""
N = int(input("Input Size: "))
for i in range(N):
    for j in range(i+1):
        print(chr(65+N+j-i-1),end=" ")
    print()
