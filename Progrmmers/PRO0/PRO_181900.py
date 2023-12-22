def solution(my_string, indices):
    return ''.join([my_string[i] for i in range(len(my_string)) if i not in indices])

print(solution("apporoograpemmemprs",[1, 16, 6, 15, 0, 10, 11, 3]))