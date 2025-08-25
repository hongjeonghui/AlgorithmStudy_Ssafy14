max_num = 1
for i in range(1, 10):
    input_val = int(input())
    if input_val > max_num:
        max_num = input_val
        max_index = i
print(f'{max_num}\n{max_index}')
