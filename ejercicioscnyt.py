import math

def suma(x, y):
    sumaReales = x[0] + y[0]
    sumaImaginarios = x[1] + y[1]
    return (sumaReales, sumaImaginarios)

def producto(x, y):
    productoa = (x[0] * y[0]) - (x[1] * y[1])
    productob = (x[0] * y[1]) + (x[1] * y[0])
    return (productoa, productob)

def resta(x, y):
    restaReales = x[0] - y[0]
    restaImaginarios = x[1] - y[1]
    return (restaReales, restaImaginarios)

def division(x, y):
    parteReal = ((x[0] * y[0]) + (x[1] * y[1])) / (y[0]**2 + y[1]**2)
    parteImaginaria = ((y[0] * x[1]) - (x[0] * y[1])) / (y[0]**2 + y[1]**2)
    return (parteReal, parteImaginaria)

def modulo1(x):
    modulo = ((x[0]**2) + (x[1]**2))**(1/2)
    return modulo

def modulo2(x, y):
    modulo2 = ((x[0]**2) * (x[1]**2)) + ((y[0]**2) * (y[1]**2)) + ((x[0]**2) * (y[1]**2)) + ((x[1]**2) * (y[0]**2))
    return modulo2

def conjugado(x):
    return (x[0], x[1] * (-1))

def polarAcartesiano(x):
    a = x[0] * math.cos(x[1])
    b = x[0] * math.sin(x[1])
    return (a, b)

def cartesianoApolar(x):
    c = modulo1(x)
    angulo = math.atan2(x[1], x[0])
    return (c, angulo)

def fase(x):
    fase = math.atan2(x[1], x[0])
    return fase

def main():
    print("PRUEBA")
    print("SUMA")
    print("suma 1",suma((4,-1),(6,-5)))
    print("suma 2",suma((1,-8),(3,2)))

    print("\nPRODUCTO")
    print("producto 1",producto((4,-1),(6,-5)))
    print("producto 2",producto((1,-8),(3,2)))

    print("\nRESTA")
    print("resta 1",resta((4,-1),(6,-5)))
    print("resta 2",resta((1,-8),(3,2)))

    print("\nDIVISION")
    print("division 1",division((4,-1),(6,-5)))
    print("division 2",division((1,-8),(3,2)))

    print("\nMODULO 1")
    print("modulo 1",modulo1((4,-2)))
    print("modulo 2",modulo1((-1,7)))


    print("\nCONJUGADO")
    print("conjugado 1",conjugado((4,-2)))
    print("conjugado 2",conjugado((-1,7)))

    print("\nPOLAR A CARTESIANO")
    print("polarAcartesiano 1",polarAcartesiano((4,math.pi/5)))
    print("polarAcartesiano 2",polarAcartesiano((2,math.pi/2)))

    print("\nCARTESIANO A POLAR")
    print("cartesianoApolar 1",cartesianoApolar((4,-2)))
    print("cartesianoApolar 2",cartesianoApolar((-1,7)))

    print("\nFASE")
    print("fase 1",fase((4,-2)))
    print("fase 2",fase((-1,7)))

main()


    
