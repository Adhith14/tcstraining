n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
c=0
for i in l:
    if i%2!=0:
        c+=1
if c==0:
    print('No odd elements are present')
else:
    print(f'Odd Elements: {c}')
