import random
rand_list = []
for i in range(6):
    rnd_num = random.randint(1, 100)
    rand_list.append(rnd_num)
print('Случайный список: ', rand_list)
sort_list = sorted(rand_list)
print('Упорядоченный по возрастанию список :', sort_list)


