def solution(arr):
    answer = [i for i, num in enumerate(arr) if num==2]
    if len(answer) < 1:
        return [-1]
    return arr[min(answer):max(answer)+1]

print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1,2,1]))
print(solution([1,1,1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))