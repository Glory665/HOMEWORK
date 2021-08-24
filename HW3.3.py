
def thesaurus(*args):
    my_dict = {}
    for i in sorted(args):
        letter = i[0]
        if letter in my_dict:
            my_dict[letter] += [i]
        else:
            my_dict[letter] = [i]

    return my_dict

print( thesaurus("Иван", "Мария", "Петр", "Илья"))
