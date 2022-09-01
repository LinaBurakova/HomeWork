print('Task 1')
import datetime


def myDecorator(fn):
    def function1(*args):
        start=datetime.datetime.now()
        result = fn(*args)
        print('Used time:', datetime.datetime.now()-start)
        return result
    return function1


@myDecorator
def simple_num(startN=1, endN=1000):
    list = []
    diapason=range(startN,endN+1)
    count=0
    for i in diapason:
        simple = True
        for n in range(2, i):
            if i % n == 0:
                simple = False
                break
        if i==1:
            count-=1
        if simple:
            count += 1
            list.append(i)
    print("Amount of prime numbers: ",count)
    print("List result:", list)
    return count


res=myDecorator(simple_num)
res()


print('Task 2')
# я все же нашла решение, как в декоратор передать input().
# Теперь границы диапазона для поиска простых чисел может вводить пользователь
# перед декораторам объявила переменные, которые будут принимать значения
# а после того, как мы вызовем декоратор, эти переменные я передаю в объект res1
startN = int(input("Enter num1:"))
endN = int(input("Enter num2:"))
def myDecorator1(fn):
    def function2(startN,endN):

        return fn(startN,endN)
    return function2

res1=myDecorator1(simple_num)
res1(startN,endN)

print('Task 3')
import random

income = [random.randrange(5000, 100000) for i in range(30)]
assets = [random.randrange(3000, 80000) for i in range(30)]


def month_financial_reporting1(fun):
    def decor():
        res = ' Daily financial report: \n'
        res += fun()
        return res

    return decor

def general_month_financial_reporting(fun):
    def decor():
        res = fun()
        res += f'Total: \n' \
               f'Income(total) - {sum(income)};' \
               f' Assets(total) - {sum(assets)};' \
               f' Profit(total) - {sum(income) - sum(assets)};\n'
        return res
    return decor

def avarage_month_financial_reporting(fun):
    def decor():
        res = fun()
        res += f'Avarage: \n' \
            f'Income(avarage) - {sum(income)/30};' \
            f' Assets(avarage) - {sum(assets)/30};' \
            f' Profit(avarage) - {(sum(income) - sum(assets))/30};\n'
        return res
    return decor


@month_financial_reporting1
@general_month_financial_reporting
@avarage_month_financial_reporting
def month_report(income=income, assets=assets):
    fin_report = ''
    for i in range(30):
        fin_report += f'Date {i + 1}' \
                  f' - Income: {income[i]}' \
                  f' - Assets: {assets[i]}' \
                  f' - Profit:{income[i] - assets[i]}\n'

    return fin_report

print(month_report())