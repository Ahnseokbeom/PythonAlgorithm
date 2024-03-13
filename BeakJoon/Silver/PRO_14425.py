import sys
n,m = map(int, sys.stdin.readline().split())
sets = set()
for _ in range(n):
    sets.add(sys.stdin.readline())

answer = 0
for _ in range(m):
    s = sys.stdin.readline()
    if s in sets:
        answer+=1

print(answer)

