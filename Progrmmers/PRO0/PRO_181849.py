def solution(num_str):
    return sum(int(num) for num in num_str)

print(solution("123456789"))
print(solution("100000"))