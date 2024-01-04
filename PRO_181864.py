def solution(myString, pat):
    return 1 if pat in myString.replace("A", "t").replace("B", "A").replace("t", "B") else 0

print(solution("ABBAA","AABB"))
print(solution("ABAB","ABAB"))