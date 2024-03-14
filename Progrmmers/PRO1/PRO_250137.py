def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    end_time = attacks[-1][0]
    attacks = {attack[0]:attack[1] for attack in attacks}
    
    cur_t = 0
    answer = health
    
    for i in range(end_time + 1):
        if i in attacks:
            cur_t = 0
            answer -= attacks[i]
            if answer <= 0:
                return -1
            continue
            
        cur_t += 1
        answer += x
        
        if cur_t == t:
            answer += y
            cur_t = 0
            
        answer = min(answer, max_health)
    
    return answer

print(solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
print(solution([1, 1, 1],5,[[1, 2], [3, 2]]))