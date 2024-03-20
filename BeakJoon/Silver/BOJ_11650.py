import sys
n = int(input())
n_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    n_list.append((x,y))
n_list.sort()

for num in n_list:
    print(num[0],num[1])
