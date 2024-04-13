def solution(array, n):
    closest = None
    min_diff = float('inf')
    
    for num in array:
        diff = abs(num - n)
        if diff < min_diff or (diff == min_diff and num < closest):
            closest = num
            min_diff = diff
    
    return closes

print(solution([3,10,28]))
print(solution([10,11,12]))
