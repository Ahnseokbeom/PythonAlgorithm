def check_receipt(total_amount, num_items, items):
    calculated_total = 0

    for price, quantity in items:
        calculated_total += price * quantity

    if calculated_total == total_amount:
        return "Yes"
    else:
        return "No"

total_amount = int(input())
num_items = int(input())

items = []
for _ in range(num_items):
    price, quantity = map(int, input().split())
    items.append((price, quantity))

result = check_receipt(total_amount, num_items, items)
print(result)
