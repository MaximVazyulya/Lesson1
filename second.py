#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.
m = 0
h = 0
sec = 0
print("Перевод секунд в чч:мм:сс")
sec = int(input("Введите время в секундах = "))
if sec >= 3600:
    h = int(sec/3600)
    sec = sec - 3600 * h
if sec >= 60 & sec < 3600:
    m = int(sec/60)
    sec = sec - 60 * m
print(h, ":", m, ":", sec)
print(f"{h} : {m} : {sec}")







