def solution(picture, k):
	answer = []
	for r in picture:
		str = ''
		for c in r:
			str += c*k
		for _ in range(k):
			answer.append(str)
	return answer
