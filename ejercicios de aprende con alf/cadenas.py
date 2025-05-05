"""
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

# nombre = input("Ingresa tu nombre: ")
# num = int(input("Introduce un número entero: "))
# print(f"{nombre}\n"* int(num))

"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

# nombre_completo = input("Ingresa tu nombre completo: ")
# print(f"Tu nombre es: {nombre_completo.lower()}")
# print(f"Tu nombre es: {nombre_completo.upper()}")
# print(f"Tu nombre es: {nombre_completo.title()}")

"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

# nombre = input("¿Como es tu nombre? ")
# num_caracteres = len(nombre)
# print(f"Tu nombre es {nombre.upper()} y tiene {num_caracteres} letras")

"""
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

# num_empresa = input("Ingrese el número de la empresa con el formato +xx-xxxxx-xx: ")
# print(f"El número de la empresa es {num_empresa[4:-3]}")

"""
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
"""

# frase = input("Ingrese una frase y la invertimos: ")
# print(f"Frase invertida: {frase[::-1]}")

"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
# frase = input("Escriba una frase: ")
# vocal = input("Ahora escriba una vocal: ")
# print(f"Frase: {frase} \nVocal: {vocal.upper()}")

"""
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
# correo_usuario = input("Ingrese su correo electrónico: ")
# print(correo_usuario[:correo_usuario.find('@')] + '@ceu.es')

"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
"""
# precio = input("Cual es el valor?: ")
# euros, centimos = precio.split(".")
# print(f"Euros: {euros}, Céntimos: {centimos}")
# O también la otra forma
# print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')

"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""
# fecha_nacimiento = input("Escriba su fecha de nacimiento en formato dd/mm/aaaa: ")
# dia, mes, año = fecha_nacimiento.split("/")
# print(f"Su fecha es: {dia}/{mes}/{año}")

"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""
# productos = input("Ingrese los productos de la cesta: ")
# lista_productos = productos.split(",")
# print("\nLista de productos:")
# for productos in lista_productos:
#    print(productos.strip())

"""
Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

# fruits = ('apple','banana','mango','cherry')
# (x,*y,z) = fruits

# print(y)

print('Hello', 'World')
