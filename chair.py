s=input()
res=0
avail=0
for i in s:
    if i in ['C','U']:
        if avail>0:
            avail-=1
        else:
            res+=1
    elif i in ['R','L']:
        avail+=1
print(res)
