import random

pc = ('piedra', 'papel', 'tijera')
flag = True
puntos_pc = 0
puntos_user = 0

while flag:
    user = input('Elije piedra, papel o tijera: ').lower()

    def pc_choice():
        choice = random.choice(pc)
        return choice

    def game(pc, user):
        global puntos_pc, puntos_user

        if pc == 'piedra' and user == 'papel':
            puntos_user += 1
            return 'users win'
        elif user == 'piedra' and pc == 'papel':
            puntos_pc += 1
            return 'pc wins'
        elif user == 'tijera' and pc == 'piedra':
            puntos_pc += 1
            return 'pc wins'
        elif user == 'piedra' and pc == 'tijera':
            puntos_user += 1
            return 'user wins'
        elif user == 'tijera' and pc == 'papel':
            puntos_user += 1
            return 'user wins'
        elif pc == 'tijera' and user == 'papel':
            puntos_pc += 1
            return 'pc wins'
        else:
            return 'empate'

    game_pc = pc_choice()
    print(game_pc)
    print(game(game_pc, user))

    if puntos_pc == 2:
        break
        print('PC llego a 2 puntos, entonces GANA')
    elif puntos_user == 2:
        print('USER llego a 2 puntos, entonces GANA')
        break
