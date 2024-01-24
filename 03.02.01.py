my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def tmp(x):
    if x < 0:
        return 
    tmp(x - 1)
    print(x)
    if x == my_list[-1]:
        print('Конец списка')

n = my_list[-1]
tmp(n)