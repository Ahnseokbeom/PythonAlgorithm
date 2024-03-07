a,b = map(int,input().split())
print(str(a)[::-1] if str(a)[::-1]>str(b)[::-1] else str(b)[::-1])