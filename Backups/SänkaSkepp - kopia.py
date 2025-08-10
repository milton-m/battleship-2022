import random

# Variabel för vilken båt som ska väljas
båtlängd = 0

# Listor av listor (rutnät)
antalrader=10
antalkolumner=10

bräde = []

# Skapar en rad med vågor
rad=[]
for r in range(antalkolumner):
    rad.append("~")

# Skapar ett bräde av vågorna
for k in range (0,antalrader):  # Sätter in raderna brädet 
    bräde.append(list(rad))     # board.append(rad)
                                # list(rad) används för att skapa en...
                                # ...ny lista som innehåller samma som rad

#print(bräde)

rad0=[]     # Skapar raden med kolumnernas namn
for k in range(ord('A'),ord('A')+antalkolumner):
    rad0.append(chr(k))

def rita_bräde(): # skriver ut hela brädet
    for b in rad0:
        if b == "A":      # Gör så att "bokstavsindexeringen" börjar först tre rutor in
            print(end="   ")
        print(b, end=" ")
    print()
    for r in range(antalrader):
        print(r+1, end=" ")
        if r != 9:     # Gör så att de rutorna avsedda att vara i samma kolumn inte förskjuts
            print(end=" ")
        for k in bräde[r]:
            print(k,end=" ") # ,end="" för att print ska fortsätta skriva i samma rad
        print()# För att skriva på nästa rad

# Val av ändar
def båt_ändar():
    while True: # Genomsökande av giltliga ändar
        giltlig = True  # Antag att de kommande ändarna är giltliga
        print("En båt med längden", båtlängd, "ska utplaceras") # Talar om båtlängden som den valda båten ska ha
        ändeI = input("Välj den ena änden: ")   # Tar emot den första änden som ändeI
        # Raden nedan gör ändeI till en lista med kolumnbokstaven som elemenet av index 0 och radindex, räknat 1-10,...
        # ... som element av index 1 (Hakparanteser fungerar på motsvarande sätt efter en string som efter en lista)
        ändeI = [ändeI[0],ändeI.replace(ändeI[0],"")] 
        ändeI[0] = rad0.index(ändeI[0].upper()) # Eventuella gemener blir versaler och kolumn-bokstaven ersätts med sitt index
        ändeI[1] = int(ändeI[1])-1  # Gör om radindexeringen från 1-10 till 0-9
        if båtlängd != 1:    # Om båtlängden inte är 1 krävs det en andra ände
            ändeII = input("Välj den andra änden: ")    # Motsvarande för den andra änden
            ändeII = [ändeII[0],ändeII.replace(ändeII[0],"")]
            ändeII[0] = rad0.index(ändeII[0].upper())
            ändeII[1] = int(ändeII[1])-1
        else:                # Om båtlängden är 1 ska den "andra" änden vara samma ände som den "första"
            ändeII = ändeI
            
        vertikal_längd = max(ändeI[1],ändeII[1]) - min(ändeI[1],ändeII[1]) + 1 # Båtlängden vertikalt
        horisontal_längd = max(ändeI[0],ändeII[0]) - min(ändeI[0],ändeII[0]) + 1 # Båtlängden horisontellt
        # Följande rads if-villkor undersöker om båtlängden är korrekt
        if vertikal_längd == båtlängd and horisontal_längd == 1 or horisontal_längd == båtlängd and vertikal_längd == 1:
            for radindex in range(min(ändeI[1],ändeII[1])-1,max(ändeI[1],ändeII[1])+2): # Radindex som eventuellt ska undersökas
                if 0 <= radindex <= 9:  # Kollar enbart de radindex som faktiskt finns (då en båt kan ligga intill en kant)
                    for kolumnindex in range(min(ändeI[0],ändeII[0])-1,max(ändeI[0],ändeII[0])+2): # Kolumnindex -||-
                        if 0 <= kolumnindex <= 9: # Kollar enbart de kolumnindex som faktiskt finns (-||-)
                            if giltlig == True and bräde[radindex][kolumnindex] != "~": # Kollar om den aktuella positionen...
                                    print("Ogiltliga ändar")                            # ...inte är tom, och om detta gäller...
                                    giltlig = False                                     # ...är de valda ändarna ogiltliga och...
        else:   # Är båtlängden fel är ändarna ogiltliga och ska väljas om              # ...ska väljas om. "giltlig == True"...
            print("Ogiltliga ändar")                                                    # ...finns med som villkor för att... 
            giltlig = False                                                             # ..."Ogiltliga ändar" eventuellt inte ... 
        if giltlig == True: # Om ändarna är giltliga ska genomsökandet avbrytas         # ... ska skrivas ut flera gånger.
            break
    return([ändeI, ändeII]) # Returnernar änd-koordinaterna med raden respektive kolumnen angiven med index 0-9

# Placerar ut en båt med två angivna ändkoordinater (eller en ändkoordinat i fallet med en båt med lägden 1).
# Parametern "ändar" kommer att anta den returnerade listan [ändeI, ändeII] i båt_ändar-funktionen när funktionen körs.
def placera_båt(ändar):
    for radindex in range(min(ändar[0][1],ändar[1][1]), max(ändar[0][1],ändar[1][1])+1):    # Radindex med position att fylla i
        for kolumnindex in range(min(ändar[0][0],ändar[1][0]), max(ändar[0][0],ändar[1][0])+1): # Kolumnindex för aktuell...
            bräde[radindex][kolumnindex] = ":"                                                  # ...position
            
# Båtplacering
for båtlängd_att_utplacera in range(4,0,-1):    # Båtlängder som ska utplaceras
    båtlängd = båtlängd_att_utplacera   # Sätter båtlängden som användaren ska välja en båt för till den aktuella längden
    for antal_lika_båtar in range(5-båtlängd_att_utplacera):    # Antal båtar av en viss längd som ska utplaceras
        rita_bräde()
        placera_båt(båt_ändar())    # Båtändar väljs och och båten med de valda ändarna placeras
rita_bräde()


"""
X
# 1. r in range(antalrader) gör att r tar alla
#    värden från noll till antalrader-1
#    Använd print(r, end="  ") för att skriva radnummer
#    före varje rad i den delen av programmet.
X

X
# 2. skriv ut en rad före brädan (board) med en
#    bokstav för varje kolumn från bokstaven 'A'.
#    Du ska förstå hur ord() och chr() fungerar nedan
X

X
#  När du är klar ska programmet skriva ut
'''
	A B C D E F G H I J 
1	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
2	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
3	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
4	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
5	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
6	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
7	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
8	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
9	~ ~ ~ ~ ~ ~ ~ ~ ~ ~ 
10	~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''
X

T
# 3.  Du kan modifiera platserna i din bräda genom
#     att komma år positionen, dvs vilken kolumn och vilken rad
#     använd  board[3][7]=':' och skriv ut brädan igen
#     Vilken position har ändrats?
T

#FRÅGA CALLE OM "FELAKTIGA KOORDINATER"!
X
# 4.  Nu ska du fylla brädan med båtar som i ett
#     sänka skepp-spel, dvs
#     1 st båt som upptar 4 platser : : : : 
#     2 st båtar som upptar 3 platser : : :  
#     3 st båtar som upptar 2 platser : :
#     4 st båtar som upptar 1 plats   : 
#     båtarna får inte vidröra varandra.
#     Skriv ut brädan igen.
X

# 5.  Nästa steg är att göra programmet interaktivt
#     så att någon annan kan skjuta dina båtar.
#     Programmet ska fråga rad och kolumn för
#     positionen där man vill skjuta.
#     Därefter ska det svara om det fanns en båtdel där
#     och i så fall byta båtdelen mot X.

# 6.  Som ett första steg kan du ha en variabel
#     som räknar antal träff.
#     När antalet träff blir =4*1+(3*2)+(2*3)+4 så har man vunnit
#     Du kan även visa hur många skott man
#     använt för att sänka alla skepp.


# 7.  Du kan underlätta för användaren genom att visa
#     en bräda med alla skott hittills och vilka som träffat båt.
#     OBS, du ska inte visa var båtarna är!


# 8.  Sista delen är att göra programmet helt automatiskt, dvs
#     programmet ska även placera båtarna slumpvis i brädan,
#     utan att de överlappar eller vidrör varandra!
"""
