def solution(n):
    prime = set()
    div = 2
    while n!=1:
        if n % div == 0:
            prime.add(div)
            n //= div
        else: div+=1
    answer = sorted(list(prime))
    return answer

print(solution(12))
print(solution(17))
print(solution(420))