import random
szamok = [-3, 5, 11, -2, 4]

def otodik(tomb):
    primek = []
    for i in tomb:
        for j in range(2, i):
            if not i % j:
                break
        else:
            if i > 0:
                primek.append(i)
    print(f"Prímek száma: {len(primek)}")



def negyedik(tomb):
    i = 0
    ketszamjegy = 0
    while i < len(tomb):
        if len(str(tomb[i])) == 2:
            ketszamjegy = i
            break
        i += 1
    print(f"Az első kétszámjegyű: {ketszamjegy}, értéke {tomb[ketszamjegy]} ")


def masodikfeladat(tomb):
    while True:
        utolsoelem = int(input("Kérem az utolsó elemet mely 3-mal osztható kétjegyű szám ami páratlan!"))
        if utolsoelem % 3 == 0 and utolsoelem % 2 != 0 and len(str(utolsoelem)) == 2:
            tomb.append(utolsoelem)
            break
    print(f"A tömb elemei: {tomb}")


def elsofeladat(tomb):
    tomb[0] += int(random.random() * 7) + 5
    print(f"Az első szám értéke {szamok[0]} -ra/re változott miután hozzáadtam egy véletlen számot 5 és 12 között.")


def elvalaszt(tomb):
    sep = str(input("Adjon meg szeparátort!"))
    i = 0
    szamok2 = ""
    while i < len(tomb)-1:
        szamok2 += str(tomb[i]) + sep
        i += 1
    szamok2 += str(tomb[i])
    return szamok2
    print(f"A tömb számai elválasztva {elvalasztva}")


elvalaszt(szamok)
elsofeladat(szamok)
masodikfeladat(szamok)
negyedik(szamok)
otodik(szamok)



