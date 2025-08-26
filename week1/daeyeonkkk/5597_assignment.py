student = []
for i in range(1, 31):
    student.append(i)
for _ in range(28):
    student.remove(int(input()))
student.sort()
print(f'{student[0]}\n{student[1]}')
