spisok = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
spisok1 = []

for i in spisok:
    if i.replace("+", "").replace("-", "").isdigit():
        if i.isdigit():
            spisok1.append(f"'{int(i):02}'")
        else:
            spisok1.append(f"'{i[0]}{int(i):02}'")
    else:
        spisok1.append(i)

print(" ".join(spisok1))
