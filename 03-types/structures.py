pismena = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'd', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
user_text = str(input("Zadejte text: "))
i = 0
j =0


def count_vse(str_obj):
    pocet = 0
    for elem in str_obj:
        if elem.isupper():
            pocet += 1
        elif elem.islower():
            pocet += 1
        else:
            pocet += 1
    return pocet


pocet = count_vse(user_text)
# print(pocet)
while i in range(0,pocet):
     # print("j",j)
     if pismena[j] in user_text:
          print(f'\t{pismena[j]} : {user_text.count(pismena[j])}\n')
     j+=1
     # print("i",i)
     i+=1






# if 'a' in user_text:
#     print(f'\tA : {user_text.count("a")}\n')
# if 'b' in user_text:
#     print(f'\tB : {user_text.count("b")}\n')
# if 'c' in user_text:
#     print(f'\tC : {user_text.count("c")}\n')
# if 'd' in user_text:
#     print(f'\tD : {user_text.count("d")}\n')
# if 'e' in user_text:
#     print(f'\tE : {user_text.count("e")}\n')
# if 'f' in user_text:
#     print(f'\tF : {user_text.count("f")}\n')
# if 'g' in user_text:
#     print(f'\tG : {user_text.count("g")}\n')
# if 'h' in user_text:
#     print(f'\tH : {user_text.count("h")}\n')
# if 'i' in user_text:
#     print(f'\tI : {user_text.count("i")}\n')
# if 'j' in user_text:
#     print(f'\tJ : {user_text.count("j")}\n')
# if 'k' in user_text:
#     print(f'\tK : {user_text.count("k")}\n')
# if 'l' in user_text:
#     print(f'\tL : {user_text.count("l")}\n')
# if 'm' in user_text:
#     print(f'\tM : {user_text.count("m")}\n')
# if 'n' in user_text:
#     print(f'\tN : {user_text.count("n")}\n')
# if 'o' in user_text:
#     print(f'\tO : {user_text.count("o")}\n')
# if 'p' in user_text:
#     print(f'\tP : {user_text.count("p")}\n')
# if 'q' in user_text:
#     print(f'\tQ : {user_text.count("q")}\n')
# if 'r' in user_text:
#     print(f'\tR : {user_text.count("r")}\n')
# if 'd' in user_text:
#     print(f'\tS : {user_text.count("s")}\n')
# if 't' in user_text:
#     print(f'\tT : {user_text.count("t")}\n')
# if 'u' in user_text:
#     print(f'\tU : {user_text.count("u")}\n')
# if 'v' in user_text:
#     print(f'\tV : {user_text.count("v")}\n')
# if 'w' in user_text:
#     print(f'\tW : {user_text.count("w")}\n')
# if 'x' in user_text:
#     print(f'\tX : {user_text.count("x")}\n')
# if 'y' in user_text:
#     print(f'\tY : {user_text.count("y")}\n')
# if 'z' in user_text:
#     print(f'\tZ : {user_text.count("z")}\n')
