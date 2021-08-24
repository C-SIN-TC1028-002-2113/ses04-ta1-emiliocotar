def main():
    #escribe tu código abajo de esta línea
    x = int(input("Ingresa la medida del lado 1: "))
    y = int(input("Ingresa la medida del lado 2: "))
    z = int(input("Ingresa la medida del lado 3: "))

    if not (x+y<z or x+z<y or y+z<x):
        if x==y and x==z:
            print("ES UN TRIANGULO EQUILATERO")
        elif x!=y and x!=z and y!=z:
            print("ES UN TRIANGULO ESCALENO")
        elif x==z and x!=y or y==x and x!=z or y==z and y!=x:
            print("ES UN TRIANGULO ISOSCELES")
    else:
        print("NO ES TRIANGULO")
if __name__=='__main__':
    main()
