import sys
n = int(input())
n_list = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    n_list.append((x,y))
n_list.sort(key=lambda num : (num[1],num[0]))

for num in n_list:
    print(num[0],num[1])
