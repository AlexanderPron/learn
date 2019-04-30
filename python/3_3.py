import random
rand_tuple = tuple()
max = 0
min = 101
for i in range(10):
    rnd_num = round(random.random()*100, 2)
#    if rnd_num >= max:
#        max = rnd_num
#    if rnd_num <= min:
#        min = rnd_num
    rand_tuple += (rnd_num, )
print('Случайный список: ', rand_tuple)
for tuple_elem in rand_tuple:
    if tuple_elem >= max:
        max = tuple_elem
    if tuple_elem <= min:
        min = tuple_elem
print('max = ', max)
print('min = ', min)