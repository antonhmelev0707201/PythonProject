"""
  Данную программу написали:
    Шмелёв Антон Андреевич
    Таранов Гордей Алексеевич
    Отраднов Денис Сергеевич
"""

import sys
from tqdm import tqdm
import time
from colorama import Style,Fore

#Переменные
person_name = ['admin']
pass_word = ['admin']
name_1 = "0"
pass_1 = "0"
ind = '0'
int_pass = '0'
length = 0
width=0
exit_blok = 0
spase = 0
leg_a = 0
leg_b = 0
least_basic = 0
greatest_basic = 0
trapezoid_height = 0



#Цикл Регистрация+Вход
while True:
    #Проверка пользовательского ввода
    print(Style.RESET_ALL+'\n(Для выхода из программы , напишите exit или выйти)')
    start_1 = input('Что бы войти , нажмите 1 , что бы зарегистрироваться , нажмите 2: ')
    if start_1 == 'exit':
        print(Fore.RED + '\nПроизводится выход из программы')
        sys.exit()
    if start_1 == 'выйти':
        print(Fore.RED + '\nПроизводится выход из программы')
        sys.exit()
    if start_1 != '1' and start_1 != '2':
        print(Fore.RED+"\nОшибка! Вы вели неправильный вариант запроса, "
              "попробуйте снова!")
        continue
    #Регистрация
    if start_1 == "2":
    #Цикл регистрация имени
        if exit_blok  == 0:
            while True:
                try:
                    print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)'
                          '\nИмя должно быть от 5 до 12 символов без пробелов!')
                    # Пользовательский ввод
                    name = input('Введите имя: ')
                # Перехват ошибки
                except KeyboardInterrupt:
                    print(Fore.RED+'\nОшибка ввода , повторите ошибку!')
                    continue
                except ValueError as e:
                    print(Fore.RED+"\nОшибка ввода , повторите ошибку!")
                    continue
                else:
                    # Проверка возвращения
                    if name == 'back':
                        print(Fore.GREEN+'\nВозвращение')
                        exit_blok = 1
                        break
                    if name == 'назад':
                        print(Fore.GREEN+'\nВозвращение')
                        exit_blok = 1
                        break

                    # Проверки пробела
                    del_space = name.strip()
                    col_space = len(del_space)
                    if col_space == 0:
                        print(Fore.RED+'\nПробелы запрещены!')
                        continue
                    # Проверка кол-тво символов
                    len_name = len(name)
                    if len_name >= 13 or len_name <= 4:
                        print(Fore.RED+'\nИмя не доступно!')
                        continue
                    # Проверка есть или нет
                    if name in person_name:
                        print(Fore.RED+'\nДанное имя существует, введите другое имя!')
                        continue
                    else:
                        person_name.extend([del_space])
                        break
        # Проверка возвращения
        elif exit_blok == 1:
            break

        #Цикл регистрация пароля
        if exit_blok == 0:
            while True:
                try:
                    print(Style.RESET_ALL+'\n(Пароль должно быть от 4 до 21 символов без пробелов!)')
                    # Пользовательский ввод
                    key = input('Введите пароль: ')
                # Перехват ошибки
                except KeyboardInterrupt:
                    print(Fore.RED+'\nОшибка ввода , повторите ошибку!')
                    continue
                except ValueError as e:
                    print(Fore.RED+"\nОшибка ввода , повторите ошибку!")
                    continue
                else:
                    # Проверка возвращения
                    if key == 'back':
                        print(Fore.GREEN+'\nВозвращение')
                        exit_blok = 1
                        break
                    if key == 'назад':
                        print(Fore.GREEN+'\nВозвращение')
                        exit_blok = 1
                        break
                    # Проверка кол-тво символов
                    len_key = len(key)
                    if len_key >=21 or len_key <= 4:
                        print(Fore.RED+'\nПароль не допустимый!')
                        continue
                    # Проверки пробела
                    del_space = key.strip()
                    col_space = len(del_space)
                    if col_space == 0:
                        print(Fore.RED+'\nПробелы запрещены!')
                        continue
                    # Проверка есть или нет
                    if key in pass_word:
                        print(Fore.RED+'\nДанный пароль существует , введите другой пароль!')
                        continue
                    else:
                        pass_word.extend([del_space])
                        break
        # Проверка возвращения
        elif exit_blok == 1:
            #Проверка записалось ли имя 1 раз
            len_person_name = len(person_name)
            len_pass_word = len(pass_word)
            if len_person_name == len_pass_word:
                break
            elif len_person_name >=len_pass_word:
                del(person_name[-1])
                break

    #Вход
    if start_1 == '1':
        while True:
            try:
                print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад, напишите back или назад)')
                # Пользовательский ввод
                name_1=input('Введите своё имя: ')
                # Проверка возвращения
                if name_1 == 'back':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                if name_1 == 'назад':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                # Проверка имени
                ind = person_name.index(name_1)
                # Пользовательский ввод
                pass_1 = input('\nВведите пароль: ')
                # Проверка имени

                if pass_1 == 'back':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                if pass_1 == 'назад':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                # Проверка пароля
                int_pass = pass_word.index(pass_1)
            # Перехват ошибки
            except ValueError as e:
                print(Fore.RED+"\nОшибка ввода , повторите ошибку!")
                continue
            except KeyboardInterrupt:
                print(Fore.RED+'\nОшибка ввода , повторите ошибку!')
                continue
            else:
                # Полоска ожидания
                print(Fore.YELLOW+'Проверка: ')
                for e in tqdm([1,2,3,4,5,6,7,8,9,10]):
                    time.sleep(0.5)
                # Проверка индекса
                if start_1 == '1' and ind == int_pass:
                    print(Fore.GREEN+'\nДобро пожаловать')
                    exit_blok = 2
                    break
                elif start_1 == '1' and ind != int_pass:
                    print(Fore.RED+'\nПовторите вход')
                    continue

        # Проверка возвращения
        if exit_blok == 1:
            continue
        elif exit_blok == 2:
            break

#Начала калькулятора
while True:
    # Выбор пользователем действия
    do_pol = input(Style.RESET_ALL+'\n(Для выхода из программы , напишите exit или выйти)'
                   '\nВыберите действие из перечня ниже'+Fore.MAGENTA+
                   '\n1)Извлечение числа, из под знака корня.'
                   '\n2)Возведение числа в степень.'
                   '\n3)Нахождение площади, а также периметр фигур. '+
                   Fore.YELLOW+'\nВыполнение действие: '+Style.RESET_ALL
                        )
    # Проверка возвращения
    if do_pol == 'exit':
        print(Fore.RED + '\nПроизводится выход из программы')
        sys.exit()
    if do_pol == 'выйти':
        print(Fore.RED + '\nПроизводится выход из программы')
        sys.exit()
    # Проверка выбора действия
    if do_pol != '1' and do_pol != '2' and do_pol != '3':
        print(Fore.RED+'\nОшибка! Вы вели неправильный вариант запроса, попробуйте снова!')
        continue
    # Извлечение числа, из-под знака корня
    if do_pol == '1':
        while True:
            try:
                print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                # Пользовательский ввод
                pol_koren = input('\nВедите число под знаком корня: ')
                # Проверка возвращения
                if pol_koren == 'back':
                    print(Fore.GREEN+'\nВозвращение')
                    break
                if pol_koren == 'назад':
                    print(Fore.GREEN+'\nВозвращение')
                    break
                # Изменения int на float
                pol_koren=float(pol_koren)
                #Вычисления числа из-под знака корня
                sqrt = pol_koren ** 0.5
            # Перехват ошибки
            except ValueError as e:
                print(Fore.RED+"\nОшибка, Вы ввели неправильный вариант запроса, попробуйте снова!")
                continue
            else:
                # Полоска ожидания
                print(Fore.YELLOW+'Проверка: ')
                for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                    time.sleep(0.5)
                print(Fore.GREEN+'\nКвадратный корень из числа '+str(pol_koren)+' равен '+str(sqrt))
                break
        continue
    # Возведение числа в степень
    elif do_pol == '2':
        while True:
            try:
                print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                # Пользовательский ввод
                one_int = input('Ведите число основание: ')
                # Проверка возвращения
                if one_int == 'back':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                if one_int == 'назад':
                    print(Fore.GREEN+'\nВозвращение')
                    exit_blok = 1
                    break
                # Изменения int на float
                one_int = float(one_int)
                # Пользовательский ввод
                two_int = input('Ведите степень: ')
                # Проверка возвращения
                if two_int == 'back':
                    print(Fore.GREEN+'\nВозвращение')
                    break
                if two_int == 'назад':
                    print(Fore.GREEN+'\nВозвращение')
                    break
                # Изменения int на float
                two_int=float(two_int)
                # Вычисления возведение в степень
                degree = one_int ** two_int
            # Перехват ошибки
            except ValueError as e:
                print(Fore.RED+"Ошибка, Вы ввели неправильный вариант запроса, попробуйте снова!")
                continue
            else:
                # Полоска ожидания
                print(Fore.YELLOW+'Проверка: ')
                for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                    time.sleep(0.5)
                print(Fore.GREEN+'\nСтепень числа ' + str(degree) + ' равен ')
                break
        continue
    # Нахождение площади, а также периметр фигур
    elif do_pol == '3':
        while True:
            print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
            # Выбор пользователем действия
            do_pol_3 = input(
            Fore.MAGENTA+'\nВыберите действие из перечня ниже'
            '\n1)Нахождение площади и периметра квадрата,прямоугольника'
            '\n2)Нахождение площади и периметра параллелограмма'
            '\n3)Нахождение площади и периметра трапеции'
            +Fore.YELLOW+'\nВыполнение действие: '+Style.RESET_ALL
            )
            # Проверка возвращения
            if do_pol_3 == 'back':
                print(Fore.GREEN+'\nВозвращение')
                break
            if do_pol_3 == 'назад':
                print(Fore.GREEN+'\nВозвращение')
                break
            # Проверка выбора действия
            if do_pol_3 != '1' and do_pol_3 != '2' and do_pol_3 != '3':
                print(Fore.RED+'\nОшибка! Вы вели неправильный вариант запроса, попробуйте снова!')
                continue
            # Нахождение площади и периметра квадрата, прямоугольника
            if do_pol_3 == '1':
                while True:
                    try:
                        print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        length = input("Введите длину :  ")
                        # Проверка возвращения
                        if length == 'back':
                            length = 1
                            print(Fore.GREEN+'\nВозвращение')
                            break
                        if length == 'назад':
                            length = 1
                            print(Fore.GREEN+'\nВозвращение')
                            break
                        # Изменения int на float
                        length = float(length)
                    # Перехват ошибки
                    except ValueError as e:
                        print(Fore.RED+"Ошибка, Вы ввели неправильный вариант запроса"
                              "\nпопробуйте снова!")
                        continue
                    else:
                        break
                if length == 1:
                    continue
                while True:
                    try:
                        print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        width = input("Введите ширину:  ")
                        # Проверка возвращения
                        if width == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            width = 1
                            break
                        if width == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            width = 1
                            break
                        # Изменения int на float
                        width=float(width)
                    # Перехват ошибки
                    except ValueError as e:
                        print(Fore.RED+"Ошибка, вы ввели неправильный вариант запроса, "
                              "попробуйте снова!")
                        continue
                    else:
                        break
                if width == 1:
                    continue

                # Вычисления площади и периметра
                square = width * length
                perimeter = 2 * width + 2 * length
                # Проверка фигура квадрат или прямоугольник
                if width == length:
                    # Полоска ожидания
                    print(Fore.YELLOW+'Проверка: ')
                    for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                        time.sleep(0.5)
                    print(Fore.GREEN+'\nПлощадь квадрата равна '+str(square)+' периметр равен '+str(perimeter))
                else:
                    # Полоска ожидания
                    print(Fore.YELLOW+'Проверка: ')
                    for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                        time.sleep(0.5)
                    print(Fore.GREEN+'\nПлощадь прямоугольника равна ' + str(square) + ' периметр равен ' + str(perimeter))

            #Нахождение площади и периметра параллелограмма
            elif do_pol_3 == '2':
                while True:
                    try:
                        print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        leg_a = input("\nВведите 1 сторону:  ")
                        # Проверка возвращения
                        if leg_a == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            leg_a = 1
                            break
                        if leg_a == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            leg_a = 1
                            break
                        # Изменения int на float
                        leg_a=float(leg_a)
                        # Пользовательский ввод
                        leg_b = input("Введите 2 сторону:  ")
                        # Проверка возвращения
                        if leg_b == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            leg_b = 1
                            break
                        if leg_b == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            leg_b = 1
                            break
                        # Изменения int на float
                        leg_b = float(leg_b)
                        # Вычисления высоты
                        tall_x2 = leg_a ** 2 + leg_b ** 2
                        tall = tall_x2 ** 0.5
                        # Вычисления площади и периметра
                        square = leg_a * tall
                        perimeter = (leg_a * 2) + (leg_b * 2)
                    # Перехват ошибки
                    except ValueError as e:
                        print(Fore.RED+"Ошибка, вы ввели неправильный вариант запроса, "
                              "попробуйте снова!")
                        continue
                    else:
                        # Полоска ожидания
                        print(Fore.YELLOW+'Проверка: ')
                        for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                            time.sleep(0.5)
                        print(Fore.GREEN+'\nПлощадь параллелограмма равна ' + str(square) + ' периметр равен ' + str(perimeter))
                        break
                # Проверка возвращения
                if leg_a == 1:
                    continue
                if leg_b == 1:
                    continue

            #Нахождение площади и периметра трапеции
            elif do_pol_3 == '3':
                while True:
                    try:
                        print(Style.RESET_ALL+'\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        least_basic = input('Ведите наименьшее основание: ')
                        # Проверка возвращения
                        if least_basic == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            least_basic = 1
                            break
                        if least_basic == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            least_basic = 1
                            break
                        # Изменения int на float
                        least_basic = float(least_basic)
                        # Пользовательский ввод
                        greatest_basic = input('Ведите наибольшее основание: ')
                        # Проверка возвращения
                        if greatest_basic == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            greatest_basic = 1
                            break
                        if greatest_basic == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            greatest_basic = 1
                            break
                        # Изменения int на float
                        greatest_basic = float(greatest_basic)
                        # Проверка правильности трапеции
                        if greatest_basic < least_basic:
                            print(Fore.RED+'\nОшибка, наибольшая сторона основания трапеции, меньше наименьшей стороны!'
                                  '\nПовторите попытку!')
                            continue
                        # Пользовательский ввод
                        trapezoid_height = input('Ведите высоту трапеции: ')
                        # Проверка возвращения
                        if trapezoid_height == 'back':
                            print(Fore.GREEN+'\nВозвращение')
                            trapezoid_height = 1
                            break
                        if trapezoid_height == 'назад':
                            print(Fore.GREEN+'\nВозвращение')
                            trapezoid_height = 1
                            break
                        # Изменения int на float
                        trapezoid_height = float(trapezoid_height)
                        # Вычисления площади и периметра
                        square = 2/(least_basic+greatest_basic)*trapezoid_height
                        perimeter = (least_basic * 2) + (greatest_basic * 2)
                        # Перехват ошибки
                    except ValueError as e:
                        print(Fore.RED+"Ошибка, вы ввели неправильный вариант запроса, "
                              "попробуйте снова!")
                        continue
                    else:
                        # Полоска ожидания
                        print(Fore.YELLOW+'Проверка: ')
                        for e in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
                            time.sleep(0.5)
                        print(Fore.GREEN+'\nПлощадь трапеции равна ' + str(square) + ' периметр равен ' + str(perimeter))
                        break
                # Проверка возвращения
                if least_basic == 1:
                    continue
                elif greatest_basic == 1:
                    continue
                elif trapezoid_height == 1:
                    continue
        continue