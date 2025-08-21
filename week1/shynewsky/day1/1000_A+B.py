# map() 을 사용하여 언패킹할때, list()를 사용하든 안하든 동작은 똑같이 한다
# 메모리사용량과 속도도 똑같다

#방1
a, b = map(int, input().split())
print(a+b)

#방2
a, b = list(map(int, input().split()))
print(a+b)
