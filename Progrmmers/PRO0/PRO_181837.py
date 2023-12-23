def solution(order):
    return sum(5000 if i.find("hot") >= 0 else 4500 for i in order)

print(solution(["cafelatte", "americanoice", "hotcafelatte", "anything"]))
print(solution(["americanoice", "americano", "iceamericano"]))