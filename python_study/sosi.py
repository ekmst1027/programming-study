

# test_case = input('Number of TestCase>>')
# num_student, num_couple = input('Number of student>>'), input('Number of couple>>')
# back_number = []
test_case = 3
num_student, num_couple = 4, 6
back_number = [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3]
# for i in range(2*int(num_couple)):
#     back_number.append(input('Number of student>>'))

result = {}
for number in back_number:
    if number not in result:
        result[number] = 1
    else:
        result[number] += 1




print(test_case)
print(num_student, num_couple)
print(back_number)
print(result)
