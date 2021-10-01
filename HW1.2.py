day_sales = []
num_sum = 0
all_sum = 0

for i in range(1, 1000, 2):
    day_sales.append(i ** 3) # вариант а.
   #day_sales.append(i ** 3 + 17) # вариант b.

for n in day_sales:
    var = n
    num_sum = 0
    while n > 0:
        count = n % 10
        num_sum += count
        n = n // 10
    if num_sum % 7 == 0:
        all_sum += var

print(all_sum)