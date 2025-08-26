N = int(input())
scores = list(map(int, input().split()))
sum_score = 0
max_score = max(scores)
for score in scores:
    sum_score += score/max_score*100
print(sum_score/len(scores))