c=[int(x) for x in input().split()]
n,m=c[0],c[1]
m1=[]
m2=[]
print('First Matrix:')
for i in range(n):
    l=[int(x) for x in input().split()]
    print(*l)
    m1.append(l)
print('Second Matrix:')
for i in range(n):
    l=[int(x) for x in input().split()]
    print(*l)
    m2.append(l)
res=[]
print('Sum of the two matrices is:')
for i in range(n):
    l=[]
    for j in range(n):
        l.append(m1[i][j]+m2[i][j])
    print(*l)
