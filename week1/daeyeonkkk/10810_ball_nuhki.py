N, M = map(int, input().split())
bucket = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for num in range(i-1, j):
        bucket[num] = k
print(*bucket)

