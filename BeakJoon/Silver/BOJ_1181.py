import sys
n = int(input())
word_set = set()

for _ in range(n):
    word = sys.stdin.readline().strip()
    word_set.add(word)

sorted_words = sorted(word_set, key=lambda s: (len(s), s))

for word in sorted_words:
    print(word)