def solution(ineq, eq, n, m):
    if eq=="!":
        if ineq==">":
            return int(n>m)
        else: return int(n<m)
    else:
        if ineq==">":
            return int(n>=m)
        else: return int(n<=m)
    return 0

print(solution("<","=",20,50))
print(solution(">","!",41,78))