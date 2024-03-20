n_list = []
for _ in range(5):
    n_list.append(int(input()))
    
print(int(sum(n_list)/5))
print(sorted(n_list)[2])