#Ex01.:
def get_num():
    while True:
        try:
            return float(input('Informe um número: '))
        except ValueError: print('Erro. Informe um número válido')

def doble(num):
    return num * 2

def triple(num):
    return num * 3

def square(num):
    return num ** 2

def half(num):
    return num / 2

def show_menu():
    dict_opt = {1: 'Dobro',
                2: 'Triplo',
                3: 'Quadrado',
                4: 'Metade'}
    for x, y in dict_opt.items():
        print(f'[{x}] - {y} ')
    choice_menu()

def choice_menu():
    opt = int(input('\nSelecione sua opção: '))
    match opt:
        case 1:
            print(f'{doble(n):.2f}')
        case 2:
            print(f'{triple(n):.2f}')
        case 3:
            print(f'{square(n):.2f}')
        case 4: 
            print(f'{half(n):.2f}')
        case _: 
            print('Selecione uma opção válida')

n = get_num()

if __name__ == '__main__':
    show_menu()