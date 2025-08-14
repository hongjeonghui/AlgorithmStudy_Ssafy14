arr = [int(input()) for _ in range(9)]

total = sum(arr)  # 총합
target = total - 100  # 두명 합 (일곱난쟁이에 포함되지 못한)

idx1 = -1
idx2 = -1
found = False

for i in range(8, -1, -1):  
    for j in range(i):
        if arr[i] + arr[j] == target: 
            idx1, idx2 = i, j
            found = True
            break
    if found:
        break

result = []
for k, n in enumerate(arr):
    if k not in (idx1, idx2):
        result.append(n)

result.sort()
for n in result:
    print(n)
