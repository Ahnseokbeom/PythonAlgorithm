def solution(l, r):
	return [num for num in range(l, r + 1) if all(d in {'0', '5'} for d in str(num))] or [-1]

print(solution(5,555))
print(solution(10,20))
