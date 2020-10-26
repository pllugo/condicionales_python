#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Pedro Luis Lugo Garcia"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''

    numero_1 = float(input('Ingrese el primer número:\n'))
    numero_2 = float(input("Ingrese el segundo número:\n"))

    restar = numero_1 - numero_2
    if restar > 0:
        print("El resultado de restar {} - {} =".format(numero_1,numero_2), restar)
    else:
        if restar < 0:
            print("El resultado de restar {} - {} =".format(numero_1,numero_2), restar)
        else:
            print("El resultado de restar {} - {} =".format(numero_1,numero_2), restar)

# Para saber si un número es par
def par(n1):

    if n1 % 2 == 0: #Si el resto = 0 entonces es par
        print("{} Es par".format(n1))
    else:
        print("{} Es impar".format(n1))

# Función para saber el orden de las palabras según orden de palabras
def alfabetico(palabra_1,palabra_2,palabra_3):
    if (palabra_1 > palabra_2) and (palabra_1 > palabra_3):
        if (palabra_2 > palabra_3):
            print("El orden según ASCII es: {} , {} , {}".format(palabra_1,palabra_2,palabra_3))
            print("El orden alfabetico es: {} , {} , {}".format(palabra_3,palabra_2,palabra_1))
        else:
            print("El orden SEGÚN ASCII es: {} , {} , {}".format(palabra_1,palabra_3,palabra_2))
            print("El orden alfabetico es: {} , {} , {}".format(palabra_2,palabra_3,palabra_1))
    else:
        if (palabra_2 > palabra_1) and (palabra_2 > palabra_3):
            if (palabra_1 > palabra_3):
                print("El orden según ASCII es: {} , {} , {}".format(palabra_2,palabra_1,palabra_3))
                print("El orden alfabetico es: {} , {} , {}".format(palabra_3,palabra_1,palabra_2))
            else:
                print("El orden según ASCII es: {} , {} , {}".format(palabra_2,palabra_3,palabra_1))
                print("El orden alfabetico es: {} , {} , {}".format(palabra_1,palabra_3,palabra_2))
        else:
            if (palabra_3 > palabra_1) and (palabra_3 > palabra_2):
                if palabra_1 > palabra_2:
                    print("El orden según ASCII es: {} , {} , {}".format(palabra_3,palabra_1,palabra_2))
                    print("El orden alfabetico es: {} , {} , {}".format(palabra_2,palabra_1,palabra_3))
                else:
                    print("El orden según ASCII es: {} , {} , {}".format(palabra_3,palabra_2,palabra_1))
                    print("El orden alfabetico es: {} , {} , {}".format(palabra_1,palabra_2,palabra_3))

# Función para saber el orden de las palabras según número de letras
def numero(palabra_1,palabra_2,palabra_3):
    if (len(palabra_1) > len(palabra_2)) and (len(palabra_1) > len(palabra_3)):
        if (len(palabra_2) > len(palabra_3)):
            print("El orden es: {} , {} , {}".format(palabra_1,palabra_2,palabra_3))
        else:
            print("El orden es: {} , {} , {}".format(palabra_1,palabra_3,palabra_2))
    else:
        if (len(palabra_2) > len(palabra_1)) and (len(palabra_2) > len(palabra_3)):
            if (len(palabra_1) > len(palabra_3)):
                print("El orden es: {} , {} , {}".format(palabra_2,palabra_1,palabra_3))
            else:
                print("El orden es: {} , {} , {}".format(palabra_2,palabra_3,palabra_1))
        else:
            if (len(palabra_3) > len(palabra_1)) and (len(palabra_3) > len(palabra_2)):
                if len(palabra_1) > len(palabra_2):
                    print("El orden es: {} , {} , {}".format(palabra_3,palabra_1,palabra_2))
                else:
                    print("El orden es: {} , {} , {}".format(palabra_3,palabra_2,palabra_1))

def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input("Ingrese el primer número:\n"))
    numero_2 = int(input("Ingrese el segundo número:\n"))
    numero_3 = int(input("Ingrese el tercer número:\n"))
    # Este ejercicio se puede hacer mejor llamando a una sola función para saber si es par o no
    # La función la llame par
    par(numero_1)
    par(numero_2)
    par(numero_3)



def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_1 = float(input("Ingrese el primer número:\n"))
    numero_2 = float(input("Ingrese el segundo número:\n"))
    operacion = input(("""Ingrese la operación que desee realizar: 
    suma(+) 
    Resta(-) 
    Multiplicación(*) 
    División(/) 
    Exponente/Potencia (**)
    Por favor, indique: """))
    if operacion == "+":
        print("El resultado de la suma es:", numero_1 + numero_2)
    else:
        if operacion == "-":
            print("El resultado de la resta es:", numero_1 - numero_2)
        else:
            if operacion == "*":
                print("El resultado de la multiplicación es:", numero_1 * numero_2)
            else:
                if operacion == "/":
                    print("El resultado de la división es:", numero_1 / numero_2)
                else:
                    print("El resultado del exponente/potencia es:", numero_1 ** numero_2)


def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''

    texto_1 = str(input("Ingresar la palabra 1:\n"))
    texto_2 = str(input("Ingresar la palabra 2:\n"))
    texto_3 = str(input("Ingresar la palabra 3:\n"))

    orden = int(input ("""Ingrese 1 si quiere ordenar las palabras por orden alfabetico
                        Ingrese 2 si quiere ordenar por cantidad de letras :\n"""))
    
    #Este ejercicio lo resolvi haciendo funciones que llamo antes 
    # alfabetico y numero, para ahorrar codigo

    if orden == 1:
        print("Ordenar por orden alfabetico")
        alfabetico(texto_1,texto_2,texto_3) #Llamo una función que antes hice antes
    else:
        print("Ordenar por números de letras")
        numero(texto_1,texto_2,texto_3) #Llamo una función que antes hice antes
    
    


    


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    temp_1 = float(input("Ingrese la temperatura 1:\n"))
    temp_2 = float(input("Ingrese la temperatura 2:\n"))
    temp_3 = float(input("Ingrese la temperatura 3:\n"))


    # Para la máxima temperatura, lo resuelvo de dos formas una corta y una larga
    # La forma corta, es que tomo el primer valor como el mayor y lo comparo
    # con los otros dos valores y sustituyo cuando un valor es mayor al otro
    
    # Calcular la mayor temperatura de forma corta
    mayor = temp_1
    if (mayor > temp_2) and (mayor > temp_3):
        print("El mayor es", mayor)
    else:
        if mayor > temp_2:
            print("La temperatura mayor es", temp_3)
        else:
            mayor = temp_2
            if mayor > temp_3:
                print("El mayor es",mayor)
            else:
                print("El mayor es", temp_3)
    
    # Calcular la menor temperatura de forma corta
    menor = temp_1
    if (menor < temp_2) and (menor < temp_3):
        print("El menor es", menor)
    else:
        if menor < temp_2:
            print("La temperatura menor es", temp_3)
        else:
            menor = temp_2
            if menor < temp_3:
                print("El menor es",menor)
            else:
                print("El menor es", temp_3)


    # Esta es la forma larga en donde comparo todos los valores para encontrar
    # el mayor valor
    if temp_1 > temp_2 and temp_1 > temp_3:
        if temp_2 == temp_3:
            print("La temperatura 2 {} = temperatura 3 {}".format(temp_2,temp_3))
        else:
            print("La mayor temperatura es:", temp_1)
    else:
        if temp_2 > temp_1 and temp_2 > temp_3:
            if temp_1 == temp_3:
                print("La temperatura 1 {} = temperatura 3 {}".format(temp_1,temp_3))
            else:
                print("La mayor temperatura es:", temp_2)
        else:
            if temp_3 > temp_2 and temp_3 > temp_1:
                if temp_1 == temp_2:
                    print("La temperatura 1 {} = temperatura 2 {}".format(temp_1,temp_2))
                else:
                    print("La mayor temperatura es:", temp_3)
            else:
                if temp_1 == temp_2 and temp_1 == temp_3:
                    print("La temperatura {} es = {} = {}".format(temp_1,temp_2,temp_3))
                else:
                    if temp_1 == temp_2:
                        print("La temperatura 1 {} = a la temperatura 2 {}".format(temp_1,temp_2))
                        if temp_1 > temp_3:
                            print("La temperatura mayor es", temp_1)
                        else:
                            print("La temperatura mayor es", temp_3)
                    else:
                        if temp_1 == temp_3:
                            print("La temperatura 1 {} = a la temperatura 3 {}".format(temp_1,temp_3))
                            if temp_1 > temp_2:
                                print("La mayor temperatura es", temp_1)
                            else:
                                print("La mayor temperatura es", temp_2)
                        else:
                            print("La temperatura 2 {} = a la temperatura 3 {}".format(temp_2,temp_3))
                            if temp_2 > temp_1:
                                print("La mayor temperatura es",temp_2)
                            else:
                                print("La mayor temperatura es", temp_1)
    
    #Calculo del promedio de las temperaturas
    promedio = (temp_1 + temp_2 + temp_3) / 3
    print("El promedio es:", round(promedio,2)) #La función round() redondea el valor de un número float
        




if __name__ == '__main__':
    print("Ejercicios de práctica")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
