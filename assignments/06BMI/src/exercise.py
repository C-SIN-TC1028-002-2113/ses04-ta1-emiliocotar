def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    indice=peso/altura**2

    if peso<=0 or altura<=0:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    elif indice<20:
        print("PESO BAJO")
    elif indice>=20 and indice<25:
        print("NORMAL")
    elif indice>=25 and indice<30:
        print("SOBREPESO")
    elif indice>=30 and indice<35:
        print("OBESIDAD")
    else:
        print("OBESIDAD MORBIDA")

if __name__=='__main__':
    main()