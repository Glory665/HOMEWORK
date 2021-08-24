
def num_translate():

    dict = {'zero': 'ноль','one': 'один', 'two': 'два', 'three': 'три', 'four': 'четры', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    n = input('Enter number: ')
    if n in dict:
        print(dict[n])
    else:
        print(None)

num_translate()