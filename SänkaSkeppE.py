import random

# Variabel för vilken båt som ska väljas
båtlängd = 0

# Listor av listor (rutnät)
antalrader=10
antalkolumner=10

båtbräde = []   # Bräde med "facit" för båtplaceringarna
skjutbräde = [] # Bräde för sänkning av båtar

antal_träffar = 0   # Variabel för hur många giltliga gånger användaren har träffat en båt
antal_skott = 0     # Antalet giltliga skott som har avfyrats av användaren

rad = []    # En rad med vågor
rad0 = []   # Raden med kolumnerans namn

# Skriver ut ett visst bräde
# Paramtern "brädtyp" antar antingen båtbräde eller skjutbräde när funktionen körs
def rita_bräde(brädtyp):
    for bokstav in rad0:
        if bokstav == "A":      # Gör så att "bokstavsindexeringen" börjar först tre rutor in
            print(end="   ")
        print(bokstav, end=" ")
    print()
    for rindex in range(antalrader):
        print(rindex+1, end=" ")
        if rindex != 9:     # Gör så att rutorna avsedda att vara i samma kolumn inte förskjuts
            print(end=" ")
        for r in brädtyp[rindex]:
            print(r,end=" ") # ,end="" för att print ska fortsätta skriva i samma rad
        print() # För att skriva på nästa rad

# Val av ändar
def båt_ändar():
    sökning = True
    while sökning: # Genomsökande av giltliga ändar
        giltlig = True  # Antag att de kommande ändarna är giltliga
        print("\nEn båt med längden", båtlängd, "ska utplaceras") # Talar om båtlängden som den valda båten ska ha
        ändeI = input("Välj den ena änden: ")   # Tar emot den första änden som ändeI
        # Raden nedan gör ändeI till en lista med kolumnbokstaven som elemenet av index 0 och radindex, räknat 1-10,...
        # ...som element av index 1 (Hakparanteser fungerar på motsvarande sätt efter en string som efter en lista)
        ändeI = [ändeI[0],ändeI.replace(ändeI[0],"")]
        if not ändeI[0].upper() in rad0 or not ändeI[1].isdigit() or not int(ändeI[1]) in range(1,11):  #...
            print("Ogiltliga ändar")    # ...Om ändeI inte består av en kolumnbokstav och ett heltal 1-10 (i string-datatyp)...
            continue                    # ...(för att undvika en krasch)
        ändeI[0] = rad0.index(ändeI[0].upper()) # Eventuella gemener blir versaler och kolumn-bokstaven ersätts med sitt index
        ändeI[1] = int(ändeI[1])-1  # Gör om radindexeringen från 1-10 till 0-9
        
        if båtlängd != 1:    # Om båtlängden inte är 1 krävs det en andra ände
            ändeII = input("Välj den andra änden: ")    # Motsvarande för den andra änden
            ändeII = [ändeII[0],ändeII.replace(ändeII[0],"")]
            if not ändeII[0].upper() in rad0 or not ändeII[1].isdigit() or not int(ändeII[1]) in range(1,11):
                print("Ogiltliga ändar") 
                continue
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
                            if giltlig and båtbräde[radindex][kolumnindex] != "~": # Kollar om den aktuella positionen...
                                    print("Ogiltliga ändar")                            # ...inte är tom, och om detta gäller...
                                    giltlig = False                                     # ...är de valda ändarna ogiltliga och...
        else:   # Är båtlängden fel är ändarna ogiltliga och ska väljas om              # ...ska väljas om. "giltlig"...
            print("Ogiltliga ändar")                                                    # ...finns med som villkor för att... 
            giltlig = False                                                             # ..."Ogiltliga ändar" eventuellt inte... 
        if giltlig: # Om ändarna är giltliga ska genomsökandet avbrytas                 # ...ska skrivas ut flera gånger.
            sökning = False
    return([ändeI, ändeII]) # Returnernar änd-koordinaterna med kolumnen respektive raden angiven med index 0-9

# Placerar ut en båt med två angivna ändkoordinater (eller en ändkoordinat i fallet med en båt med lägden 1).
# Parametern "ändar" kommer att anta den returnerade listan [ändeI, ändeII] i båt_ändar-funktionen när funktionen körs.
def placera_båt(ändar):
    for radindex in range(min(ändar[0][1],ändar[1][1]), max(ändar[0][1],ändar[1][1])+1):    # Radindex med position att fylla i
        for kolumnindex in range(min(ändar[0][0],ändar[1][0]), max(ändar[0][0],ändar[1][0])+1): # Kolumnindex för aktuell...
            båtbräde[radindex][kolumnindex] = ":"                                               # ...rad

def avfyrning():
    sökning = True
    while sökning:      # Genomsökande av giltlig koordinat
        s_koordinat = input("\nVilket koordinat ska beskjutas? ")
        s_koordinat = [s_koordinat[0],s_koordinat.replace(s_koordinat[0],"")]   # Översätter koordinaten till en lista
        if not s_koordinat[0].upper() in rad0 or not s_koordinat[1].isdigit() or not int(s_koordinat[1]) in range(1,11): #...
            print("Ogiltliga ändar") # ...Om s_koordinat inte består av en kolumnbokstav och ett heltal 1-10 (i string-datatyp)...
            continue                 # ...(för att undvika en krasch)            
        s_koordinat[0] = rad0.index(s_koordinat[0].upper()) # Kolumnbokstaven ersätts med index 0-9
        s_koordinat[1] = int(s_koordinat[1])-1      # Indexering 1-10 blir 0-9

        giltlig = True                      # Antag att skottet är giltligt
        if skjutbräde[s_koordinat[1]][s_koordinat[0]] == "~":
            if båtbräde[s_koordinat[1]][s_koordinat[0]] == ":":
                träff = True                # Skottet är en träff
                skjutbräde[s_koordinat[1]][s_koordinat[0]] = "x"
                print("TRÄFF")
                rita_bräde(skjutbräde)
            else:
                träff = False               # Skottet är en miss
                skjutbräde[s_koordinat[1]][s_koordinat[0]] = "o"
                print("MISS")
                rita_bräde(skjutbräde)
        else:
            giltlig = False                 # Skottet är ogiltligt
            print("Ogiltlig koordinat")
        if giltlig:                 # Om skottet är giltligt behöver inget nytt tas emot
            sökning = False
        
    if träff:       # Returnerar om antalet_träffar ska uppdateras med 1 eller inget, dvs. 0
        return(1)
    else:
        return(0)

# Skapar en rad med vågor
for k in range(antalkolumner):
    rad.append("~")

# Skapar båtbrädet av vågorna
for r in range (antalrader):  # Sätter in raderna i brädena
    båtbräde.append(list(rad))  
    skjutbräde.append(list(rad))# list(rad) används för att skapa en ny lista som innehåller samma som rad
                                
# Skapar raden med kolumnernas namn
for unicode in range(ord('A'),ord('A')+antalkolumner):
    rad0.append(chr(unicode))

# Båtplacering
for båtlängd_att_utplacera in range(4,0,-1):    # Båtlängder som ska utplaceras 
    båtlängd = båtlängd_att_utplacera   # Sätter båtlängden som användaren ska välja en båt för till den aktuella längden
    for antal_lika_båtar in range(5-båtlängd_att_utplacera):    # Antal båtar av en viss längd som ska utplaceras
        rita_bräde(båtbräde)
        placera_båt(båt_ändar())    # Båtändar väljs och och båten med de valda ändarna placeras
rita_bräde(båtbräde)

for nyrad in range(100):     # Döljer facit så att användaren som ska sjuta inte samtidigt ser facit
    print()

# Båtsänkning
# Medan användarns träffar är mindre än antalet båtpostioner = 4*1+(3*2)+(2*3)+4 = 20 (medan användaren har skott kvar att skjuta)
while antal_träffar < 20:
    antal_träffar += avfyrning()
    antal_skott += 1

print("Du sänkte alla båtar med", antal_skott, "skott!")
