from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "поза вчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(n, repeat=False):
    """
    Функция возвращает n шуток, сформированных из двух случайных слов

    :param n: количество шуток
    :param repeat: уникальные/неуникальные
    :return: список случайных шуток

    """

    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    my_list = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            my_list.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            my_list.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return my_list


print(get_jokes(3, True))