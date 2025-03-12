n=int(input())
f=0
for i in range(2,n//2):
    if n%i==0:
        f=1
        break
if f:
    print(f'{n} is not a prime number')
else:
    print(f'{n} is a prime number')
