def solution(my_string):
    return sorted([int(char) for char in my_string if char.isdigit()])

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))