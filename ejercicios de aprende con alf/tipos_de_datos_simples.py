"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""
# num1 = int(input("Ingrese un número entero: "))
# num2 = int(input("Ingrese otro número entero: "))
# cociente = num1 / num2
# resto = num1 % num2
# print(f"El cociente entre el número {num1} y el número {num2} es {cociente} y su resto es {resto}")


"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""
# monto_para_invertir = float(input("Escriba la cantidad ha invertir: "))
# interes_anual = float(input("Interés procentual anual?: "))
# tiempo_a_invertir = int(input("Cuantos años invertirá?:"))
# formula = round(monto_para_invertir * (interes_anual / 100 + 1) ** tiempo_a_invertir,2)
# print(f"Capital final: {formula}")


"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
"""
# peso_payasos = 112
# peso_muñeca = 75
# payasos = int(input("Introduce el número de payasos a enviar: "))
# muñecas = int(input("Introduce el número de muñecas a enviar: "))
# peso_total = peso_payasos * payasos + peso_muñeca * muñecas
# print(f"El peso total del paquete es de {peso_total}")

"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
# inversion = float(input("Introduce la inversión inicial: "))
# interes = 0.04
# balance1 = inversion * (1 +  interes)
# print("Balance tras el primer año:" + str(round(balance1, 2)))
# balance2 = balance1 * (1 +  interes)
# print("Balance tras el primer año:" + str(round(balance2, 2)))
# balance3 = balance2 * (1 +  interes)
# print("Balance tras el primer año:" + str(round(balance3, 2)))

"""
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""
"""
A revisar este ejercicio.
"""
# pan_del_dia = 3.49
# descuento = 0.6
# pan_no_fresco = round(descuento * pan_del_dia / 100,2)
# cant_barra_de_pan = int(input("Cantidad de barras de pan vendidas: "))
# print(f"Se han vendido {cant_barra_de_pan} del día anterior, precio de pan fresco es de {pan_del_dia}. Al no ser del día, es de {pan_no_fresco}. Coste final es de: ")
