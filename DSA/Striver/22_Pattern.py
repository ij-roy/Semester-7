"""
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5 
5 4 3 3 3 3 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 2 1 2 3 4 5 
5 4 3 2 2 2 3 4 5 
5 4 3 3 3 3 3 4 5 
5 4 4 4 4 4 4 4 5 
5 5 5 5 5 5 5 5 5
"""
N = int(input("Input Size: "))
for i in range(N,0,-1):
    for j in range(N,0,-1):
        print(max(i,j),end=" ")
    for k in range(2,N+1):
        print(max(i,k),end=" ")
    print()
for i in range(2,N+1):
    for j in range(N,0,-1):
        print(max(i,j),end=" ")
    for k in range(2,N+1):
        print(max(i,k),end=" ")
    print()