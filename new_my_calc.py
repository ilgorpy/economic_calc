import math

def credit():
    choice = input('\nВыберите тип платежа:\n1 - Аннуитетный платеж\n2 - Дифференцированный платеж\n')
    match choice.split():
        case ['1']:
            annuitty_payment()
        case ['2']:
            differentiated_payment()
        case _:
            print('Ошибка ввода! Повторите попытку!')


def annuitty_payment():  # меню для выбора неизвестной
    choice = input('\nВыберите неизвестную величину:\n1 - Сумма кредита\n2 - Процентная ставка\n3 - Срок выплаты кредита\n4 - Платежи по кредиту\n5 - Вернуться в главное меню\n')
    match choice.split():
        case ['1']:
            amount()
        case ['2']:
            percent_credit()
        case ['3']:
            credit_term()
        case ['4']:
            payments()
        case ['5']:
            main()
        case _:
            print('Такого пункта меню не существует! Повторите попытку.\n')
            annuitty_payment()


def menu_annuit(func):  # меню для выбора дальнейшего пользовательского решения
    while True:
        choice = input(
            '\nВыберите:\n1 - Снова решить подобную задачу задачу с этой неизвестной\n2 - Решить задачу на аннуитетный платеж с другой неизвестной\n3 - Выход в главное меню\n')
        match choice.split():
            case ['1']:
                func()
            case ['2']:
                annuitty_payment()
            case ['3']:
                main()
            case _:
                print('Ошибка ввода! Повторите попытку.')


def amount():  # функция, вычисляющая сумму кредита
    def data_input():
        global payment_term, percent, tranche, decimal_point
        try:
            percent = float(input('\nПроцентная ставка: '))
            payment_term = int(input('Срок выплаты кредита: '))
            tranche = float(input('Платежи по кредиту: '))
            decimal_point = int(input('Количество знаков после запятой: '))
        except ValueError:
            print('Срок выплаты кредита - целое число! Повторите попытку.')
            data_input()
        return percent, payment_term, tranche, decimal_point

    def data_output(summcredit):
        print('Сумма кредита: ', summcredit, 'рублей')

    def alg_amount(percent, payment_term, tranche, decimal_point):
        summ_percent = 1
        for n in range(1, payment_term):
            summ_percent += (percent / 100 + 1) ** n
        summcredit = round((tranche * summ_percent) / (percent / 100 + 1) ** payment_term, decimal_point)
        return summcredit

    percent, payment_term, tranche, decimal_point = data_input()
    summcredit = alg_amount(percent, payment_term, tranche, decimal_point)
    data_output(summcredit)
    menu_annuit(amount)


def percent_credit():
    def data_input():
        global summ_credit, tranche1, tranche2, decimal_point
        print('\nБерут кредит на 2 года(месяца)')
        try:
            summ_credit = float(input('Сумма кредита: '))
            tranche1 = float(input('Введите первый платеж: '))
            tranche2 = float(input('Введите второй платеж: '))
            decimal_point = int(input('Количество знаков после запятой: '))
        except ValueError:
            print('Срок выплаты кредита - целое число! Повторите попытку.')
            percent_credit()
        return summ_credit, tranche1, tranche2, decimal_point

    def data_output(result):
        print('Процентная ставка: ', result, '%')

    def alg_percent(summ_credit, tranche1, tranche2, decimal_point):
        global res
        tranche1 *= -1
        tranche2 *= -1
        d = tranche1 ** 2 - 4 * summ_credit * tranche2
        if d < 0:
            print('Корней нет')
        elif d == 0:
            x = (-tranche1) / (2 * summ_credit)
            res = round((x - 1) * 100, decimal_point)
        else:
            x = (-tranche1 + math.sqrt(d)) / (2 * summ_credit)
            res = round((x - 1) * 100, decimal_point)
        return res

    summ_credit, tranche1, tranche2, decimal_point = data_input()
    res = alg_percent(summ_credit, tranche1, tranche2, decimal_point)
    data_output(res)
    menu_annuit(percent_credit)

def credit_term():
    def data_input():
        global percent, amount_before, amount_after
        try:
            amount_before = float(input('\nСумма кредита: '))
            percent = float(input('Процентная ставка: '))
            amount_after = float(input('Введите уплаченную сумму: '))
        except ValueError:
            print('Ошибка ввода! Повторите попытку.')
            credit_term()
        return amount_before, percent, amount_after

    def data_output(term):
        print('За', term, 'лет(года, месяца(-ев)) будет уплачен кредит')

    def alg_crterm(amount_before, percent, amount_after):
        term = round(math.log10(amount_before / amount_before) / math.log10(1 + percent / 100))
        return term

    amount_before, percent, amount_after = data_input()
    term = alg_crterm(amount_before, percent, amount_after)
    data_output(term)
    menu_annuit(credit_term())


def main():  # главное меню
    print('Вклады или кредиты?')
    choice = input('1 - Кредит\n2 - Вклад\n3 - Выход\n')
    match choice.split():
        case ['1']:
            credit()
        case ['2']:
            deposit()
        case ['3']:
            exit()
        case _:
            print('Ошибка ввода! Повторите попытку.')
            main()

if __name__ == '__main__':
    main()
