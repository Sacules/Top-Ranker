# La idea es hacer ésto en partes: primero, un programa que me toma una list de strings, y, según su ubicación, guarde cada string en un diccionario y le asigne un valor correspondiente. Luego, al darle otra string, comprueba si cada elemento está en el diccionario. Si está, le suma al valor el que le corresponde, si no, añade la string al diccionario.

# Último, una función, que dado un diccionario, imprime las keys basado en el orden de los values de mayor a menor.

# PS: Hacer un programa que le pida al usuario ingresar una list de strings, o que la lea de un archivo de texto.

# Hacer un loop que le pida al usuario si quiere ver la list de juegos, si quiere agregar una list, y si salir del mismo.

# ------------------------------------------------------------- #

# Funciones #
def loads_list(n): # agregar confirmacion de si la lista está correcta y permitir rehacerla
    print("Enter the list, one item at a time, per line.\n")
    ls = []
    while True:
        loader = input()
        ls.append(loader)

        if len(ls) == n:
            print()
            break

    return ls

def loads_list2(n):
    text_list = input('Insert the name of the file to read (without the extension):\n\n')
    source = open(text_list + '.txt', 'r') # Text file with the items
    item_list = []

    print('\n\n')

    for line in source:
        item = line.strip()
        item_list.append(item)

        if len(item_list) == n:
            break

    return item_list

def agrega_lista(ls,dic):
    """Dada una list de strings, guarda cada elemento en un diccionario y le asigna un valor según su ranking.

    ls = list de strings.
    dic = diccionario."""

    ls.reverse()

    for i in range(len(ls)):
        juego = ls[i]
        if juego not in dic:
            dic[juego] = i + 1
        else:
            dic[juego] += i + 1

def imprime_top(dic,n,t):
    """Imprime cada elemento del top en orden de mayor puntaje a menor.

    dic = diccionario con los tops.
    n = cantidad  de elementos a imprimir
    t = string, tipo de elementos del top i.e. juegos, albumes etc"""

    # Algunas variables
    fout = open('Top ' + str(n) + ' ' + str(t) + 's.txt','w')
    i = 1
    tab = "                                                                                                "
    first_line = "N°   " + t + " " * (len(tab) - len(str(t))) + "Score"

    #Imprime la primeras dos líneas
    bar = "-" * len(first_line)
    fout.write(first_line)
    fout.write("\n")
    fout.write(bar)
    fout.write("\n")

    # Imprime la lista en orden decreciente
    for item in sorted(dic, key=dic.get, reverse=True):
        if i < 10:
            line = str(i) + ".   " + item + " "*(len(tab) - len(str(item))) + str(dic[item])
            fout.write(line)
            fout.write("\n")
        elif i < 100:
            line2 = str(i) + ".  " + item + " "*(len(tab) - len(str(item))) + str(dic[item])
            fout.write(line2)
            fout.write("\n")
        else:
            line3 = str(i) + ". " + item + " "*(len(tab) - len(str(item))) + str(dic[item])
            fout.write(line3)
            fout.write("\n")

        if i == n:
            break

        i += 1

# Testeo
if __name__ == '__main__':
    score_acum = dict()

    print("Welcome to the Top Tanker!")

    print("Please enter what kind of top you're doing (Game, Album, Movie, etc) in singular:\n")

    kind_top = input()

    print("\nNow enter how many items your top will have (10, 25, 50, 100, etc):\n") 

    num_top = int(input())
    print()

    while True:

        ls = loads_list2(num_top) # Carga la lista a una string

        agrega_lista(ls,score_acum) # Agrega los elementos al diccionario

        imprime_top(score_acum,num_top,kind_top) # Imprime y guarda en un archivo los n elementos del diccinario en orden decreciente

        choice = input('Would you like to add another list of the same kind? (y/n)\n\n')
        print('\n')

        if choice.lower() == 'n' or choice.lower() == 'no':
            break
