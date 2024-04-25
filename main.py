import random
from tree import BinaryTree
from typing import TypeVar


T = TypeVar('T')

#creacuin de los documentos
def crear_archivos():
    palabras = ['hola mundo', 'pan con cafe', 'abeja', 'hola como estas', 'Pan', 'Ganar', 'Espero que funcione', 'Que bueno', 'feliz', 'zanahoria para la vista', 'juego']
    cantidad = 9
    for i in range(10):
        with open(f'{i + 1}', 'w') as archivo:
            word = random.randint(0, cantidad)
            archivo.write(f'{palabras[word]} ')
            palabras.remove(palabras[word])
            cantidad -= 1

#colocar la cantidad de palablras que hay en el docuumento
def verificado(contador):
    for i in range (1, contador + 1):
        with open(f'{i}', 'r') as archivo:
            contenido = archivo.read()
            word = ''
            for j in contenido:
                word += j
                if j == ' ':
                    word1 = ''
                    catidad = 0
                    for k in contenido:
                        word1 += k
                        if k == ' ':
                            if str(word) == str(word1):
                                catidad += 1
                                word1 = ''
                            else:
                                word1 = ''
                    with open(f'{i}', 'a') as archivo:
                        archivo.write(f'\n {word}: {catidad}')
                    word = ''


def main():
    print('Bienvenido al programa')
    tree = T
    crear_archivos()
    verificado(10)
    cantidad = 10
    #agragar los documentos a un arbol
    for i in range(cantidad):
        with open(f'{i + 1}', 'r') as archivo:
            contenido = archivo.read()
        if i == 0:
            tree = BinaryTree(contenido)
        else:
            tree.insert_at(contenido)
    print('Los archivos actuales son: ')
    tree.print_inorder(tree.root)
    #buscar la palabra en los documentos
    word = str(input('Ingresa la palabra que quieras buscar: '))
    tree.search_file(word)
    print(tree.filles)

main()
