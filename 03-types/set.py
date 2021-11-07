'''
 Set je množina jedinečných hodnot
 Set je množina, která je neseřazená a neoznačená.
 V pythonu se sety píšou s křivými závorkami.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaný seznam hodnot: {chars}')
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile je set vytvořen, nejdou hodnoty změnit, jdou pouze přidat.
# k přidání jedné položky použijeme add() metodu.
set_chars.add('V')

# K přidání více než jedné položky použijeme update() metodu.
set_chars.update('X', 'Y', 'Z')

# K odstranění používáme remove() nebo discard() metody.
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metody clear() vyčistí set
set_chars.clear()

# Slovo del smaže set kompletně:
del set_chars

# Přístup k hodnotám množiny
# V setu se nemůžeme k položkám dostat odkázáním na jejich index, jelikož set je neseřazený a bez indexů.
# my_set[1]

# Můžeme udělat smyčku a projít set použitím in metody
print('rady')
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
