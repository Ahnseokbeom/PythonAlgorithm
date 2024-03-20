word = input()
positions = {chr(i): -1 for i in range(ord('a'), ord('z') + 1)}

for idx, char in enumerate(word):
    if positions[char] == -1:
        positions[char] = idx

print(*positions.values())