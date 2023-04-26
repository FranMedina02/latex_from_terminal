from sys import argv

def default_action():
    return 'Funcion default'

def hola():
    return 'Funcion Hola'

def matriz3x3(matriz):
    matriz = [int(i) for i in matriz]
    place_holder = ''
    for i in range(3):
        place_holder += str(matriz[(i*3):3*(i+1)]) + '\n'
    return place_holder

commands = {
    'hola':hola,
    'matriz':matriz3x3
}

print(commands.get(argv[1:][0], default_action)(argv[2:]))