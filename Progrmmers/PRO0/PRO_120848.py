from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

print(solution(3628800))
print(solution(7))