n = int(input())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

print(*sorted(n_list),sep="\n")