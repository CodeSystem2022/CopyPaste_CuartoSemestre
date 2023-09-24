
# STRING INMUTABLES - Las variables que tienen cadenas, no pueden modificarse sino que se crea una nueva

# help(str.capitalize) # convierte el primer caracter a mayúscula

mensaje1 = "hola mundo"
mensaje2 = mensaje1.capitalize()

print(f'Mensaje1: {mensaje1}, id: {id(mensaje1)}') 
print(f'Mensaje2: {mensaje2}, id: {id(mensaje2)}') 

mensaje1 += ' Adiós' 
print(f'Mensaje1: {mensaje1}, id: {id(mensaje1)}') 