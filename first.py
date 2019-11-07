#!/usr/bin/python3


# mettre des espaces (4 espaces) et pas de [tab]

print("hello world")

a = 1
if a==0:
    print("toto")
else:
    print("a ne vaut pas 0")


print("fin")

# un entier
entier = 1
# un float
fl = 1.5
# un string (chaine de caractère)
string = "chaine1"
string = 'chaine1'
string = """chaine1"""
string = '''chaine1'''

string = " il va dire \"coucou\" assf"
string = """ il va dire "coucou" assf """


# les commenaires
"""
les commentaires multilignes
sont avec des " "
"""

# 2 écritures équivalentes
stringadd = "aa" + "bb"
stringadd = "aa" "bb"
print("stringadd")

string = """coucou
salut
hello"""

if a == 0:
    string = ("coucou\n"
              "salut\n"
              "hello")



# nomenclateure "style guide" PEP8

alphabet = "abcdefghijklmnopqrstuvwxyz"

if 'a' in alphabet:
    print("j'ai trouvé a")

# tableau / list / array
alist = list()
alist = []
alist = ["a", "b"]

# une list de string
alist = ["0", "1", "2", "3", "4"]

# une list de int
alist = [0, 1, 2, 3, 4, 5]
for x in alist:
    print(x)
print(alist)
alist = range(5)
print(alist)
for x in alist:
    print(x)

for char in alphabet :
    print(char)

for st in alist:
    print(st)

print("le 3e elem")
print(alist[3])

alist = []
print(alist)
#ajout un element à la fin
alist.append("hello")
print(alist)
alist.append("hello")
print(alist)
alist.append("hello")
print(alist)
#supprime le dernier element ajoute
alist.pop()
print(alist)

blist = [ "salut", "salut"]
print(alist + blist)


adict = dict()
adict = {}
adict = {"fr" : "salut",
         "en" : "hello"}
print(adict)

print(adict["fr"])

lang = "fr"
print(adict[lang])


trad = {"fr" : "salut",
        "en" : "hello"}
print(trad[lang])

for key in trad:
    print(key)
    print(trad[key])

