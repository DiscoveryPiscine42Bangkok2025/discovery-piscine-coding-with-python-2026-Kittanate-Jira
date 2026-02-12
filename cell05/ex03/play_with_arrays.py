original_array = [2, 8, 9, 48, 8, 22, -12, 2]

temp_list = []

for number in original_array:

    if number > 5:

        temp_list.append(number + 2)

new_set = set(temp_list)

print(original_array)
print(new_set)