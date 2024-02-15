import math
def solution(slice, n):
    return math.ceil(n/slice)

print(solution(7,2))
print(solution(4,12))