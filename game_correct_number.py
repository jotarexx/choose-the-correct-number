def run():
    numero_aleatorio = random.randint(1,51)
    numero_elegido = int(input('choose a number from 1 to 50: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('look for a bigger number')
        else:
            print('look for a smaller number')
        numero_elegido = int(input('choose another number: '))
    print('Ganaste!')


if __name__ == "__main__":
    run()
