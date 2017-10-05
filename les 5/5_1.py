def convert(celsius):
    farenheid = celsius * 1.8 + 32
    return farenheid


n = 'F'
i = 'C'


def table():
    print('{1:4}  {0}'.format(n, i))
    for celsius in range(-30, 40, 10):
        print('{1:3} {0:7}'.format(convert(celsius), celsius))


table()
