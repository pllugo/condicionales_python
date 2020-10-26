#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Pedro Luis Lugo García"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda

    if numero_1 > numero_2:
        print("El", numero_1, "es mayor que", numero_2)
    else:
        if numero_2 > numero_1:
            print("El", numero_2, "es mayor que", numero_1)
        else:
            print("Los números son iguales")

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if numero_1 > 0:
        print("El número", numero_1, "es positivo")
    elif numero_1 < 0:
        print("El número", numero_1, "es negativo")
    else:
        print("El numero es cero")
        
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if numero_1 == 0:
        print("El número es 0")
    else:
        if numero_1 == 100:
            print("El número es 100")
        else:
            if numero_1 > 0 and numero_1 < 100:
                print("El número_1 es > 0 y < 100")
            else:
                print("El numero_1 no esta entre 0 y 100")
        
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if numero_1 < 10 or numero_2 > -2:
        print("El numero_1 es < 10 o número_2 es > -2")
        if numero_1 < 10:
            print("El numero_1 es < 10")
        elif numero_1 == 10:
            print("el numero_1 es = 10")
        else:
            print("El numero_1 es > 10")
        if numero_2 > -2:
            print("El numero_2 es > -2")
        elif numero_2 == -2:
            print("el numero_2 es = -2")
        else:
            print("El numero_2 es < -2")
    else:
        print("El numero_1 > 10 o numero_2 < -2")
        if numero_1 < 10:
            print("El numero_1 es < 10")
        elif numero_1 == 10:
            print("el numero_1 es = 10")
        else:
            print("El numero_1 es > 10")
        if numero_2 > -2:
            print("El numero_2 es > -2")
        elif numero_2 == -2:
            print("el numero_2 es = -2")
        else:
            print("El numero_2 es < -2")

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("La palabra", texto_1, "es mayor a", texto_2, "Segun codigo ASCII")
        print("La palabra {} es alfabeticamente mayor a {}".format(texto_2,texto_1))
    else:
        print('{} es menor que {} Segun codigo ASCII'.format(texto_1, texto_2))
        print("La palabra {} alfabeticamente mayor a {}".format(texto_1,texto_2))
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    if len(texto_1) > len(texto_2):
        print("La palabra", texto_1, "contiene más letras que", texto_2)
    else:
        if len(texto_1) == len(texto_2):
            print("La palabra", texto_1, "tiene la misma cantidad de letras que", texto_2)
        else:
            print("La palabra", texto_2, "tiene mas letras que", texto_1)

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    if texto_1[0] > texto_2[0]:
        print("Segun codigo ASCII, la primera letra de {} es = {} , la cual es mayor a la primera letra de {} que es = {}".format(texto_1,
                                                                                                                            texto_1[0],
                                                                                                                            texto_2,
                                                                                                                            texto_2[0]))
    else:
        print("Segun codigo ASCII, la primera letra de {} es = {} , la cual es mayor a la primera letra de {} que es = {}".format(texto_2,
                                                                                                                            texto_2[0],
                                                                                                                            texto_1,
                                                                                                                            texto_1[0]))

    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1:
        print("La copia de la variable", copia_texto_1, "es igual a", texto_1)
    else:
        print("La palabra {} es diferente a {}".format(copia_texto_1,texto_2))
    

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 != texto_2:
        print("La copia de {} es diferente a {}".format(copia_texto_1,texto_2))
    else:
        print("La copia de la variable {} es igual, manor o mayor {}".format(copia_texto_1,texto_2))

def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if numero_1 > 5:
        if numero_2 > 0:
            print("Resp=1")
        else:
            print("Resp=2")
    else:
        if numero_2 > 5:
            print("Resp=3")
        else:
            print("Resp4")
        
    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    if puntaje >= 90:
        print("Calificación es: A")
    else:
        if puntaje >= 80:
            print("Calificación es: B")
        else:
            if puntaje >= 70:
                print("Calificación es: C")
            else:
                if puntaje >= 60:
                    print("Calificación es: D")
                else: 
                    print("Calificación es: F") #En éste punto ya el puntaje es menor a 60
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados


def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print("El texto {} es mayor a {}".format(texto_1,texto_2))
    else:
        print("El texto {} es menor a {}".format(texto_1,texto_2))
    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    numero_texto_1 = int(texto_1)
    numero_texto_2 = int(texto_2)

    if numero_texto_1 > numero_texto_2:
        print("El número {} es mayor a {}".format(numero_texto_1,numero_texto_2))
    else:
        print("El número {} es menor a {}".format(numero_texto_1,numero_texto_2))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
