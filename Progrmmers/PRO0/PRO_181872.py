def solution(myString, pat):
    return myString[:myString.rfind(pat)+len(pat)]

print(solution("AbCdEFG","dE"))
print(solution("AAAAaaaa","a"))