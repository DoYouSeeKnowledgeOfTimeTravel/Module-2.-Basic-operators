def pairs():
    number = int(input('Введите число: '))
    for i in range(1, 21):
        for j in range(i, 21):
            summa = i + j
            if summa == 2:
                continue
            if i == j and j == i:
                continue
            if number % summa == 0:
                print(f'{i}{j}', end='')

pairs()


# list_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# password = []
# index = 0
#
# for n in list_1:
#     int(input('Введите число: '))
#     for i in list_2:
#         for j in list_2:
#             print(f'{list_1[n]} - ', f'{i + j}')
#     break

# for i in list_2:
#     for j in list_2:
#         for q in list_1:
#             number = list_2[first_index]
#             if number % q == 0:
#                 print(f'{q} =', number + number)
#                 first_index += 1
#     break

# sum_ =
# if sum_


    # i = list_2[first_index]
    # j = list_2[first_index]
    # sum_ = i + j
    # for i in list_2:
    #     for j in list_2:
    #         if sum_ == sum(i) + sum(j):
    #             password.append(f'{str(sum_)}')
    #             print(password)
    # break


# for i in list_1:
#     while i == sum()
#         print(f'{i} =', )

# for i in list_1:
#     for each_elem in range(i):
#         each_elem += list_2[0]
#         while sum(list_2) == :
#             password.append(each_elem)
#             print(password)
#             break

    # if i in range(1, i):
    #
    # for j in list_1:
    #     print(i)
    #     break
    # for j in list_1:

            # while sum(list_2) == :
            #     password.append(each_elem)
            #     print(password)
            #     break

        # while each_elem != i:
        #     first_index += list_2[0]
        #     password.append(first_index)
        #     print(f'{i} =', password)
        #     break

# print(f'{i} =', password)