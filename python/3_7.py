import random
matrix = [[0] * 3 for i in range(4)]
for i in range(4):
    for j in range(3):
        matrix[i][j] = random.randrange(-100, 100)
print(matrix)
print('строки:')
for i in range(4):
    print(i+1, 'строка: ', matrix[i])
print('столбцы:')
for j in range(3):
    x = [x[j] for x in matrix]
    print(j+1, 'столбец: ', x)
