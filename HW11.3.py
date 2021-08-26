class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


dic = []
while True:
    num = input("Enter text: ")

    num = str(num)
    if num == 'Stop':
        break
    else:
        try:
            num = int(num)
            dic.append(num)
        except (ValueError, MyException) as err:
            print(err)


print(dic)