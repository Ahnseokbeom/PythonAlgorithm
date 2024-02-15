def solution(order):
    answer = 0
    for digit in str(order):
        print(digit)
        if digit in ['3','6','9']:
            answer+=1
    return answer

print(solution(3))
print(solution(29423))