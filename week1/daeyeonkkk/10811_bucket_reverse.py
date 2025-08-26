N, M = map(int, input().split())
bucket = []
for num in range(1, N+1):
    bucket.append(num)
for _ in range(M):
    i, j = map(int, input().split())
    bucket[i-1:j] = reversed(bucket[i-1:j])
print(*bucket)