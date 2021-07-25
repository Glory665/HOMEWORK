# _____________ Вариант A _______________

prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90,
          70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78, 48.29,
          8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]

for i in prices:
    rub = int(i)
    cop = str(f"{i:.2f}".split('.')[-1])
    print(f"{rub} руб {cop} коп")


# _____________ Вариант B _______________

print(f"ID = {id(prices)} prices = {prices}")
prices.sort()
print(f"ID = {id(prices)} prices = {prices}")


# _____________ Вариант C _______________

prices_sorted = sorted(prices)
print(f"ID = {id(prices_sorted)} prices = {prices_sorted}")


# _____________ Вариант D _______________

max_prices = sorted(prices)[::-1][:5]
print(f"ID = {id(max_prices)} {max_prices}")
