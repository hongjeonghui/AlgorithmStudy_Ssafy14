A, B, V = map(int, input().split())
move = A-B
goal = V-1
print(goal + (move-1) // move + 1)
