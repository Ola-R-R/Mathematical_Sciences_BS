#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li class="active"><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
#     <li><a href="Euklids%20algoritme.ipynb">Euklids algoritme</a></li>
#     <li><a href="Primtall.ipynb">Primtall</a></li>
#     <li><a href="Multiplikasjon.ipynb">Multiplikasjon</a></li>
#         <li><a href="Den%20store%20sporreundersokelsen.ipynb">Den store spørreundersøkelsen</a></li>
#     <li><a href="Arbeidsdager.ipynb">Arbeidsdager</a></li>
#     <li><a href="Sekantmetoden.ipynb">Sekantmetoden</a></li>
#     <li><a href="Not%20quite%20Blackjack.ipynb">Not quite Blackjack</a></li>
#         <li><a href="Funksjoner%20og%20Jupyter%20widgets.ipynb">Funksjoner og Jupyter widgets</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Grunnleggende om funksjoner
# 
# **Læringsmål:**
# - Funksjoner
# 
# **Starting Out with Python:**
# - Kap. 5.1-5.2
# - Kap. 5.4
# - Kap. 5.8

# ## Innføring – Del 1: Enkle funksjoner uten parametre og returverdi
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du går videre

# Programmet nedenfor tenkes å skulle skrive ut en masse data (hvorav bare fragmenter er vist her).
# 
# Mellom hver bolk av data vil vi ha et skille med blank linje, horisontal strek og en ny blank linje.
# 
# Dette gir identisk kode alle stedene markert med `##`, som er unødig tungvint.

# In[ ]:


# EKSEMPEL UTEN FUNKSJON
print("Eksempel der vi BURDE brukt en funksjon")
print()                                 ##
print("---------------------")          ##
print()                                 ##
print("Data fra måler 1:", 23.4, 21.2, 21.9)
print("Osv., ...")
print()                                 ##
print("---------------------")          ##
print()                                 ##
print("Data fra måler 2: ...")
print()                                 ##
print("---------------------")          ##
print()                                 ##
print("Data fra måler 3: ...")
print()                                 ##
print("---------------------")          ##
print()                                 ##


# Nedenfor er det løst bedre:
# 
# - Kodesnutten som trengs flere steder i programmet, defineres øverst som en funksjon, her med navnet `skille()`
# - Trenger da kun skrive `skille()` de stedene i koden hvor vi ønsker disse tre print-setningene utført.

# In[ ]:


# EKSEMPEL MED FUNKSJON
def skille():
    print()
    print("---------------------")
    print()


print("Samme eksempel MED funksjon")
skille()
print("Data fra måler 1:", 23.4, 21.2, 21.9)
print("Osv., ...")
skille()
print("Data fra måler 2:", 18.4, 19.1, 18.7)
skille()
print("Data fra måler 3:", 19.9, 19.1, 18.2)
skille()


# Utførelsen av denne koden starter på toppen av **skriptet**, dvs. koden som som er ute på vanlig marg.
# 
# Det første som printes er derfor "Samme eksempel MED funksjon".
# 
# Deretter de tre printene i skille-funksjonen.
# 
# Deretter "Data fra måling 1: ..." Osv. Alt i alt blir resultatet dermed identisk med koden der vi ikke hadde funksjon, men koden med funksjon er kortere og ryddigere fordi vi unngår å gjenta identiske kodelinjer flere ganger.

# ## a)

# Koden under har 4 identiske fragmenter merket med ##.
# 
# ***Endre koden på følgende måte:***
# 
# - definer en funksjon `siksak()` som utfører de 4 linjene som er merket med `##`
# - i skriptet kan du da erstatte disse 4 kodelinjene med kall til `siksak()`
# 
# Utskriften etter endringen din skal være eksakt den samme som før programmet ble endret. Hvis du er i tvil om hva du skal gjøre her, les tutorial ovenfor som viser et lignende eksempel.

# In[ ]:


def siksak():
    print()
    print("**  **  **  **  **  **  **  **  **")
    print("  **  **  **  **  **  **  **  **")
    print()
    

print("Data fra spørreundersøkelse")
siksak()
print("Del 1: ... div. data her, ikke vist")
siksak()
print("Del 2: ... mer data ...")
siksak()
print("Del 3: ... enda mer data ...")
siksak()
print("Del 4: ... ytterligere data ...")


# ## Innføring – Del 2: Funksjoner med parametre, men fortsatt uten returverdi
# 
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du går videre

# Innføring – del 1 og oppgave (a) illustrerte hovedpoenget med funksjoner: At vi har lik kode flere sted i et program, denne kan da defineres en gang for alle og deretter kalles ved navn, så slipper vi å gjenta kodelinjer, og programmet blir ryddigere.
# 
# Uten parametre har funksjoner likevel begrenset slagkraft. En funksjon uten parametre gjør eksakt det samme hver gang vi kaller den. Men ofte er behovet å gjøre nesten det samme, men ikke helt. En kvadratrotfunksjon trenger f.eks. å kunne regne ut roten av ulike tall - en funksjon som bare kan regne roten av 2, er ikke særlig nyttig. Nedenfor vises et eksempel som ligner på eksemplet fra oppgave (a). Vi har en utskrift hvor det inngår overskrifter i hashtag-bokser. Men koden er bare nesten lik, siden overskriftens tekst endrer seg fra gang til gang. Hvis vi lager en funksjon som alltid skriver INTRODUKSJON, kan denne ikke brukes for de neste overskriftene.

# In[ ]:


# EKSEMPEL UTEN FUNKSJON
print()
print("################")
print("# INTRODUKSJON #")
print("################")
print()
print("her kommer noen innledende forklaringer...")
print()
print("##########################")
print("# DATA FRA EKSPERIMENT 1 #")
print("##########################")
print()
print("Div. data:", 123, 345, 432, 356)
print()
print("##########################")
print("# DATA FRA EKSPERIMENT 2 #")
print("##########################")
print()
print("Osv...") 


# Løsningen blir å utstyre funksjonen med en **parameter**, som gir funksjonen fleksibilitet til å endre litt oppførsel fra gang til gang:

# In[ ]:


# SAMME EKSEMPEL MED FUNKSJON
def box_heading(tekst):
    bredde = len(tekst) + 4
    print()
    print("#" * bredde )
    print("# " + tekst + " #")
    print("#" * bredde )
    print()
     
box_heading("INTRODUKSJON")
print("her kommer noen innledende forklaringer...")
box_heading("DATA FRA EKSPERIMENT 1")
print("Div. data:", 123, 345, 432, 356)
box_heading("DATA FRA EKSPERIMENT 2")
print("Osv...")


# Programmet starter med å utføre `box_heading("INTRODUKSJON")`. Dette gjør at vi kjører funksjonen `box_heading`, med argumentet `"INTRODUKSJON"` byttet inn for parameteren `tekst`.
# 
# Setningen `print("# " + tekst + " #")` gjør da at denne strengen skrives midt i boksen.
# 
# Funksjonen `len(tekst)` gir oss lengden på strengen, dette gjør det mulig for oss å tilpasse bredden på boksen til hva som gis inn for parameteren.
# 
# I neste kall av `box_heading` er det derimot argumentet `"DATA FRA EKSPERIMENT 1"` som byttes inn for parameteren `tekst`. Osv. Bruk av parameter gjør det dermed mulig for funksjonen `box_heading` å skrive ulik tekst i boksen fra gang til gang.

# ## Innføring - Del 3: Funksjoner med parametre *og* returverdi:
# 
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du går videre

# I (a) og (b) har vi sett på funksjoner uten returverdi. Dette kan være greit for funksjoner som spesifikt skal skrive eller tegne på skjermen.
# 
# Men for funksjoner som skal beregne en verdi (og svært mange funksjoner skal nettopp det), trenger vi å få ut et resultat av beregningen. Til dette brukes **returverdi**.
# 
# Det trenger ikke å være en matematisk beregning. For å vise noe annet, gis under et eksempel relatert til språk, nemlig en funksjon for å gradbøye adjektiv.
# 
# Ideen med funksjonen **komparativ()** er at den får inn et adjektiv i vanlig positiv form, og da kan bøye til komparativ, f.eks. snill -> snillere, interessant -> mer interessant.
# 
# For at ikke koden skal bli for lang, er eksemplet grovt forenklet - mange adjektiver vil bli bøyd feil.
# 
# Å gi returverdi fra en funksjon, oppnås med ordet **return** (linje 7). Verdien av det som står etter return (her: variabelen svar, som vil være en streng, f.eks. "snillere") vil bli returnert fra funksjonen.
# 
# Med "snillere" som returverdi vil da komparativ(adj) i linje 11 printe "Hah! Jeg er mye snillere !"
# 
# Lenger nede i programmet, linje 16, vil bøyningen  (f.eks. "snillere") bli satt inn i variabelen fasit, som deretter brukes i en if-test.

# In[ ]:


def komparativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
 
### TILLEGG 1, ny funksjon, kommer her:
 
#DEL AV KODEN HVOR SYSTEMET DISSER BRUKEREN
adj = input("Beskriv deg selv med et adjektiv: ")
print("Hah! Jeg er mye", komparativ(adj) + "!")
 
### TILLEGG 2 kommer her ...
 
# DEL AV KODEN HVOR BRUKEREN TRENER PÅ Å GRADBØYE
adj = input("Skriv inn et adjektiv: ")
svar = input("Hva er komparativ for " + adj + "? ")
fasit = komparativ(adj)
if svar == fasit:
    print("Korrekt!")
else:
    print("Feil, det var", fasit)
 
### TILLEGG 3 kommer her...


# Men hva oppnår vi med returverdi her? Hvorfor ikke like godt bruke print() i slutten av funksjonen, heller enn å returnere en verdi som printes senere??
# 
# **Med returverdi oppnår vi at funksjonen blir mer generelt anvendelig.** Funksjonen lar seg bruke for to ulike behov i dette lille programmet:
# 
# - BRUK 1, linje 11, her er det programmet som autogenererer komparativ form og printer ut på skjermen
# - BRUK 2, linje 16, her er det brukeren som prøver å svare hva komparativ er, programmet tester med en if-setning om det var korrekt
# 
# **Hadde vi derimot printet i slutten av funksjonen, ville anvendeligheten har vært mindre.**
# 
# - Printe "Hah! Jeg er ..." i slutten av funksjonen? Da passer den bare for BRUK 1
# - Gjøre en if-test i  slutten av funksjonen og printe Korrekt / Feil? Da passer den bare for BRUK 2
# - Gjøre bare print(svar) i slutten av funksjonen i stedet for return svar? Da passer den verken for BRUK 1 eller BRUK 2
# 
# På samme måte ville input i starten av funksjonen (i stedet for parameteren adj) ødelegge den generelle anvendeligheten.
# 
# - input("Beskriv deg selv...") i funksjonen - og den passer kun for BRUK 1
# - input("Skriv inn...") osv. i funksjonen - og den passer kun for BRUK 2
# 
# For å lage generelt anvendelige funksjoner er det vanligvis lurt å unngå input og print i funksjonen - annet enn for funksjoner som spesifikt har som mål akkurat å kommunisere med brukeren.

# # b)

# Ta utgangspunkt i koden nedenfor, som også er forklart i Tutorial like over. Kjør koden og sjekk at den virker. Ikke la deg bekymre deg om at en del adjektiver bøyes feilaktig.

# In[ ]:


def komparativ(adj):
    # GROVT FORENKLET FOR Å KUNNE FOKUSERE PÅ HOVEDPOENGET
    if len(adj) >= 8: # unøyaktig
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar
  
### TILLEGG 1, ny funksjon, kommer her:
def superlativ(adj):
    if len(adj) >= 8: # unøyaktig
        svar = "mest " + adj
    else:
        svar = adj + "est"
    return svar
 
#DEL AV KODEN HVOR SYSTEMET DISSER BRUKEREN
adj = input("Beskriv deg selv med et adjektiv: ")
print("Hah! Jeg er mye", komparativ(adj), "!")
  
### TILLEGG 2 kommer her ...
adj = input("Beskriv deg selv med et adjektiv: ")
print("Jeg er faktisk", superlativ(adj), "i hele verden.")
 
# DEL AV KODEN HVOR BRUKEREN TRENER PÅ Å GRADBØYE
adj = input("Skriv inn et adjektiv: ")
svar = input("Hva er komparativ for" + adj + "? ")
fasit = komparativ(adj)
if svar == fasit:
    print("Korrekt!")
else:
    print("Feil, det var", fasit)
  
### TILLEGG 3 kommer her...

adj = input("Skriv inn et adjektiv: ")
svar = input("Hva er superlativ for" + adj + "? ")
fasit = superlativ(adj)
if svar == fasit:
    print("Korrekt!")
else:
    print("Feil, det var", fasit)


# ***Din oppgave: Lag en tilsvarende funksjon superlativ(adj)*** som tar inn som parameter et adjektiv i vanlig positiv form, bøyer det til superlativ (f.eks. snill -> snillest, interessant -> mest interessant), og returnerer superlativformen.
# 
# Bortsett fra forskjellen i bøyning vil denne funksjonen være svært lik komparativ() som står der nå.
# 
# - Den nye funksjonen skal skrives der kommentaren ### TILLEGG 1 nå står i koden
# - Der det står ### TILLEGG 2, legg til en print-setning med et kall til superlativ(). Hvis brukeren skrev adjektivet "snill", skal utskriften bli "Jeg er faktisk snillest i hele verden."
# - Der det står ### TILLEGG 3, legg til en programdel som spør brukeren "Hva er superlativ for ..." (det adjektivet som ble skrevet inn...) og sjekker dette mot fasit på samme måte som koden nå gjør for komparativ.
# 
# Frivillig ekstraoppgave (ikke nødvendig for å få (c) godkjent, men anbefalt å prøve): Etter dette vil du kanskje se at de to kodefragmentene som sjekker svar mot fasit er ganske like. Klarer du å lage en funksjon for dette, og så kalle denne to ganger, i stedet for å gjenta ganske lik kode to ganger i programmet?

# ## Innføring - Del 4: Main-funksjonen
# 
# Dette er ikke en del av oppgaven, men kan være lurt å lese før du går videre

# Det er vanlig for et program å ha en main-funksjon som blir kalt når programmet starter. Det er denne funksjonen som kaller programmets andre funksjoner når de trengs.
# 
# Et eksempel på et program med en main-funksjon er vist under. Her er det oppdelt slik at funksjonen kvadrattall gjør en beregning, mens main() står for kommunikasjon med brukeren.
# 
# I større programmer kunne det også ha vært egne funksjoner for å kommunisere med brukeren, slik at main() bare hadde gjort den overordende styringen både av beregning og brukerkommunikasjon ved å kalle andre funksjoner.
# 
# Når kode som vi ellers ville hatt i skriptet puttes i en main()-funksjon, blir skriptet kun 1 linje som kaller main-funksjonen, som vist nederst her. Kjør koden selv og se om du skjønner hvordan den funker:

# In[ ]:


def kvadrattall(x):
    # INN: x, som er ment å være et heltall
    # PROSESS: sjekker om x er et kvadrattall
    #(dvs. om det fins et heltall y <= x slik at y * y == x)
    # UT: hvis ja, returneres y. Ellers returneres False
    for y in range(1, x + 1):
        if y * y == x:
            return y
    return False
    # vi kommer til siste return bare hvis vi ikke fant kvadrattall
    # siden vi ellers vil ha avsluttet funksjonen med return y
 
def main():
    tall = int(input("Gi et heltall >0, eller 0 for å slutte: "))
    while tall > 0:
        rot = kvadrattall(tall)
        if rot:
            print(tall, "=", rot, "*", rot, "; m.a.o. et kvadrattall")
        else:
            print(tall, "er ikke et kvadrattall.")
        tall = int(input("Gi et heltall >0, eller 0 for å slutte: "))
 
# SKRIPT 
main()


# Et annet poeng som denne koden illustrerer, er at **return** ikke er begrenset til å stå i siste setning i en funksjon.
# 
# Her har vi dessuten en return som står inni en if-setning. Grunnen er at hvis vi finner svaret, er det ikke vits å fortsette flere runder med løkka; return vil gjøre at vi avslutter funksjonen.

# ## c)

# ***Kopier koden du lagde for adjektiv i oppgave (b) inn under. Endre den ved å lage en main-funksjon for det som nå er skriptet, slik at skriptet bare blir et kall til main().***

# In[2]:


def komparativ(adj):
    if len(adj) >= 8:
        svar = "mer " + adj
    else:
        svar = adj + "ere"
    return svar

def superlativ(adj):
    if len(adj) >= 8:
        svar = "mest " + adj
    else:
        svar = adj + "est"
    return svar

def main():
    adj = input("Beskriv deg selv med et adjektiv: ")
    print("Hah! Jeg er mye", komparativ(adj), "!")
    print("Jeg er faktisk", superlativ(adj), "i hele verden.")
    svar1 = input("Hva er komparativ for" + adj + "? ")
    fasit1 = komparativ(adj)
    if svar1 == fasit1:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit1)
    svar2 = input("Hva er superlativ for" + adj + "? ")
    fasit2 = superlativ(adj)
    if svar2 == fasit2:
        print("Korrekt!")
    else:
        print("Feil, det var", fasit2)

main()


# Kjøring av koden skal gi samme resultat som tidligere.

# #### Framgangsmåte

# 1. Definer funksjonen og kall den main. Funksjonen skal IKKE ta inn noen argumenter.
# 2. Flytt kodelinjene som nå står i skriptet (dvs., som foreløpig ikke er del av noen funksjon) inn i main-funksjonen. Pass på riktig innrykk!
# 3. Legg til helt nederst i koden, ute på ytterste marg, et kall til main().
