n=int(input())
a=input().split()

for i in range(n-1,-1,-1): ## range범위가 n-1,-1,-1 -> 역순으로 출력하도록 만들어줌
  print(a[i],end=' ')
