t = int(input())

for _ in range(t):
    r,s = input().split()
    print(''.join([char * int(r) for char in s]))