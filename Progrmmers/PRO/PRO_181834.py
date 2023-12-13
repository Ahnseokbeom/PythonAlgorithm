import re
def solution(myString):
    return re.sub(r'[a-k]','l',myString)

print(solution("abcdevwxyz"))
print(solution("jjnnllkkmm"))
