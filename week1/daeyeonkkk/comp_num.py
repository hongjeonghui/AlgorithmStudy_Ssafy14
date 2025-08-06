A ,B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('=')


# A, B = map(int, input().split())                  # 삼항 연산자
# print('>' if A > B else '<' if A < B else '=')

# A, B = map(int, input().split())                  # 딕셔너리 비교 연산
# print({1: '>', -1: '<', 0: '='}[(A > B) - (A < B)])

# A, B = map(int, input().split())                  # match-case
# match (A > B, A < B):
#     case (True, False):
#         print('>')
#     case (False, True):
#         print('<')
#     case _:
#         print('=')

