number = '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'
x,b = map(str, input().split())
x = x[::-1]
answer = 0
for i in range(len(x)):
    answer += (int(b)**i)*number.index(x[i])
print(answer)