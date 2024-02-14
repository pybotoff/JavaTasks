
def goNumbers():
    try:
        numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        valid_numbers = []
        for number in numbers_list:
            if number %2 == 0:
                valid_numbers.append(number)
        for i in valid_numbers:
            print(i)
    finally:
        main()
def Operations():
    try:
        a = int(input('Введите первое число:\n'))
        b = int(input('Введите второе число:\n'))
        print(f'{a} + {b} = {a+b}')
        print(f'{a} - {b} = {a-b}')
        print(f'{a} * {b} = {a*b}')
        if b != 0:
            print(f'{a} / {b} = {a/b}')
        else:          
            print('На ноль делить нельзя.')
    except ValueError:
        print('Введите числовое значение от 0 до 9')
    finally:
        main()

def Strings():
    try:
        a = str(input('Первая строка:\n'))
        b = str(input('Вторая строка:\n'))
        if a == b:
            print('Строки идентичны')
        else:
            print(('Строки неидентичны'))
    finally:
        main()

def main():
    try:
        select = int(input('Введите номер функции, которую вы хотите вызвать:\n1. Вывести четные значения от 1 до 10\n2. Провести операцию с двумя числами\n3. Сравнить строки\n4. Выход\n'))
        if select == 1:
            goNumbers()
        elif select == 2:
            Operations()
        elif select == 3:
            Strings()
        elif select == 4:
            print('Выход из программы')
        else:
            print('Неверный выбор')
            main()
    except ValueError:
        print('Неверный выбор')
        main()
if __name__ == '__main__':
    main()