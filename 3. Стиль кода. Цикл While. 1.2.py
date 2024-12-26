from unittest import skipIf

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
first_index = 0

# while my_list[first_index] >= 0:
#     print(my_list[first_index])
#     first_index += 1

while first_index < len(my_list):
    number = my_list[first_index]
    if number > 0:
        print(number)
        first_index += 1
        continue
    if number == 0:
        first_index += 1
        continue
    break

        # first_index += 1
        # print(number)
        # continue


    # for number in my_list:
    #     if number < 0:
    #         break
    #     print(number)




# while first_index < len(my_list):
#     print(my_list[first_index])
#     first_index += 1
