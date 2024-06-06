#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li class="active"><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Intro til løkker
# 
# **Læringsmål:**
# 
# * Løkker
# * Velge egnet løkkekonstruksjon (for eller while) etter behov
# 
# **Starting Out with Python:**
# 
# * Kap. 4.1-4.3
# 
# I denne oppgaven skal du lære å skrive kode hvor handlinger repeteres ved hjelp av løkker.

# ### Intro om løkker

# Noe av det datamaskiner er best på, er gjentatte handlinger i høyt tempo. Dette er også et vanlig behov.
# * Et firma skal utbetale lønn til alle sine ansatte hver måned.
# * Et digitalt eksamenssystem skal vise spørsmål til, og motta svar fra, alle studenter som tar eksamen. 
# * Et system som styrer industrielt produksjonsutstyr skal motta informasjon fra en rekke sensorer hvert eneste sekund, om trykk, temperatur, osv., og gjøre handlinger basert på verdiene.
# * Utstyr på et sykehus skal overvåke pasienters hjerterytme osv. sekund for sekund, og kunne slå alarm hvis noe er unormalt.
# * Utstyr for opptak av musikk skal kunne sample lyden tusenvis eller millionvis av ganger per sekund.
# * Et program for å vise video på en mobilskjerm må likeledes kunne oppdatere fargen i hver piksel på skjermen mange ganger i sekundet.
# 
# Du har kanskje erfaring med bruk av regneark? Der er det vanlig hvis man skal bruke samme formel på alle radene i en tabell at man **kopierer** formelen nedover.  
# Å kopiere samme kodesetning flere ganger er mulig i Python også, men bare praktisk hvis antall repetisjoner er lavt og kjent på forhånd.
# Eksemplet nedenfor viser et slikt tilfelle, hvor en kodelinje er gjentatt 3 ganger.

# In[ ]:


print("Hipp")
print("Hipp")
print("Hipp")
print("Hurra!")


# Samme utskrift kan oppnås med løkke:

# In[ ]:


for i in range(3):
    print("Hipp!")
print("Hurra!")


# **for &lt;variabel&gt; in range(3)**: gjør at påfølgende kodesetning(er) med innrykk blir repetert 3 ganger.
# 
# print("Hurra!") som ikke har innrykk, er ikke del av løkka, og vil derfor bare bli utført en gang, etter at løkka er ferdig.
# 
# Det fins to typer løkker i Python, **for**-løkke som vist over, og **while**-løkke. Vi kunne ha klart oss med bare while-løkke, eksemplet ville da ha blitt:

# In[ ]:


i = 0
while i < 3:
    print("Hipp")
    i = i + 1  # eller: i += 1
print("Hurra!")


# while er noe mer tungvint her, vi må eksplisitt øke i med 1 for hver runde, som er implisitt i for-løkka. 
# 
# while-løkka vil fortsette så lenge betingelsen (her: i < 3) er sann, den vil derfor kjøre når i er 0, 1, 2, men deretter stoppe når i blir 3. Som i for-løkka gjør dette at Hipp skrives 3 ganger.
# 
# I andre situasjoner er while-løkke derimot bedre enn  for-løkke. Generelt gjelder følgende:
# 
# * **for-løkke** egner seg når vi har et **kjent antall repetisjoner**. Eksempel fra den virkelige verden: hver måned skal et firma utbetale lønn til alle sine ansatte. Firmaet og dets datasystem vet (forhåpentligvis) hvor mange ansatte det har, dermed har løkka "for alle ansatte, beregn og utbetal lønn" et kjent antall repetisjoner når lønningsdagen kommer.
# * **while-løkke** er derimot nødvendig hvis **maks antall repetisjoner er uvisst** når løkka starter og vi først finner ut underveis når løkka skal avsluttes. F.eks.
#  * brukeren bestemmer underveis, f.eks. "Try again" / "Quit" - vi aner ikke hvor mange ganger brukeren vil forsøke. Eller et program for lydopptak: løkka som sampler lyden, starter når brukeren klikker på "Record" og skal fortsette til brukeren trykker "Stop" - og vi aner ikke hvor mange sekunder eller minutter det vil ta.
#  * numerisk løsning av matematiske likninger, hvor stoppkriteriet er at vi skal ha nådd en viss presisjon. Hvis vi ikke aner på forhånd hvor mange iterasjoner som trengs for å nå denne presisjonen, vil while-løkke være best.
#  * produksjonsutstyr i en fabrikk skal kjøre som normalt med mindre sensordata indikerer en krisesituasjon, og da gå over til en alternativ nødprosedyre. Vi aner ikke om det går tusen sekunder, eller millioner av sekunder... kanskje inntreffer krisesituasjonen slett ikke. Dermed vil antall repetisjoner av løkka for normal oppførsel være ukjent når den starter, som tilsier while-løkke.
# 
# Under er forskjellen vist ved to ytterligere varianter av Hurra-programmet vårt. Kopier gjerne denne koden inn i editoren din og  kjør  den  for å se hvordan den virker.

# In[ ]:


# hvis brukeren skal bestemme antall på forhånd:
antall = int(input("Hvor mange Hipp?" ))
for i in range(antall):
    print("Hipp")
print("Hurra!")
 
# hvis brukeren skal bestemme seg for å slutte underveis:
print("Slå Enter direkte etter Hipp for å legge til flere Hipp,")
print("eller mellomrom så Enter for å avslutte: ")
while input("Hipp") == "":
    pass
print("Hurra!")


# Linje 1-5 viser en variant med **for**-løkke. Siden brukeren gir inn på forhånd antall Hipp som ønskes, er **antall repetisjoner kjent**, og **for-løkke enklest.**
# 
# Linje 7-12 viser derimot en variant hvor brukeren bestemmer underveis i løkka om vi skal fortsette eller avslutte, da er det best med **while** siden **antall repetisjoner er ukjent.**
# 
#  * brukeren velger å fortsette ved å trykke Enter direkte etter Hipp; dette vil gi en helt tom streng "" som resultat, slik at betingelsen i while vil  være sann. Så lenge den er sann, fortsetter løkka med å gjøre ny input() som gjør at ledeteksten "Hipp" kommer på skjermen på ny.
#  
#  * brukeren velger å avslutte ved å skrive inn et blankt tegn og deretter slå Enter. Dette vil gi strengen " " som er forskjellig fra "", da blir betingelsen usann, og løkka avsluttes, og programmet går videre med å skrive "Hurra".
# 
# I while-løkka er den eneste handlingen vi ønsker å utføre, den input() og sammenligning som står i betingelsen. Da trenger vi egentlig ingen innmat. Man er imidlertid nødt til å ha minst en setning inni ei løkke.
# Derfor **pass**, som er et beskyttet ord i Python for å gjøre ingenting. De fleste løkker vil ha mer kompliserte gjøremål og derfor også trenge en eller flere setninger inni som gjør noe.

# ## a)

# Koden under viser en for-løkke som repeterer 3 ganger. For hver runde blir brukeren bedt om å beskrive seg selv med et adjektiv, hvorpå maskinen disser brukeren ved å si at den er snillere, smartere etc.
# 
# (Trikset her er bare å legge til "ere" bak adjektivet, så det vil ikke bli grammatisk korrekt for adjektiv som bøyes annerledes.)
# 
# ***Kjør koden for å se hvordan den virker. Endre så koden slik at programmet først spør brukeren hvor mange repetisjoner som ønskes, og deretter utfører programmet med ønsket antall repetisjoner av løkka.***
# 
# Eksempel på kjøring:
# 
# ```python  
# Hvor mange adjektiv vil du gi? 2
# Beskriv deg selv med et adjektiv? snill
# Hah, du snill!? Jeg er mye snillere!
# Beskriv deg selv med et adjektiv? ond
# Hah, du ond!? Jeg er mye ondere!
# Takk for nå!
# ```

# In[ ]:


#endre koden under
antall = int(input("Hvor mange repetisjoner vil du ha? "))
for i in range(antall):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")


# #### Hint

# I stedet for tallet 3 i koden, må det stå en variabel for antall repetisjoner, og denne må i forkant leses inn fra bruker med input() og konverteres til et heltall.

# ## b)

# Koden under viser en while-løkke som utfører samme type brukerdialog som i (a), med 3 repetisjoner. Kjør den for å se hvordan det virker. **Endre nå programmet så løkka ikke kjører akkurat 3 ganger, men så mange ganger brukeren vil**, hvor brukeren kan bestemme dette underveis ved å gi et tomt svar (dvs. bare slå Enter) for å slutte. Da vil input()-setningen resultere i en tom streng, "".
# 
# Eksempel på kjøring:
# 
# ```python
# Slå Enter uten å skrive noe når du vil avslutte.
# Beskriv deg selv med et adjektiv? snill
# Hah, du snill!? Jeg er mye snillere!
# Beskriv deg selv med et adjektiv? smart
# Hah, du smart!? Jeg er mye smartere!
# Beskriv deg selv med et adjektiv? flittig
# Hah, du flittig!? Jeg er mye flittigere!
# Beskriv deg selv med et adjektiv?
# Takk for nå!
# ```
# 
# Fjerde gang spørsmålet om adjektiv ble stilt, slo brukeren her bare Enter uten å skrive inn noen tegn, da avsluttet løkka og programmet gikk videre med å skrive "Takk for nå"

# In[4]:


# print("Slå Enter uten å skrive noe når du vil avslutte.")
i = 42
while i >= 0:
    print("Du har", i, "bokstaver til disposisjon.")
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
    i = i - len(adj)
print("Takk for nå!")


# #### Hint

# I eksemplet måtte vi sette i = 0 før vi kan utføre testen i < 3, hvis ikke i hadde fått noen verdi, ville testen gi feilmelding. Likeledes, hvis du skal teste på at adj != "" må adj ha fått en verdi før denne testen skjer. Altså må du gjøre den første input til adj før while-løkka  starter.
# 
# Inni while-løkka vil det da også være fornuftig å bytte om  rekkefølgen på print-setningen og input-setningen, fordi du allerede har gjort en input før løkka som du kan basere den første "Hah..."-responsen på.

# ## c)

# Ta igjen utgangspunkt i while-løkka med 3 repetisjoner som vist før oppgave (b). Vi ønsker nå å endre programmet på følgende måte:
# 
# Brukeren starter med 42 bokstaver til disposisjon. For hver runde skal programmet trekke fra antall bokstaver i det adjektivet som ble brukt.
# 
# Løkka skal fortsette så lenge det fortsatt er bokstaver til disposisjon (dvs. dette tallet er større enn 0). 
# 
# **Eksempel på kjøring:**
# 
# ```python
# Du har 42 bokstaver til disposisjon.
# Beskriv deg selv med et adjektiv? snill
# Hah, du snill!? Jeg er mye snillere!
# Du har 37 bokstaver til disposisjon.
# Beskriv deg selv med et adjektiv? desperat
# Hah, du desperat!? Jeg er mye desperatere!
# Du har 29 bokstaver til disposisjon.
# Beskriv deg selv med et adjektiv? kjempetørst
# Hah, du kjempetørst!? Jeg er mye kjempetørstere!
# Du har 18 bokstaver til disposisjon.
# Beskriv deg selv med et adjektiv? megasupereffektiv
# Hah, du megasupereffektiv!? Jeg er mye megasupereffektivere!
# Du har 1 bokstaver til disposisjon.
# Beskriv deg selv med et adjektiv? o
# Hah, du o!? Jeg er mye oere!
# Takk for nå!
# >>>
# ```
# 
# I siste linje, hvor det bare er 1 bokstav til disposisjon, er brukeren lojal her og skrive bare en bokstav - men du behøver ikke lage programmet slik at det sikrer dette... det er ok om brukeren skriver et lenger ord den siste gangen, så lenge brukeren ikke får lov til å skrive nye ord når antall bokstaver til disposisjon er blitt <= 0.

# #### Hint

# I stedet for tellevariabelen i som starter på 0, og med betingelse < 3 i while-setninga, må du nå ha en variabel som starter på 42, og hvor lengden av hvert nye ord trekkes fra i løkka. Lengde kan finnes med funksjonen len(), dvs. len(adj) gir lengden til strengen adj. Testen i while-setninga må også tilpasses til det vi nå er ute etter, nemlig å fortsette så lenge det fremdeles er bokstaver til disposisjon.

# #### Intro til for-løkke og range()

# Som forklart over, er for-løkker egnet for tilfeller hvor antall repetisjoner er kjent. I oppgave (a) startet vi med kode:

# In[ ]:


for i in range(3):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er mye", adj + "ere!")
print("Takk for nå!")


# som repeterer 3 ganger. Du byttet deretter ut tallet 3 med en variabel for å kunne repetere et annet (men fortsatt kjent) antall ganger.
# 
# I oppgave (a) ble løkkevariabelen i ikke brukt til noe inni selve løkka, den fins kun i for-setningen. Poenget i denne løkka er bare å telle opp at den kjører 3 ganger, i har ingen mening utover det.
# 
# I andre tilfeller hvor vi bruker for-løkker kan løkkevariabelen ha en større betydning. Det er da viktig å forstå ikke bare at f.eks. range(3) fører til 3 repetisjoner, men å vite eksakt hvilken tallsekvens en range() representerer.
# 
# Generelt gjelder følgende:
# 
# * Hvis vi gir inn bare **ett tall** til range(), tolkes dette som sluttverdien. Startverdien er default 0. Sluttverdien selv er **ikke** med i sekvensen; det er "til", ikke "til og med". Eksempel:
#  * range(3) gir tallsekvensen 0, 1, 2. Løkka over kjører 3 ganger ved å ta først med i=0, så med i=1, så med i=2.
#  * range(5) gir 0, 1, 2, 3, 4
#  * range(0) gir en tom tallsekvens. Samme vil være tilfelle med negative tall; og en løkke for i in range(0): vil kjøre null ganger.
# * Hvis vi gir inn **to tall** til range(), tolkes dette som startverdi (fra og med) og sluttverdi (til, men ikke med). Eksempel:
#  * range(1, 7) gir 1, 2, 3, 4, 5, 6
#  * range(-3, 4) gir -3, -2, -1, 0, 1, 2, 3
#  * range(4, 3) gir en tom  tallsekvens (fordi sluttverdi er mindre enn startverdi)
# * Hvis vi gir inn tre tall til range(), er de to første start og slutt som før, det tredje er stegverdien. Default stegverdi er +1, så vi trenger kun angi den hvis vi ønsker noe annet enn +1. Eksempel:
#  * range(1, 10, 2) gir 1, 3, 5, 7, 9
#  * range(3, 11, 4) gir 3, 7 (men ikke 11, fordi det bare er til sluttverdien, ikke til og med)
#  * range(11, 3, -2) gir 11,  9,  7,  5 - det går altså an å bruke negative tall for stegverdi, da må startverdi være større enn sluttverdi for at løkka skal kjøre
# 
# På basis av dette kan vi endre det lille programmet over til ett som bruker variabelen i også inne i løkka, f.eks. (**Kjør gjerne selv koden med ctrl + enter, og ta gjerne å endre på verdiene for å se hva som skjer**)

# In[ ]:


for i in range(7, 14, 3):
    adj = input("Beskriv deg selv med et adjektiv? ")
    print("Hah, du", adj + "!? Jeg er", i, "ganger", adj + "ere!")
print("Takk for nå!")


# Her vil  koden fortsatt kjøre 3 ganger fordi den resulterende tallsekvensen har 3 elementer, men bruken av i inni løkka gjør programmet mer og mer skrytende. (Bare range(3) ville ikke ha sett like bra ut her, da sier den "0 ganger...", "1 ganger..." som ikke er særlig imponerende)

# Et annet eksempel (kjør koden!):

# In[ ]:


tall = int(input("Hvilket tall vil du se gangetabellen for? "))
print(str(tall)+"-gangen går slik:")
  
for i in range(1, 11):
    print(i * tall, end = "  ")
  
print("Takk for nå!")


# Merk igjen at sluttverdien er til, men ikke med, så vi må gi 11 som sluttverdi i range() for at den skal få med 70 i resultatet, dersom vi vil se hele 7-gangen.
# 
# end = "  " i print-setninga gjør at vi ikke får linjeskift mellom hvert tall men i stedet får dem etter hverandre med blanke mellom.
# 
#  
# 
# Problemet kunne alternativt ha vært løst ved å bruke tallet det skal ganges med som stegverdi. Ulempen er at range-uttrykket blir litt mer komplisert, men samtidig slipper vi nå unna med en enkelt multiplikasjon utenfor løkka i stedet for å multiplisere i hver runde av løkka:

# In[ ]:


tall = int(input("Hvilket tall vil du se gangetabellen for? "))
print(str(tall)+"-gangen går slik:")
 
for i in range(tall, tall * 10 + 1, tall):
    print(i, end = "  ")
 
print("Takk for nå!")


# Dette programmet vil gi eksakt samme utskrift som det foregående, bare oppnådd på en litt annen måte; for 7-gangen vil nå 7 være startverdi og stegverdi, og 71 sluttverdi for range().

# ## d)

#  koden under er de to første for-løkkene ferdige og gir riktig utskrift i forhold til den forklarende teksten i print-setningene.
# 
# De tre neste er ikke ferdige. Bytt ut `range(0)` i disse tre (også merket med ###) slik at for-løkkene gir tallsekvenser som passer med det som forklares i print-setningene.
# 
# **Øvelse på range()**

# In[5]:


print("Oddetallene fra 1 til 20:")
for number in range(1, 20, 2):
    print(number, end = " ")
print()
  
print("Tallene i 3-gangen mellom 12 og 25:")
for number in range(12, 25, 3):
    print(number, end = " ")
print()
  
print("Tallene i 5-gangen mellom 20 og 81:")
for number in range(20, 81, 5):
    print(number, end = " ")
print()
  
print("Tallsekvensen 48, 56, 64, 72, 80")
for number in range(48, 81, 8):
    print(number, end = " ")
print()
  
print("Telle baklengs fra 100 til 80, med intervall på -3, dvs. 100, 97, ...:")
for number in range(100, 79, -3):
    print(number, end = " ")
print()


# ## e)

# Lag et program som skriver ut tallene 1 til 5 ved bruk av en for-løkke.
# 
# ***Skriv koden din her:***

# In[6]:


for i in range(1, 6):
    print(i, end = " ")
print()


# ## f) 

# Lag et program som teller nedover fra 15 til 1 ved hjelp av en for-løkke. Skriv ut alle tallene.
# 
# ***Skriv koden din her:***

# In[7]:


for i in range(15, 0, -1):
    print(i, end = " ")
print()


# ## Evig while-løkke

# Hvis en while-løkke ikke blir stoppet kan den kjøre evig. Et eksempel er en løkke som starter ***while True*** ; da vil betingelsen alltid være sann uansett hva som skjer inni løkka. Løkka vist under vil printe Jeg elsker ITGK! et uendelig antall ganger.
# 
# Det vil vanligvis gå greit å stoppe programmet likevel, enten ved å trykke Ctrl-C eller ved å lukke vinduet der koden kjører... men **lagre for sikkerhets skyld alle filer du jobber med før du eksperimenterer med å kjøre en evig løkke**.
# 
# Eksempel på en evig løkke:

# In[ ]:


while True:
    print("Jeg elsker ITGK!")

