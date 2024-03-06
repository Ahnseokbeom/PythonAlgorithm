dice = list(map(int, input().split()))

if len(set(dice)) == 1:
    answer = 10000 + dice[0] * 1000
elif len(set(dice)) == 2:
    for d in set(dice):
        if dice.count(d) == 2:
            answer = 1000 + d * 100
            break
else: answer = max(dice) * 100

print(answer)