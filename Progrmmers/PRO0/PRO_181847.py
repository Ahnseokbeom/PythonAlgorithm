# solve 1
def solution1(n_str):
    return n_str.lstrip('0')

print(solution1("0010"))
print(solution1("854020"))

# solve 2
def solution2(n_str):
    return str(int(n_str))

print(solution2("0010"))
print(solution2("854020"))