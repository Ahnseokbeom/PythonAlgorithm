def solution(food):
    answer = ""
    left = ""
    right = ""
    for i in range(1, len(food)):
        if food[i] != 0:
            for j in range(food[i] // 2):
                left += str(i)
                right = str(i) + right

    answer = left + "0" + right
    return answer
