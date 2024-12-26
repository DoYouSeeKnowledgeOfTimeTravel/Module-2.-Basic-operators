# def check_winner(X, O):
#     if area X or O ==

area = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
columns = 4
for first, second, third, four in zip(area[:columns], area[:columns], area[:columns], area[:columns]):
    print(f'{first: <5}{second: <5}{third: <5}{four}')


# area = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']


# for first, second, third, four in zip(area[:columns], area[:columns], area[:columns], area[:columns]):
#     print(f'{first: <5}{second: <5}{third: <5}{four}')



