# Write a program to store odd numbers in the list using list comrehension.

n=int(input())
l=[i for i in range(1,n+1) if i%2!=0]
print(l)
