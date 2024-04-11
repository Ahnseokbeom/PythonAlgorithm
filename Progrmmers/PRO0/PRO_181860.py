def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            length = arr[i]*2
            answer.extend([arr[i]]*length)
        else:
            answer = answer[:-arr[i]]
    return answer

print(solution([3,2,4,1,3],[True,False,True,False,False]))