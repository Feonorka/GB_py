a=[]
b=[]
n=int(input())
m=int(input())
for i in range(n):
    c=input()
    a.append(c)
    print(a)
for i in range(m):
    c=input()
    b.append(c)
    print(b)
c=a+b
print(c)
v=set(c)
print(v)
c=list(v)
k=sorted(c)
print(k)