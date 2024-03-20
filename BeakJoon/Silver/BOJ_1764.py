import sys
n,m = map(int, sys.stdin.readline().split())
not_heard = set()
not_seen = set()

for _ in range(n):
    not_heard.add(sys.stdin.readline().strip())

for _ in range(m):
    not_seen.add(sys.stdin.readline().strip())

member = sorted(not_heard.member(not_seen))

print(len(member))
for person in member:
    print(person)
