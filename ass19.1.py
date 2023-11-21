# Write a program to separate even on oneside and odd numbers on another side.

n=int(input())
l=list(map(int,input().split()))
o=[]
e=[]
for i in l:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
res=e+o
for i in res:
    print(i,end=' ')
    
