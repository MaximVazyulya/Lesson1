#6. Спортсмен занимается ежедневными пробежками.
# первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 %
# относительно предыдущего. Требуется определить номер
# дня, на который общий результат спортсмена составить
# не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

a = input("Введите результат первого дня пробежки км = ")
b = input("Введите результат которого надо достичь км  = ")
result_day = 1
km = float(a)
while km < float(b):
    print(f"{result_day}-й день : {km}")
    km = km + km  * 0.1
    result_day += 1
   # print("%.2f" % (20.0 / 8))
print(f"{result_day}-й день : {km}")
print(f"{result_day}-й день спортсмен достиг результата — не менее: {int(b)} км.")