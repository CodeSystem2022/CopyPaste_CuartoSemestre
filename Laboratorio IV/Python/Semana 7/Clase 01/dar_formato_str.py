# dar formato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mensaje_con_formato)

#Creamos una tupla
persona = ('Noelia', 'Ruiz', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' #% persona #le pasamos la tupla persona
print(mensaje_con_formato % persona) #podemos pasarlo en el print directamente