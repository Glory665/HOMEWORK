import re


def email_parse(email_adress):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_adress):
        raise ValueError(f'wrong email: {email_adress}')
    print(RE_email.match(email_adress).groupdict())


for i in ['glory@mail.ru', 'glory@glorymail', 'glo665re@gmail.com']:
    try:
        email_parse(i)
    except ValueError as error:
        print(error)
