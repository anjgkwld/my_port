d=1
a,b,c=map(int, input().split())

while True:
          if d%a==0 and d%b==0 and d%c==0:
                    break
          d+=1

print(d)
