# solve 1
def solution1(my_string, m, c):
    return ''.join(my_string[i] for i in range(c-1, len(my_string), m))

print(solution1("ihrhbakrfpndopljhygc",4,2))
print(solution1("programmers",1,1))

# solve 2
def solution2(my_string, m, c):
    return my_string[c-1::m]

print(solution2("ihrhbakrfpndopljhygc",4,2))
print(solution2("programmers",1,1))