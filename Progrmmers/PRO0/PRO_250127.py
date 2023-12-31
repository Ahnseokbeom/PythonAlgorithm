def func1(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else: return 5
    
def func2(humidity, val_set):
    return 3 if humidity < val_set else 1


def func3(humidity, val_set):
    return int(humidity < val_set)


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func1(humidity)

    elif mode_type == "target":
        answer = func2(humidity, val_set)

    elif mode_type == "minimum":
        answer = func3(humidity,val_set)

    return answer

print(solution("auto",23,45))
print(solution("target",41,40))
print(solution("minimum",10,34))