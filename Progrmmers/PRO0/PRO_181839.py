def solution(a, b):
    answer = 0
    if a%2==1 and b%2==1:
        return pow(a,2)+pow(b,2)
    elif a%2==0 and b%2==0:
        return abs(a-b)
    return 2*(a+b)

print(solution(3,5))
print(solution(6,1))
print(solution(2,4))