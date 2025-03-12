n=int(input())
l=[int(x) for x in input().split()]
s=set()
f=0
for i in l:
    if i in s:
        print('true')
        f=1
        break
    else:
        s.add(i)
if not f:
    print('false')
