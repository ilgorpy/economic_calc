import math

def fcredit():  # меню для выбора типа платежа по кредиту
    choice = input('Выберите тип платежа:\n1 - Аннуитетный платеж\n2 - Дифференцированный платеж\n')
    match choice.split():
        case ['1']:
            fannuittyPayment()
        case ['2']:
            fdifferentiatedPayment()
        case _:
            print('Ошибка ввода! Повторите попытку!')

def fannuittyPayment():  # меню для выбора неизвестной
    choice = input(
        '\nВыберите неизвестную величину:\n1 - Сумма кредита\n2 - Процентная ставка\n3 - Срок выплаты кредита\n4 - Платежи по кредиту\n5 - Вернуться в главное меню\n')
    match choice.split():
        case ['1']:
            fsummCredit()
        case ['2']:
            fpercent()
        case ['3']:
            fpaymentTerm()
        case ['4']:
            ftranche()
        case ['5']:
            main()
        case _:
            print('Такого пункта меню не существует! Повторите попытку.\n')
            fannuittyPayment()

def fmenuAnnuit(func):  # меню для выбора дальнейшего пользовательского решения
    while True:
        choice = input(
            '\nВыберите:\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на аннуитетный платеж с другой неизвестной\n3 - Выход в главное меню\n')
        match choice.split():
            case ['1']:
                func()
            case ['2']:
                fannuittyPayment()
            case ['3']:
                main()
            case _:
                print('Ошибка ввода! Повторите попытку.')

def fsummCredit():  # функция, вычисляющая сумму кредита
    global percent, payment_term, tranche, decimal_point
    try:
        percent = float(input('\nПроцентная ставка: '))
        payment_term = int(input('Срок выплаты кредита: '))
        tranche = float(input('Платежи по кредиту: '))
        decimal_point = int(input('Количество знаков после запятой: '))
    except ValueError:
        print('Срок выплаты кредита - целое число! Повторите попытку.')
        fsummCredit()
    if percent <= 0 or payment_term <= 0 or tranche <= 0:
        print('Ошибка ввода! Вводите положительные числа.')
    else:
        summ_percent = 1
        for n in range(1, payment_term):
            summ_percent += (percent / 100 + 1) ** n
        summcredit = round((tranche * summ_percent) / (percent / 100 + 1) ** payment_term, decimal_point)
        print('Сумма кредита: ', summcredit, 'рублей')
        fmenuAnnuit(fsummCredit)

def fpercent():  # функция, вычисляющая процентную ставку
    global summ_credit, tranche1, tranche2, decimal_point
    print('Берут кредит на 2 года(месяца)')
    try:
        summ_credit = float(input('\nСумма кредита: '))
        tranche1 = float(input('Введите первый платеж: '))
        tranche2 = float(input('Введите второй платеж: '))
        decimal_point = int(input('Количество знаков после запятой: '))
    except ValueError:
        print('Срок выплаты кредита - целое число! Повторите попытку.')
        fpercent()
    if summ_credit <= 0 or tranche1 <= 0 or tranche2 <= 0:
        print('Ошибка ввода! Вводите положительные числа.')
    else:
        tranche1 *= -1
        tranche2 *= -1
        d = tranche1 ** 2 - 4 * summ_credit * tranche2
        if d < 0:
            print('Корней нет')
        elif d == 0:
            x = (-tranche1) / (2 * summ_credit)
            res = round((x - 1) * 100, decimal_point)
            print('Процентная ставка: ', res, '%')
        else:
            x = (-tranche1 + math.sqrt(d)) / (2 * summ_credit)
            res = round((x - 1) * 100, decimal_point)
            print('Процентная ставка: ', res, '%')
        fmenuAnnuit(fpercent)

def fpaymentTerm():  # функция, вычисляющая срок кредита
    global percent, summ_credit_after, summ_credit_before
    try:
        summ_credit_before = float(input('\nСумма кредита: '))
        percent = float(input('Процентная ставка: '))
        summ_credit_after = float(input('Введите уплаченную сумму: '))
    except ValueError:
        print('Ошибка ввода! Повторите попытку.')
        fpaymentTerm()
    if percent <= 0 or (summ_credit_after >= summ_credit_before or summ_credit_before <= 0):
        print('Ошибка ввода! Повторите попытку.')
    else:
        term = round(math.log10(summ_credit_after / summ_credit_before) / math.log10(1 + percent / 100))
        print('За', term, 'лет(года, месяца(-ев)) будет уплачен кредит')
        fmenuAnnuit(fpaymentTerm)

def ftranche():  # функция, вычисляющая размер платежей
    global summ_credit, percent, payment_term, decimal_point
    try:
        summ_credit = float(input('\nСумма кредита: '))
        percent = float(input('Процентная ставка: '))
        payment_term = int(input('Срок выплаты кредита (целое число): '))
        decimal_point = int(input('Количество знаков после запятой: '))
    except ValueError:
        print('Ошибка ввода! Повторите попытку.')
        ftranche()
    if summ_credit <= 0 or percent <= 0 or payment_term <= 0:
        print('Ошибка ввода! Повторите попытку.')
    else:
        tranchee = (summ_credit * (1 + percent / 100) ** payment_term * (percent / 100)) / ((1 + percent / 100) ** payment_term - 1)
        print('Платеж по кредиту:', round(tranchee, decimal_point))
        fmenuAnnuit(ftranche)

def fdifferentiatedPayment():  # меню для выбора неизвестной
    print('Пока в процессе разработки...')
    main()

# заканчиваются кредиты - начинаются вклады

def fdeposit():  # меню для выбора неизвестной величины вклада
    choice = input('Выберите неизвестную величину:\n1 - Начальная сумма вклада\n2 - Итоговая сумма вклада\n3 - Продолжительность жизни вклада\n4 - Вернуться в главное меню\n')
    match choice.split():
        case ['1']:
            fsummdepositbefore()
        case ['2']:
            fsummdepositafter()
        case ['3']:
            ftermdeposit()
        case ['4']:
            main()
        case _:
            print('Ошибка ввода! Повторите попытку.')
            fdeposit()

def fmenudeposit(func):  # меню для выбора дальнейшего пользовательского решения
    while True:
        choice = input(
            '\nВыберите:\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на вклад с другой неизвестной\n3 - Выход в главное меню\n')
        match choice.split():
            case ['1']:
                func()
            case ['2']:
                fdeposit()
            case ['3']:
                main()
            case _:
                print('Ошибка ввода! Повторите попытку.')


def fsummdepositafter():
    global percent, payment_term, decimal_point, initial_deposit_amount, additional_amount, count
    try:
        initial_deposit_amount = float(input('\nНачальная сумма вклада: '))
        percent = float(input('Процент по вкладу: '))
        payment_term = int(input('Срок вклада: '))
        additional_amount = float(input('Дополнительная сумма(необязательно - поставьте ноль): '))
        count = int(input('Количество внесений доп. сумм(необязательно - поставьте ноль): '))
        decimal_point = int(input('Количество знаков после запятой: '))
    except ValueError:
        print('Ошибка ввода! Повторите попытку.')
        fsummdepositafter()
    if initial_deposit_amount <= 0 and percent <= 0 and payment_term <= 0 and additional_amount < 0 and decimal_point <= 0:
        print('Ошибка ввода! Повторите попытку.')
        fsummdepositafter()
    else:
        for term in range(1, payment_term + 1):
            initial_deposit_amount *= (1 + percent / 100)
            if count != 0:
                initial_deposit_amount += additional_amount
                count -= 1
            print(f'Сумма вклада на {term} год(месяц):', end=' ')
            print(round(initial_deposit_amount, decimal_point))

        print('Итоговая сумма по вкладу:', round(initial_deposit_amount, decimal_point))
    fmenudeposit(fsummdepositafter)


def fsummdepositbefore():
    print('Пока в процессе разработки...')
    fdeposit()


def ftermdeposit():
    print('Пока в процессе разработки...')
    fdeposit()

def main():  # главное меню
    print('Вклады или кредиты?')
    choice = input('1 - Кредит\n2 - Вклад\n3 - Выход\n')
    match choice.split():
        case ['1']:
            fcredit()
        case ['2']:
            fdeposit()
        case ['3']:
            exit()
        case _:
            print('Ошибка ввода! Повторите попытку.')
            main()

percent, payment_term, tranche, decimal_point, summ_credit, tranche1, tranche2, summ_credit_after, summ_credit_before, depos_before, initial_deposit_amount, additional_amount, count = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

main()