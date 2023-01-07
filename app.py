import random


def jugador():
    name_player = input(
        'Bienvenido al piedra, papel o tijera, indique su nombre para iniciar')

    return name_player


def maquina():
    valores = ['piedra', 'papel', 'tijera']
    get_valor = random.choice(valores)
    return get_valor


def game(name, maquina):
    puntos_jugador = 0
    puntos_maquina = 0
    flag = True
    game_player = input('Escoge piedra papel o tijera').lower()
    while flag:
        game_player = input('Escoge piedra papel o tijera').lower()
        if puntos_jugador == 3 or puntos_maquina == 3:
            flag = False
            if puntos_jugador == 3:
                resultado = f'El juego lo ha ganado {name}'
            else:
                resultado = 'el juego lo ha ganado la maquina'
        else:
            if maquina == 'piedra' and game_player == 'papel':
                puntos_jugador += 1
                resultado = f'{name} win'
            elif game_player == 'piedra' and maquina == 'papel':
                puntos_maquina += 1
                resultado = 'maquina wins'
            elif game_player == 'tijera' and maquina == 'piedra':
                puntos_maquina += 1
                resultado = 'maquina wins'
            elif game_player == 'piedra' and maquina == 'tijera':
                puntos_jugador += 1
                resultado = f'{name} win'
            elif game_player == 'tijera' and maquina == 'papel':
                puntos_jugador += 1
                resultado = f'{name} win'
            elif maquina == 'tijera' and game_player == 'papel':
                puntos_maquina += 1
                resultado = 'maquina wins'
            else:
                resultado = 'empate'
    return resultado


nombre_jugador = jugador()
eleccion_maquina = maquina()
juego = game(nombre_jugador, eleccion_maquina)

print(juego)
