n=int(input())
avg=0
t=n
while t:
    avg+=float(input())
    t-=1
avg=avg/n
print(f'The average is: {avg:.3f}')
