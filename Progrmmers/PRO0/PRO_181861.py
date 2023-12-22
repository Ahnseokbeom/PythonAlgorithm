def solution(arr):
    return sum([[a]*a for a in arr],[])

print(solution([5,1,4]))
print(solution([6,6]))
print(solution([1]))