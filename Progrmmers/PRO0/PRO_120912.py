def solution(array):
    return sum(str(num).count('7') for num in array)

print(solution([7,77,17]))
print(solution([10,29]))