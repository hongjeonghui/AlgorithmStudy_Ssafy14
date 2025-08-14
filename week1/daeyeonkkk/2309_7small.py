height = [int(input()) for _ in range(9)]
h_sum = 0
complete = 0
for h in height:
    h_sum += h                                   # 싹 다 더하기

fake_small = h_sum - 100                         # - 100 하면 가짜 두명의 합임

for i in range(8):                               # 최대길이 -1번 반복
    if not complete:                             # 종료조건
        for j in range(i+1, 9):                  # i 다음~ 리스트 끝까지 반복
            if height[i] + height[j] == fake_small:  # 두개 더했을 때 fake_small 나오는 인덱스 찾아서
                fake_small_a = height[i]         # 두고보자
                fake_small_b = height[j]
                complete = 1                     # 찾았으니까 그만돌자
                break

height.remove(fake_small_a)                      # 찾은애들 제거하기
height.remove(fake_small_b)
height.sort()                                    # 오름차순 정렬
for h in height:                                 # 한줄씩 출력
    print(h)
