gul = 0
oransj = 0
blå = 0

høyremønster = 0
gultemp = 0
oransjtemp = 0
blåtemp = 0

venstremønster = 0
lilla = 0
rød = 0
grønn = 0

lyseblå = 0

lillatemp = 0
lillavenstre = False
lillahøyre = False
lillaførst = False
rødtemp = 0
grønntemp = 0

lyseblåtemp = 0
oransjførst = False
blåførst = False
midten2 = False


def main():
    global gul, oransj, blå, lilla, rød, grønn, lyseblå
    global gultemp, oransjtemp, blåtemp, lillatemp, rødtemp, grønntemp, lyseblåtemp
    global lillahøyre, lillavenstre, lillaførst
    global oransjførst, blåførst, midten2
    global venstremønster, høyremønster
    gultemp += gul
    oransjtemp += oransj
    blåtemp += blå

    lyseblåtemp += lyseblå

    lillatemp += lilla
    rødtemp += rød
    grønntemp += grønn
    if venstremønster == 2 and høyremønster == 8:
        print("nå er det sikkert 8 i høyden")

    if lilla == 1:
        print("det er lilla")
        if rødtemp == 1 and grønntemp != 2:
            print("det finnes 1 rød, lilla holdes")
            lillatemp -= 1
        elif grønntemp == 1 and rødtemp != 2:
            print("det finnes 1 grønn, lilla holdes")
            lillatemp -= 1

        elif rødtemp == 2 and not lillahøyre:
            print("det finnes 2 rød, lilla ned til høyre")
            lillahøyre = True
        elif grønntemp == 2 and not lillavenstre:
            print("det finnes 2 grønn, lilla ned til venstre")
            lillavenstre = True

        elif rødtemp == 4 and grønntemp == 4:
            print("det er 4 rød og 4 grønn, lilla snus opp ned")

        elif lillatemp == 1 and rødtemp == 0 and grønntemp == 0:
            print("det er lilla først, rett ned")
            lillaførst = True
        else:
            print("lilla kan ikke ned nå, lilla holdes")
            lillatemp -= 1

    if rød == 1:
        print("det er rød")
        if lillatemp == 0:
            print("rød først, rød holdes")
            rødtemp -= 1
        elif lillaførst and rødtemp != 3:
            print("det er lilla, rød ned til venstre")
        elif lillahøyre:
            print("det finnes lilla på høyre, rød ned til høyre")
        else:
            print("rød kan ikke nå, rød holdes")
            rødtemp -= 1
    if grønn == 1:
        print("det er grønn")
        if lillatemp == 0:
            print("grønn først, grønn holdes")
            grønntemp -= 1
        elif lillaførst and grønntemp != 3:
            print("det er lilla, grønn ned til høyre")
        elif lillavenstre:
            print("det finnes lilla på venstre, grønn ned til venstre")
        else:
            print("grønn kan ikke nå, grønn holdes")
            grønntemp -= 1
    if rødtemp == 4 and lillatemp == 4 and grønntemp == 4:
        print("venstre mønster fullført")
        lillatemp = 0
        rødtemp = 0
        grønntemp = 0
        venstremønster += 1

    if høyremønster == 8 and not midten2:
        if gul == 1:
            print("det er gul, figur 2")
            if oransjtemp == 0 and blåtemp == 0:
                print("gul først, ned i midten")
            if gultemp == 2:
                # bytt på denne
                print("det var gul i midten, gul holdes")
                gultemp -= 1
        if oransj == 1:
            print("det er oransj, figur 2")
            if blåtemp == 0:
                print("oransj før blå, den flate siden ned i midten")
                oransjførst = True
            if blåførst == 1:
                print("det finnes blå, oransj settes over blå")
        if blå == 1:
            print("det er blå, figur 2")
            if oransjtemp == 0:
                print("blå før oransj, den flate siden ned i midten")
                blåførst = True
            if oransjførst == 0:
                print("det finnes oransj, blå settes over oransj")
        if lyseblå == 1:
            print("det er lyseblå, figur 2")
            if oransjtemp == 0 and blåtemp == 0:
                print("det er lyseblåførst, den holdes")
                lyseblåtemp -= 1
            if oransjførst:
                print("det finnes oransj, lyseblå på oransj")
            if blåførst == 1:
                print("det finnes blå, lyseblå på blå")
        if gultemp == 1 and oransjtemp == 1 and blåtemp == 1 and lyseblåtemp == 1:
            print("midtfigur2 ferdig")
            midten2 = True
            gultemp = 0
            oransjtemp = 0
            blåtemp = 0
            lyseblåtemp = 0
    else:
        if gul == 1:
            print("det er gul")
            if oransjtemp == 1 and blåtemp == 1:
                print("det finnes oransj og blå, gul rett ned")
            if oransjtemp == 1 and blåtemp == 0:
                print("det finnes oransj, gul holdes")
                gultemp -= 1
            if blåtemp == 1 and oransjtemp == 0:
                print("det finnes blå, gul holdes")
                gultemp -= 1
            if gultemp == 1:
                print("gul først, rett ned")
            if gultemp == 2:
                print("det er gul allerede, gul holdes")
                gultemp -= 1

        if oransj == 1:
            print("det er oransj")
            if gultemp == 1:
                print("det finnes gul, oransj snur 2 ganger, ned til høyre")
            if oransjtemp == 2:
                print("det er oransj allerede, oransj holdes")
                oransjtemp -= 1
            if gultemp == 0:
                print("oransj før gul, ned til venstre")

        if blå == 1:
            print("det er blå")
            if gultemp == 1:
                print("det finnes gul, blå snur 2 ganer, ned til venstre")
            if blåtemp == 2:
                print("det er blå allerede, blå holdes")
                blåtemp -= 1
            if gultemp == 0:
                print("blå før gul, ned til høyre")

        if gultemp == 1 and oransjtemp == 1 and blåtemp == 1:
            print("høyre mønster fullført")
            gultemp = 0
            oransjtemp = 0
            blåtemp = 0
            høyremønster += 1

    gul = 0
    oransj = 0
    blå = 0
    lilla = 0
    rød = 0
    grønn = 0
    lyseblå = 0


rød += 1
main()
lilla += 1
main()
rød += 1
main()
grønn += 1
main()
grønn += 1
main()
lilla += 1
main()
lilla += 1
main()
rød += 1
main()
rød += 1
main()
lilla += 1
main()
lilla += 1
main()
rød += 1
main()
grønn += 1
main()
rød += 1
main()
lilla += 1
main()
grønn += 1
main()
lilla += 1
main()
print(lillatemp, rødtemp, grønntemp)
oransj += 1
main()
gul += 1
main()
blå += 1
main()
gul += 1
main()
print(lillatemp, rødtemp, grønntemp)
høyremønster = 8
print(venstremønster, høyremønster)
gul += 1
main()
lyseblå += 1
main()
oransj += 1
main()
blå += 1
main()
lyseblå += 1
main()
print(gultemp, oransjtemp, blåtemp, lyseblåtemp)










"""
list = []

nummer = 0

print(len(list))

def add_gul():
    global nummer
    list.append("gul")
    nummer += 1

def add_oransj():
    global nummer
    list.append("oransj")
    nummer += 1

def add_blå():
    global nummer
    list.append("blå")
    nummer += 1

def main():
    if list[nummer-1] == "gul":
        print("gul")
    if list[nummer-1] == "oransj":
        print("oransj")
    if list[nummer-1] == "blå":
        print("blå")
    print(nummer)
    print(list)

    if list.index("gul") < list.index("oransj") and list.index("gul") < list.index("blå"):
        print("gul først")

add_gul()
main()"""