# Functions #
import re
def titlecase(s): # Taken from the python docs, just to make sure capitalization isn't important
	return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo:  mo.group(0)[0].upper() + mo.group(0)[1:].lower(),s)

def load_list(n):
    """Turns a list in a text file with the items into a list with strings.
    Items are one per line, no symbols nor numbers. In descendent order.

    n: Number of items to read from the list."""

    text_list = input('Insert the name of the file to read (without the extension):\n\n')
    
    with open(text_list + '.txt',encoding='utf-8-sig') as source: # Text file with the items
        item_list = []  # Temporary list

        print()

        for line in source:
            item = line.strip()
            item_list.append(item)

            if len(item_list) == n:
                break

    return item_list

def add_list(ls,dic):
    """Reads a list with the items (strings) and saves them to a dictionary as keys.
    Assigns them a score (value) based on their position, with the first item getting the length of the list, and the last one a 1 (one).

    ls: String list with the items.
    dic: Dictionary in which to save the items and their score."""

    ls.reverse() # Since the list is in descending order, this will make things easier

    for i in range(len(ls)): # Starts with the last element of the original list, now it's the first one
        item = titlecase(ls[i])
        if item not in dic:
            dic[item] = i + 1
        else:
            dic[item] += i + 1

def item_line(tab,item,dic,i,n):
    return str(i) + "."+ " "*n + item + " "*(len(tab) - len(str(item))) + str(dic[item])

def save_top(dic,n,t):
    """Sorts the dictionary by value and prints the results to a text file.

    dic: Dictionary with the items and their scores.
    n: Number of items to print.
    t: Type of items to print (games, movies, books, etc)."""

    # Useful stuff
    with open('Top ' + str(n) + ' ' + str(t) + 's.txt','w',encoding='utf-8') as fout:# Resulting top
        i = 1
        tab = "                                                                                                "
        first_line = "N°   " + t + " " * (len(tab) - len(str(t))) + "Score"
        
        # Prints the first two lines
        bar = "-" * len(first_line)
        fout.write(first_line)
        fout.write("\n")
        fout.write(bar)
        fout.write("\n")

        # Prints the dictionary keys sorted by values
        for item in sorted(dic, key=dic.get, reverse=True):
            if i < 10:
                fout.write(item_line(tab,item,dic,i,3))
                fout.write("\n")
            elif i < 100: # Makes sure the items are all alligned when printed. Works up to 999 items.
                fout.write(item_line(tab,item,dic,i,2))
                fout.write("\n")
            else:
                fout.write(item_line(tab,item,dic,i,1))
                fout.write("\n")

            if i == n:
                    fout.close()
                    break

            i += 1
