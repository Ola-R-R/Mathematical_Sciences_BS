#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="#">Intro til løkker</a></li>
#     <li class="active"><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Mer om løkker - oppsamlingsløkker
# 
# **Læringsmål:**
# 
# * Løkker
# 
# **Starting Out with Python:**
# 
# * Kap. 4.2-4.3
# 
# I denne oppgaven ser vi spesielt på løkker som samler opp et resultat underveis. Hvis du har programmert noe før, vil dette være enkle oppgaver, men for deg som er helt uerfaren, se gjerne på følgende tutorial om oppsamlingsløkker før du setter i gang:

# ### Tutorial om oppsamlingsløkker

# Ofte brukes løkker til å samle opp et resultat (f.eks. en tallverdi) som vi er interessert i å finne. Et enkelt eksempel på en oppsamlingsløkke, er følgende som summerer alle tallene fra og med 1 til og med 100 (som egentlig er en unødvendig løkke å kjøre siden resultatet er kjent på forhånd, men greit å bruke som illustrasjon):

# In[ ]:


summen = 0
for i in range(1, 101):
    summen += i          # summen = summen + i
print("Summen av tallene 1-100:", summen)


# range() må ha 101 som sluttverdi fordi den er til men ikke med, dvs. hvis tallet 100 skal være med i summen. Variabelen **summen** er den som brukes til å samle opp resultatet underveis. Det kunne ha vært fristende å kalle variabelen bare sum, men dette er navnet på en standardfunksjon i Python og dermed ikke lurt å bruke som variabelnavn. Merk deg at summen må defineres **før** løkka, og der gis verdien 0 (fordi vi ikke har summert inn noen av tallene ennå). Dette fordi vi inni løkka ønsker å utføre summen = summen + 1 (som kortere kan skrives summen += 1), og et slikt uttrykk hvor summen også fins på høyre side av = kan bare fungere hvis den allerede har fått en verdi. Måten dette programmet funker på, er altså at vi starter med å gi summen verdi 0. Så begynner løkka, med i = 1, og vi legger til i (dvs. 1) til summen som da blir 1. Så blir i 2, som legges til summen, som nå blir 3. Så i=3, summen = 6. Så i=4, summen = 10, osv. Siste gang løkka kjøres er i=100 og summen blir 5050, så avslutter løkka og vi printer resultatet på skjermen.
# 
# Tilsvarende hvis vi skulle gange sammen alle tallene 1-20:

# In[ ]:


produktet = 1
for i in range(1, 20):
    produktet *= i          # produktet = produktet * i
print("Produktet av tallene 1-20:", produktet)


# Strukturelt er dette temmelig likt - en viktig forskjell er at når vi skal gange, blir riktig startverdi 1 (som er det tallet som ikke påvirker et produkt) mens det var 0 for summering.
# 
# Til slutt et lite eksempel der det passer bedre med while enn med for, fordi vi ikke aner antall repetisjoner:

# In[1]:


print("Skriv inn ett og ett positivt heltall.")
print("For å avslutte, skriv et negativt tall (dette telles ikke med).")
tall = int(input("Tall: "))
storst = tall  # første tall er størst, inntil annet bevist
antall = 0
  
while tall >= 0:
    if tall > storst:
        storst = tall
    antall += 1
    tall = int(input("Tall: "))
  
print("Du skrev inn", antall, "tall.")
print("Det største var", storst)


# Her skriver brukeren inn en serie tall fra tastaturet - og gir et negativt tall for å avslutte - og programmets oppgave til slutt er å kunne fortelle hvor mange tall som ble skrevet inn (bortsett fra det negative), og hva som var det største av tallene. For å telle opp antallet, har vi variabelen antall som settes til 0 før løkka, og deretter økes med 1 for hver runde av løkka. For å finne det største tallet, antar vi før løkka at det første tallet også er det største. (Vi må uansett lese det første tallet før løkka, for at while-testen skal funke). Deretter tester vi for hver runde av løkka om det sist innleste tallet er større enn det som var størst hittil, i så fall gis variabelen storst verdien til dette nye tallet i stedet. Variabelen storst vil dermed til en hver tid inneholde den største verdien hittil.

# ### a)

# Lag et program som ved hjelp av en løkke ber brukeren om å taste inn 7 heltall, som vist i eksemplet på kjøring under. Til slutt skal programmet skrive ut hva summen av tallene ble.
# 
# Eksempel på kjøring:
# ```
# Skriv inn et heltall: 6
# Skriv inn et heltall: 4
# Skriv inn et heltall: 7
# Skriv inn et heltall: 3
# Skriv inn et heltall: 2
# Skriv inn et heltall: 456
# Skriv inn et heltall: 99
# Summen av tallene ble 577
# ```
# 
# ***Skriv koden din her:***

# In[ ]:


summen = 0

for i in range(7):
    heltall = int(input("Skriv inn et heltall: "))
    summen += heltall
print("Sum", summen)


# #### Hint

# Du vil trenge en variabel til å summere inn ett og ett nytt tall for hver runde av løkka. Husk at denne variabelen må være opprettet og gitt en passende startverdi før løkka, ellers vil du ikke klare å bruke den i løkka.

# ### b)

# Lag et program som multipliserer sammen alle tallene fra 1,2,3,... og avslutter når produktet er større enn 1000.
# 
# ***Skriv koden din her:***

# In[ ]:


produkt = 1
i = 1

while produkt < 1000:
    produkt *= i
    i += 1
print(produkt)


# #### Hint 2

# Du vet ikke på forhånd hvor lenge du kan multiplisere tallene før du får et produkt større enn 1000, så her kan det være lurt å bruke en while-løkke med produkt mindre enn 1000 som betingelse. Svaret skal bli 5040. Som for oppgave (a) vil du trenge en variabel til å gange inn ett og ett nytt tall for hver runde av løkka, og som må ha fått en passende startverdi før løkka. Merk at passende startverdi for en variabel som skal samle opp et produkt, vil være et annet tall enn det man bruker som startverdi for å samle opp en sum.

# ### c)

# Lag et program som stiller brukeren det samme spørsmålet, om og om igjen, helt til det korrekte svaret blir skrevet. Da skal programmet fortelle hvor mange forsøk som ble brukt. Eksempel på kjøring vist nedenfor, men du kan godt bytte ut med et spørsmål med annen tematikk, noe du selv er interessert i. Se ***hint 3*** dersom du står fast.
# 
# Eksempel på kjøring:
# 
# ```
# Hva heter hovedstaden til Niue? Niue City
# Det var feil, prøv igjen.
# Hva heter hovedstaden til Niue? Niuania
# Det var feil, prøv igjen.
# Hva heter hovedstaden til Niue? Apia
# Det var feil, prøv igjen.
# Hva heter hovedstaden til Niue? Alofi
# Korrekt!! Du brukte 4 forsøk.
# ```
# 
# ***Skriv koden din her:***

# In[4]:


sporsmål = "Hva er hovedstaden i Norge? "
svar = input(sporsmål)
korrektsvar = "Oslo"
i = 1

while svar.lower() != korrektsvar.lower():
    print("Det var feil, prøv igjen.")
    svar = input(sporsmål)
    i += 1
print("Korrekt!! Du brukte", i, "forsøk.")


# #### Hint 3

# Du vet ikke hvor mange ganger brukeren svarer feil så det kan være lurt med en while-løkke hvor betingelsen er at brukerens svar != riktig svar.
