'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
V pythonu se tuples píšou s kulatými závorkami.
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# K vytvoření tuplu s pouze jednou položkou, musíme přidat čárku, jinak Python nepozná, že se jedná o tuple.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# Můžeme specifikovat rozptyl indexů.
# Tímto vznikne nový tuple s námi specifikovanými daty.
print(f'chars[2:5]: {chars[2:5]}')

# Negativní indexy znamenají, že začneme od konce. -1 je poslední, -2 předposlední atd.
# Specifikuj negativní indexy pokud chceš hledání začit od konce:
# Tento příklad vrátí položky od indexu -4 (včetně) do indexu -1 (už ne)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# K určení kolik má tuple položek použijeme len() metodu:
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
