import sys
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

print(*sorted(n_list),sep="\n")
