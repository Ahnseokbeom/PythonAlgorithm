# 정답 1
from datetime import datetime
def solution(date1, date2):
    answer = 0
    return int(datetime(date1[0],date1[1],date1[2]) < datetime(date2[0],date2[1],date2[2]))

print(solution([2021,12,28],[2021,12,29]))
print(solution([1024,10,24],[1024,10,24]))

# 정답 2
def solution2(date1, date2):
    return int(date1 < date2)

print(solution2([2021,12,28],[2021,12,29]))
print(solution2([1024,10,24],[1024,10,24]))
