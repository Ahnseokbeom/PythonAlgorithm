def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    x, y = 0, 0
    direction_index = 0
    
    for num in range(1, n*n + 1):
        answer[x][y] = num
        dx, dy = directions[direction_index]
        nx, ny = x + dx, y + dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            direction_index = (direction_index + 1) % 4
            dx, dy = directions[direction_index]
            nx, ny = x + dx, y + dy
        
        x, y = nx, ny
    
    return answer

print(solution(4))
print(solution(5))