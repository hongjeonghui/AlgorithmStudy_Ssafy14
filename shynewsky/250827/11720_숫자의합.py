import sys
sys.stdin = open('input.txt')

N = int(input())
arr = map(int, input().strip())
print(sum(arr))
