def solution(myString, pat):
    return sum(myString[i:i + len(pat)] == pat for i in range(len(myString)))

print(solution("banana","ana"))
print(solution("aaaa","aa"))
