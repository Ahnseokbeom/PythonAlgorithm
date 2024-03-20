x = int(input())
n = int(input())
total = 0
for _ in range(0,n):
    a,b = map(int,input().split())
    total += a*b
print('Yes' if x==total else 'No')