"""
A
BB
CCC
DDDD
EEEEE
"""
N = int(input("Input Size: "))
num = 65
for i in range(N):
    for j in range(i+1):
        print(chr(num),end="")
    print()
    num+=1
