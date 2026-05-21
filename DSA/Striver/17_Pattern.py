"""
   A
  ABA
 ABCBA
ABCDCBA
"""
#IMPORTANT
N = int(input("Input Size: "))
for i in range(N):
    for j in range(N-i-1):
        print(" ",end="")
    for k in range(i+1):
        print(chr(65+k),end="")
    for l in range(i-1,-1,-1):
        print(chr(65+l),end="")
    print()
