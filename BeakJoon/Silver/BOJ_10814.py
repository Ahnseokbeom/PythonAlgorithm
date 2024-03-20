n = int(input())

members = []
for _ in range(n):
    age, name = input().split()
    members.append([int(age), name])

for member in sorted(members,key=lambda x : x[0]):
    print(member[0],member[1])
