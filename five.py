#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


proceeds = float(input("Введите сумму выручки фирмы = "))
costs = float(input("Ввведите сумму издержек фирмы = "))
s = proceeds - costs
if s >= 0:
    print(f"Прибыль фирмы составила : {s}")
    print(f"Рентабельность выручки : {s/proceeds}")
    num = int(input("Введите численность сотрудников фирмы : "))
    print(f"Прибыль фирмы в расчете на одного сотрудника равна : {s/num}")
else:
    print(f"Убыток фирмы составил : {s}")





