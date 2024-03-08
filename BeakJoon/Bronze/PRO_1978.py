n = int(input())
n_list = list(map(int,input().split()))
answer = 0

for i in n_list:
    if i == 1:
        continue
    for j in range(2,i):
        if i%j==0: break
    else: answer+=1

print(answer)
