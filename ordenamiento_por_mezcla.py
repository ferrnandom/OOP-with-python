# import random 

# def ordenamiento_por_mezcla(lista):
#     if len(lista) > 1:#se ejecuta si todavia podemos seguir dividiendo en trozos mas pequeños
#         medio = len(lista) // 2 # // para ignorar los decimales
#         izquierda = lista[:medio]
#         derecha = lista[medio:]
#         print(derecha)
#         print( '*' * 20)
#         print(izquierda)

#         #llamda recursiva en cada mitad
#         ordenamiento_por_mezcla(izquierda)
#         ordenamiento_por_mezcla(derecha)

#         #iteradores para recorrer las dos sublistas
#         i = 0 #elementos mitad izquierda
#         j= 0 #elementos mitad derecha

#         #iterador para lista principal
#         k = 0

#         while i < len(izquierda) and j < len(derecha):
#             if izquierda[i] < derecha[j]:
#                 lista[k] = izquierda[i]
#                 i += 1
#             else:
#                 lista[k] = derecha[j]
#                 j += 1
            
#             k += 1

#         while i < len(izquierda):
#             lista[k] = izquierda[i]
#             i += 1
#             k +=1

#         while j < len(derecha):
#             lista[k] = derecha[j]
#             j += 1
#             k += 1
#         print(f'La izquierda: {izquierda},la derecha {derecha}')
#         print(lista)
#         print('*' * 5)
#     return lista
        


# if __name__ == '__main__':
#     tamaño_lista = int(input('De que tamaño quieres la lista?? '))

#     lista = [random.randint(0,100) for elements in range(tamaño_lista)]
#     print('La lista orginal desordenada es: ')
#     print(lista)
#     print('-' * 20)
#     print('Esta es la lista ordenada: ')

#     lista_ordenada = ordenamiento_por_mezcla(lista)
#     print(lista_ordenada)

# def ordenamiento_por_mezcla(lista):
#     #caso base
#     #parte 1 que consiste en dividir la lista inicial 
#     #hasta que queden de longitud 1.

#     #el codigo de este condicional se ejecutara siempre
#     #que la lista sea mayor a 1. cuando ya no sea mayor
#     #a uno simplemente se retorna la lista
#     if len(lista) > 1:
#         medio = len(lista) // 2
#         izquierda = lista[:medio]
#         derecha = lista[medio:]

#         #llamada recursiva en cada mitad
#         ordenamiento_por_mezcla(izquierda)
#         ordenamiento_por_mezcla(derecha)

#         #iteradores para recorrer las dos sublistas.
#         #estos son como elementos en las sublistas
#         #estos son los indeces de la lista
#         i = 0
#         j = 0
#         #iterador para iterar en la lista principal
#         k = 0


#         #mientras los elementos de la derecha e izquierda
#         #sean mayores a la longitudes de la lista, es decir,
#         #mientras hayan elementos en las dos listas se ejecutara
#         #el codigo
#         #mientras que el elemento i sea mas pequeño que
#         #
#         while i < len(izquierda) and j < len(derecha):
#             #mientras el indice de la lista sea menor que la 
#             #longitud de la lista sigo iterando
#             if izquierda[i] < derecha[j]:
#                 lista[k] = izquierda[i]
#                 #aumentamos en 1 en cada iteracion para que
#                 #los elementos se coloquen en el lugar adecuado
#                 i += 1
#             elif derecha[j] < izquierda[i]:
#                 lista[k] = derecha[j]
#                 #aumentamos en uno en cada iteracion para que se coloque
#                 #en el lugar adecuado cada elemento
#                 j += 1
            

#             #para que en cada iteracion el indice de la 
#             #lista principal vaya aumentando
#             k += 1


            #la tercera parte del programa es unir los
            #pedazos de las listas que quedaron. Estos
            #pedazos ya estan ordenados y se ejecutan solo
            #cuando ya no se puede comparar porque los indices
            #son ya mas pequeños que la lista. es decir, el codigo
            #de atras no se ejecuta.

    #     while i < len(izquierda):
    #         izquierda[i] = lista[k]
    #         i += 1
    #         k +=1

    #     while j < len(derecha):
    #         derecha[j] = lista[k]
    #         j += 1
    #         k += 1
    # return lista





# def ordenamiento_por_mezcla(lista):
#     #mientras la longitud de la lista sea mayour a uno 
#     #vamos a seguir ejecutando el codigo, de lo contrario
#     #simplemente se retorna nada
#     if len(lista) > 1:
#         medio = len(lista) // 2

#         derecha = lista[medio:]
#         izquierda = lista[:medio]


#         ordenamiento_por_mezcla(izquierda)
#         ordenamiento_por_mezcla(derecha)



#         #ahora vamos a comparar

#         #voy a crear los indices de las lista para poder
#         #iterar con ellos

#         i = 0
#         j = 0
#         k = 0

#         while i < len(izquierda) and j < len(derecha):
#             if izquierda[i] < derecha[j]:
#                 lista[k] = izquierda[i]
#                 i += 1
#             else:#elif derecha[j] > izquierda[i]:
#                 #si la condicion se cumple entonces queremos
#                 #que la lista en en indice k se igual a el elemento
#                 #en el indice j
#                 lista[k] = derecha[j]
#                 j += 1
#             k += 1

#         #esta parte del codigo es por si queda un solo elemento
#         #en alguna de las dos listas. En este caso simplemente
#         #se junta con la lista principal
#         while i < len(izquierda):
#             lista[k] = izquierda[i]
#             i += 1
#             k += 1

#         while j < len(derecha):
#             lista[k] = derecha[j]
#             j += 1
#             k += 1

#         return lista

# print(ordenamiento_por_mezcla([2,58,8,7]))























import random 


def ordenamiento_por_mezcla(lista):
    #si la lista es mayor a uno directamente no se ejecuta
    if len(lista) > 1:
        #dividimos la lista en dos mitades
        medio = len(lista) // 2

        derecha = lista[medio:]
        izquierda = lista[:medio]

         #hacemos recursividad hasta que solo quedan listas
         #de un solo elemento
        ordenamiento_por_mezcla(derecha)
        ordenamiento_por_mezcla(izquierda)

        #estos son los elementos de las lista, a traves de 
        #ellos voy a iterar
        i = 0
        j = 0
        #este es el iterador de la lista principal
        k = 0
        

        #este loop se va a repetir siempre que el numero de 
        #elementos sea menor a la longitud de la lista, es de
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1

            elif derecha[j] < izquierda[i]:
                lista[k] = derecha[j]
                j += 1
            k += 1

        #este loop lo creamos para unir los pedazos que pueden 
        #quedar despues de las iteraciones
        while i < len(lista):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(lista):
            lista[k] = derecha[j]
            j += 1
            k += 1
        return lista



if __name__ == '__main__':
    tamaño_lista = int(input('de que tamaño quieres que sea la lista?? '))
    lista = [random.randint(0, tamaño_lista) for i in range(tamaño_lista)]
    print(ordenamiento_por_mezcla(lista))

