# El metodo split sginifiva dividir/separar

# help(str.split)

cursos = 'Java Javascript Node Python Diseno'
lista_cursos = cursos.split()
print(f'Lista de cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java,Python,Node,Javascript,Spring'
lista_cursos = cursos_separados_coma.split(',', 2) # Busca la separacion de , solo 2 veces
print(f'Lista de cursos: {lista_cursos}')
print(len(lista_cursos))