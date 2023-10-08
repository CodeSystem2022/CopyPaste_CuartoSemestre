# dar formato a un string

nombre = 'Ariel'
edad = 28
mensaje_con_formato = 'Mi nombre es %s y tengo %d años' % (nombre, edad)
# print(mensaje_con_formato)

#Creamos una tupla
persona = ('Noelia', 'Ruiz', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f' #% persona #le pasamos la tupla persona
# print(mensaje_con_formato % persona) #podemos pasarlo en el print directamente

nombre = 'Juan'
edad = 19
sueldo = 3000

# se puede modificar el orden ya que manejamos índices.
mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

diccionario = {'nombre': 'Ivan', 'edad': 35, 'sueldo': 8000.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo{dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)