import sys
n = int(input())
cards = set(map(int, sys.stdin.readline().split()))
m = int(input())

for num in map(int,sys.stdin.readline().split()):
    if num in cards: print(1,end=' ')
    else: print(0,end=' ')