from math import *

mf = []
mg = []
my = []

mg_max = 0
mf_max = 0
my_max = 0

a_mass = []
x_mass = []

while True:
    try:
        a = float(input("Введите a: "))
        x = float(input("Введите x: "))
        fun = str(input("Введите ф-ию которую вы хотите вычислить( g, f, y): "))
        p = int(input('Сколько считать: '))
        sh = float(input('С каким шагом?: '))
        break
    except:
        print('Вы ввели невернеы данные!')


def f_calc(x, a):
    return  math.atan(24 * (a**2) + 25 * a * x + 6 * x**2)


def f_func_max(mf):
    return max(mf)


def g_func():
    global mg_max
    g = (4 * (-4 * (a ** 2) + a * x + 5 * x ** 2)) / (-20 * (a ** 2) + 28 * a * x + 3 * x ** 2)
    if (-20 * (a ** 2) + 28 * a * x + 3 * x ** 2) == 0:
        print('ERROR')
    else:
        # print(g)
        if g > mg_max:
            mg_max = g
        mg.append(g)
        # print(mg_max)


def y_func():
    global my_max
    y = math.log(2*(a**2)-7*a*x+6*(x**2)+1)
    if (x > 0) and (a > 0):
        e = 2 * (a ** 2) - 7 * a * x + 6 * (x ** 2) + 1
        if  e ==0 :
            print("Выражение под знаком логарифма должно быть < 0")
        else:
            Y = math.log(2 * (a ** 2) - 7 * a * x + 6 * (x ** 2) + 1)
            print(Y)

    if y > my_max:
            my_max = y
            my.append(y)




run = True
while run:
    while p >= 0:
        if p == 0:
            # while run:
            #     try:
            question = input('Вы хотите продолить?(да, нет)')
                #     break
                # except:
                #     print('Введены неверные данные')
            if question == ('да' or 'yes'):
                while run:
                    try:
                        p = int(input('Сколько считать?'))
                        sh = float(input('С каким шагом?'))
                        break
                    except:
                        print('Введены неверные данные')
            else:
                print('END')

        if a != 0 and x != a:
            for i in range(p):
                a_mass.append(a)
                if fun == 'g':
                    g_func()
                elif fun == 'f':
                    f_func()
                elif fun == 'y':
                    y_func()
                a += sh
        p -= 1
        if p == 0:
            output = 0
            # while run:
            #     try:
            output = str(input('Как вывести ответ? (tab, str)'))
                #     break
                # except:
                #     print("Введены неверные данные")
            if output == 'str':
                if fun == 'g':
                    print('Максимальный эл-т массива mg: ' + str(mg_max))
                    # Вывод массива в строку
                    print(str(mg))
                if fun == 'f':
                    print('Максимальный эл-т массива mf: ' + str(mf_max))
                    # Вывод массива в строку
                    print(mf)
                if fun == 'y':
                    print('Максимальный эл-т массива my: ' + str(my_max))
                    # Вывод массива в строку
                    print(my)
            elif output == 'tab':
                if fun == 'g':
                    print('| ' + 'a' + '   | ' + 'x' + '   |  ' + 'y')
                    for i in mg:
                        for j in a_mass:
                            print('| ' + str(j) + ' | '  + str(x) + ' | ' + str(i) + ' |')
                            j += 1
                        i += 1
                if fun == 'f':
                    print('| ' + 'a' + '   | ' + 'x' + '   |  ' + 'y')
                    for i in mf:
                        for j in a_mass:
                            print('| ' + str(j) + ' | ' + str(x) + ' | ' + str(i) + ' |')
                            j += 1
                        i += 1
                if fun == 'y':
                    print('| ' + 'a' + '   | ' + 'x' + '   |  ' + 'y')
                    for i in my:
                        for j in a_mass:
                            print('| ' + str(j) + ' | ' + str(x) + ' | ' + str(i) + ' |')
                            print('| {} | {} | {} |'.format(j, x, i))
                            j += 1
                        i += 1
        run = False

my_file_mg = open('mg_list.txt', 'w')
for i in mg:
    my_file_mg.write(str(i) + '\n')
my_file_mg.close()
my_file_mf = open('mf_list.txt', 'w')
for i in mf:
    my_file_mf.write(str(i) + '\n')
my_file_mf.close()
my_file_my = open('my_list.txt', 'w')
for i in my:
    my_file_my.write(str(i) + '\n')
my_file_my.close()

mf.clear()
mg.clear()
my.clear()

my_file_mg = open('mg_list.txt', 'r')
mg = [float(e.strip()) for e in my_file_mg.readlines()]
my_file_mg.close()
print(mg)

my_file_mf = open('mf_list.txt', 'r')
mf = [float(e.strip()) for e in my_file_mf.readlines()]
my_file_mf.close()
print(mf)

my_file_my = open('my_list.txt', 'r')
m = [float(e.strip()) for e in my_file_my.readlines()]
my_file_my.close()
print(my)