import copy
import re

n = input()  # take in the number
#n = '3**'  # example input
input_list = list(n)

stars = []  # list with stars positions
pattern = re.compile(r"\*")  # regular expression for finding stars
for find in pattern.finditer(n):
    stars.append(find.start())
stars_amount = len(stars)

missing_nums = [f'{i:0{stars_amount}d}' for i in range(pow(10, stars_amount))]  # to be filled in place of stars


# function checking if no identical neighbouring numbers in pin
def no_identical_neighbours(in_list) -> bool:
    for i in range(len(in_list)-1):
        if in_list[i] == in_list[i+1]:
            return False
    return True


for filler in missing_nums:
    input_list_temp = copy.copy(input_list)  # shallow copy list
    cnt = 0
    for star in stars:
        input_list_temp[star] = filler[cnt]
        cnt += 1
    if no_identical_neighbours(input_list_temp):
        print(''.join(input_list_temp))  # print correct pin
