def solution(strArr):
    return [i for i in strArr if "ad" not in i]

print(solution(["and","notad","abcd"]))
print(solution(["there","are","no","a","ds"]))