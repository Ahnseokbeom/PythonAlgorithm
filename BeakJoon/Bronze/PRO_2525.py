a,b = map(int,input().split())
c = int(input())
b += c
if b>=60:
    a+=int(b/60)
    if a>=24: a-=24
    b%=60
print("{0} {1}".format(a,b))