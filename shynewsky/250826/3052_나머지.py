import sys
sys.stdin = open('input.txt')

arr = [int(input()) for _ in range(10)]
arr1 = set([i % 42 for i in arr])
print(len(arr1))
