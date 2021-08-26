import re

class MyDate:
    def __init__(self, data):
        self.data = data


    @classmethod
    def d_2(cls, param):
        param = param.replace('.','-').replace('/', '-').split('-')
        return cls(param)

    @staticmethod
    def d_1(obj):
        day = int(obj.data[0])
        month = int(obj.data[1])
        year = int(obj.data[2])
        if day > 0 and day < 32:
            if month > 0 and month < 13:
                if year > 1900 and year < 2035:
                    return f"{obj.data}"
                else:
                    print("Enter years")
            else:
                print("Enter month")
        else:
            print("Enter date")


data_1 = MyDate.d_2('21-12-2021')
print(MyDate.d_1(data_1))