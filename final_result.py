#Переменные
import sys

person_name = ['admin']
pass_word = ['admin']
name_1 = "0"
pass_1 = "0"
ind = '0'
int_pass = '0'
time = 0
length = 0
width=0
exit_blok = 0
spase = 0
leg_a = 0
leg_b = 0


#Цикл Регистрация+Вход
while True:
    #Проверка пользовательского ввода
    print('\n(Для выхода из программы , напишите exit или выйти)')
    start_1 = input('Что бы войти , нажмите 1 , что бы зарегистрироваться , нажмите 2: ')
    if start_1 == 'exit':
        sys.exit()
    if start_1 == 'выйти':
        sys.exit()
    if start_1 != '1' and start_1 != '2':
        print("\nОшибка! Вы вели неправильный вариант запроса,"
              "попробуйте снова!'")
        continue
    #Регистрация
    if start_1 == "2":
        #Цикл регистрация имени
        while time !=1:
            if exit_blok  == 0:
                while True:
                    try:
                        print('\n(Для того чтобы вернутся назад , напишите back или назад)'
                              '\nИмя должно быть от 5 до 12 символов без пробелов!')
                        # Пользовательский ввод
                        name = input('Введите имя: ')
                    # Перехват ошибки
                    except KeyboardInterrupt:
                        print('\nОшибка ввода , повторите ошибку!')
                        continue
                    except ValueError as e:
                        print("\nОшибка ввода , повторите ошибку!")
                        continue
                    else:
                        # Проверка возвращения
                        if name == 'back':
                            print('\nВозвращение')
                            exit_blok = 1
                            break
                        if name == 'назад':
                            print('\nВозвращение')
                            exit_blok = 1
                            break

                        # Проверки пробела
                        del_space = name.strip()
                        col_space = len(del_space)
                        if col_space == 0:
                            print('\nПробелы запрещены!')
                            continue
                        # Проверка кол-тво символов
                        len_name = len(name)
                        if len_name >= 13 or len_name <= 4:
                            print('\nИмя не доступно!')
                            continue
                        # Проверка есть или нет
                        if name in person_name:
                            print('\nДанное имя существует, введите другое имя!')
                            continue
                        else:
                            person_name.extend([del_space])
                            time += 1
                            break
            # Проверка возвращения
            elif exit_blok == 1:
                break

        #Обнуления time
        time = 0
        #Цикл регистрация пароля
        while time !=1:
            if exit_blok == 0:
                while True:
                    try:
                        print('(Пароль должно быть от 4 до 21 символов без пробелов!)')
                        # Пользовательский ввод
                        key = input('Введите пароль: ')
                    # Перехват ошибки
                    except KeyboardInterrupt:
                        print('\nОшибка ввода , повторите ошибку!')
                        continue
                    except ValueError as e:
                        print("\nОшибка ввода , повторите ошибку!")
                        continue
                    else:
                        # Проверка возвращения
                        if key == 'back':
                            print('\nВозвращение')
                            exit_blok = 1
                            break
                        if key == 'назад':
                            print('\nВозвращение')
                            exit_blok = 1
                            break
                        # Проверка кол-тво символов
                        len_key = len(key)
                        if len_key >=21 or len_key <= 4:
                            print('\nПароль не допустимый!')
                            continue
                        # Проверки пробела
                        del_space = key.strip()
                        col_space = len(del_space)
                        if col_space == 0:
                            print('\nПробелы запрещены!')
                            continue
                        # Проверка есть или нет
                        if key in pass_word:
                            print('\nДанный пароль существует , введите другой пароль!')
                            continue
                        else:
                            pass_word.extend([del_space])
                            time += 1
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

    #Обнуления time
    time = 0
    #Вход
    if start_1 == '1':
        while True:
            try:
                print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                # Пользовательский ввод
                name_1=input('Введите своё имя: ')
                # Проверка возвращения
                if name_1 == 'back':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                if name_1 == 'назад':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                # Проверка имени
                ind = person_name.index(name_1)
                # Пользовательский ввод
                pass_1 = input('\nВведите пароль: ')
                # Проверка имени
                if pass_1 == 'back':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                if pass_1 == 'назад':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                # Проверка пароля
                int_pass = pass_word.index(pass_1)
            # Перехват ошибки
            except ValueError as e:
                print("\nОшибка ввода , повторите ошибку!")
                continue
            except KeyboardInterrupt:
                print('\nОшибка ввода , повторите ошибку!')
                continue
            else:
                # Проверка индекса
                if start_1 == '1' and ind == int_pass:
                    print('\nДобро пожаловать')
                    exit_blok = 2
                    break
                elif start_1 == '1' and ind != int_pass:
                    print('\nПовторите вход')
                    continue
        # Проверка возвращения
        if exit_blok == 1:
            continue
        elif exit_blok == 2:
            break

#Начала калькулятора
while True:
    # Выбор пользователем действия
    do_pol = input('\n(Для выхода из программы , напишите exit или выйти)'
                   '\nВыберите действие из перечня ниже'
                   '\n1) Извлечение числа, из под знака корня.'
                   '\n2) Возведение числа в степень.'
                   '\n3) Нахождение площади ,а также периметр фигур. '
                   '\nВыполнение действие: '
                        )
    # Проверка возвращения
    if do_pol == 'exit':
        sys.exit()
    if do_pol == 'выйти':
        sys.exit()
    # Проверка выбора действия
    if do_pol != '1' and do_pol != '2' and do_pol != '3':
        print('\nОшибка! Вы вели неправильный вариант запроса, попробуйте снова!')
        continue
    # Извлечение числа, из-под знака корня
    if do_pol == '1':
        while True:
            try:
                print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                # Пользовательский ввод
                pol_koren = input('\nВедите число под знаком корня: ')
                # Проверка возвращения
                if pol_koren == 'back':
                    print('\nВозвращение')
                    break
                if pol_koren == 'назад':
                    print('\nВозвращение')
                    break
                # Изменения int на float
                pol_koren=float(pol_koren)
                #Вычисления числа из-под знака корня
                sqrt = pol_koren ** 0.5
            # Перехват ошибки
            except ValueError as e:
                print("\nОшибка, Вы ввели неправильный вариант запроса, попробуйте снова!")
                continue
            else:
                print('\nКвадратный корень из числа '+str(pol_koren)+' равен '+str(sqrt))
                break
        continue
    # Возведение числа в степень
    elif do_pol == '2':
        while True:
            try:
                print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                # Пользовательский ввод
                one_int = input('Ведите число основание: ')
                # Проверка возвращения
                if one_int == 'back':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                if one_int == 'назад':
                    print('\nВозвращение')
                    exit_blok = 1
                    break
                # Изменения int на float
                one_int = float(one_int)
                # Пользовательский ввод
                two_int = input('Ведите степень: ')
                # Проверка возвращения
                if two_int == 'back':
                    print('\nВозвращение')
                    break
                if two_int == 'назад':
                    print('\nВозвращение')
                    break
                # Изменения int на float
                two_int=float(two_int)
                # Вычисления возведение в степень
                degree = one_int ** two_int
            # Перехват ошибки
            except ValueError as e:
                print("Ошибка, Вы ввели неправильный вариант запроса, попробуйте снова!")
                continue
            else:
                print('\nСтепень числа ' + str(degree) + ' равен ')
                break
        continue
    # Нахождение площади, а также периметр фигур
    elif do_pol == '3':
        while True:
            print('\n(Для того чтобы вернутся назад , напишите back или назад)')
            # Выбор пользователем действия
            do_pol_3 = input('1) Нахождение площади и периметра квадрата,прямоугольника'
                             '\n2) Нахождение площади и периметра параллелограмма'
                             '\nВыполнение действие: '
                             )
            # Проверка возвращения
            if do_pol_3 == 'back':
                print('\nВозвращение')
                break
            if do_pol_3 == 'назад':
                print('\nВозвращение')
                break
            # Проверка выбора действия
            if do_pol_3 != '1' and do_pol_3 != '2' and do_pol_3 != '3':
                print('\nОшибка! Вы вели неправильный вариант запроса, попробуйте снова!')
                continue
            # Нахождение площади и периметра квадрата, прямоугольника
            if do_pol_3 == '1':
                while True:
                    try:
                        print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        length = input("Введите длину :  ")
                        # Проверка возвращения
                        if length == 'back':
                            length = 1
                            print('\nВозвращение')
                            break
                        if length == 'назад':
                            length = 1
                            print('\nВозвращение')
                            break
                        # Изменения int на float
                        length = float(length)
                    # Перехват ошибки
                    except ValueError as e:
                        print("Ошибка, Вы ввели неправильный вариант запроса"
                              "\nПопробуйте снова!")
                        continue
                    else:
                        break
                if length == 1:
                    continue
                while True:
                    try:
                        print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        width = input("Введите ширину:  ")
                        # Проверка возвращения
                        if width == 'back':
                            print('\nВозвращение')
                            width = 1
                            break
                        if width == 'назад':
                            print('\nВозвращение')
                            width = 1
                            break
                        # Изменения int на float
                        width=float(width)
                    # Перехват ошибки
                    except ValueError as e:
                        print("Ошибка, вы ввели неправильный вариант запроса, "
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
                    print('\nПлощадь квадрата равна '+str(square)+' периметр равен '+str(perimeter))
                else:
                    print('\nПлощадь прямоугольника равна ' + str(square) + ' периметр равен ' + str(perimeter))

            #Нахождение площади и периметра параллелограмма
            elif do_pol_3 == '2':
                while True:
                    try:
                        print('\n(Для того чтобы вернутся назад , напишите back или назад)')
                        # Пользовательский ввод
                        leg_a = input("\nВведите 1 сторону:  ")
                        # Проверка возвращения
                        if leg_a == 'back':
                            print('\nВозвращение')
                            leg_a = 1
                            break
                        if leg_a == 'назад':
                            print('\nВозвращение')
                            leg_a = 1
                            break
                        # Изменения int на float
                        leg_a=float(leg_a)
                        # Пользовательский ввод
                        leg_b = input("Введите 2 сторону:  ")
                        # Проверка возвращения
                        if leg_b == 'back':
                            print('\nВозвращение')
                            leg_b = 1
                            break
                        if leg_b == 'назад':
                            print('\nВозвращение')
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
                        print("Ошибка, вы ввели неправильный вариант запроса, "
                              "попробуйте снова!")
                        continue
                    else:
                        print('\nПлощадь параллелограмма равна ' + str(square) + ' периметр равен ' + str(perimeter))
                        break
                # Проверка возвращения
                if leg_a == 1:
                    continue
                if leg_b == 1:
                    continue
        continue