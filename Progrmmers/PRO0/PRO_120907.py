def solution(quiz):
     return ["O" if eval(eq.replace('=','==')) else "X" for eq in quiz]
 
print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))