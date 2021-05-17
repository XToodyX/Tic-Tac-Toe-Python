# LArray enthält alle möglichen Kombinationen für einen Sieg
LArray = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
spielfeld = [" "," "," "," "," "," "," "," "," "]

# Listet alle noch freien Felder auf
emptyfields = [1,2,3,4,5,6,7,8,9]

def spielzug(player, symbol):
    while True:
        try:
            Zugfeld = ""

            if player == 1:
                Zugfeld = input("SP1: Auf welches freie Feld möchtest du setzen?")
                target = int(Zugfeld) - 1
            elif player == 2:
                Zugfeld = input("SP2: Auf welches freie Feld möchtest du setzen?")
                target = int(Zugfeld) - 1

            if spielfeld[target] == " " and spielfeld[target] != "O" and spielfeld[target] != "X":
                spielfeld[target] = symbol
                emptyfields.remove(int(Zugfeld))
                break

            elif spielfeld[target] == "O" or spielfeld[target] == "X":
                print(f"Bitte gebe eine Feldnummer ein, die noch nicht belegt ist {emptyfields}")
                continue
        except Exception:
            print(f"Bitte gebe eine gültige Feldnummer ein {emptyfields}")

def Spielfeldprint():
    print(spielfeld[0] + "|" +spielfeld[1] + "|" +spielfeld[2])
    print("-" + " " + "-" + " " + "-")
    print(spielfeld[3] + "|" + spielfeld[4] + "|" + spielfeld[5])
    print("-" + " " + "-" + " " + "-")
    print(spielfeld[6] + "|" + spielfeld[7] + "|" + spielfeld[8])

def checkUnentschieden():
    # Wahrheitswert von leerzeichen bestimmt
    # ob noch freie Felder sind
    leerzeichen = False

    # Überprüft ob es noch freie Felder gibt. Nein --> Unentschieden
    if " " in spielfeld:
        leerzeichen = True
    if leerzeichen == False:
        print("Unentschieden")
        exit(0)

def checkifwin(player, symbol):
    for loesung in range(8):
        counter_o = 0
        counter_x = 0
        for zahlen in range(3):
            if spielfeld[LArray[loesung][zahlen]] == symbol and player == 1:
                counter_x = counter_x + 1
            elif spielfeld[LArray[loesung][zahlen]] == symbol and player == 2:
                counter_o = counter_o + 1

        if counter_x == 3:
            print("Spieler 1: Du hast gewonnen :-)")
            exit(0)
        elif counter_o == 3:
            print("Spieler 2: Du hast gewonnen :-)")
            exit(0)

for round in range(9):
    # Spielzug von Spieler 1
    spielzug(1, "X")
    checkifwin(1, "X")
    Spielfeldprint()
    checkUnentschieden()

    # Spielzug von Spieler 2
    spielzug(2, "O")
    checkifwin(2, "O")
    Spielfeldprint()
    checkUnentschieden()








