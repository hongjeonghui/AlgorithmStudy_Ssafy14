N, K = map(int, input().split())
student = []
student_dict = {}
room = 0

for _ in range(N):
    student.append(''.join(input().split()))
    # student.append(input().replace(' ',''))
for stu in student:
    if stu in student_dict:
        student_dict[stu] += 1
    else:
        student_dict[stu] = 1

for stu in student_dict:
    if student_dict.get(stu) % K == 0:
        room += student_dict.get(stu) // K
    else:
        room += (student_dict.get(stu) // K) + 1

print(room)
