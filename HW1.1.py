# Лашин Вячеслав GU_python_1594

# Пользователь вводит произвольное количество секунд
duration = int(input('Enter seconds: '))

sec = duration % 60
min = duration // 60
hour = duration // 3600
day = duration // 86400

if duration < 60:
    print(sec, 'сек')
elif duration >= 60 and duration < 3600:
    print(min, 'мин', sec, 'сек')
elif duration >= 3600 and duration < 86400:
    print(hour, 'час' ,duration % 3600 // 60,'мин', sec, 'сек')
else:
    print(day, 'дн', duration % 86400 // 3600, 'час' ,duration % 3600 // 60,'мин', sec, 'сек')

# т.к. в сутках не может быть более 24 ч., запишем для этого условие:
if hour >= 24:
    hour = hour % 24

# более 60 мин считается часом, ограничиваем условием:
if min >= 60:
    min = min % 60

print('{} дн {} час {} мин {} сек'.format(day, hour, min, sec))