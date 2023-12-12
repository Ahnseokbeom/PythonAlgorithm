n = int(input())
numbers = [int(input()) for _ in range(n)]

sort_num = sorted(numbers)
for num in sort_num:
    print(num)