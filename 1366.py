n=int(input())

for i in range(0,n):
    for j in range(0,n):
        if(i==n//2 or j==n//2 or i==0 or i==n-1 or j==0 or j==n-1 or i==j or n-1-j==i):
            print('*',end='')
        else:
            print(' ',end='')
    print()
