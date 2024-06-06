#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li class="active"><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
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
# # Intro til nøstede løkker
# 
# **Læringsmål:**
# 
# * Nøstede løkker
# 
# **Starting out with python:**
# 
# * Kap. 4.7
# 
# I denne oppgaven skal du lære hvordan vi kan benytte oss av en løkke inne i en annen løkke. 

# ### Intro til nøstede løkker

# Nøstede løkker vil si løkker som er inni andre løkker. Et eksempel på en nøstet løkke er en dobbel løkke, som vil si at det er en løkke inni en annen løkke. Doble løkker brukes mye i programmering, typisk når man skal løse problemer som på en eller annen måte er todimensjonale, f.eks. knyttet til matriser eller todimensjonale tabeller med tall. Todimensjonal her kan bety rent visuelt (f.eks. at man skal tegne noe på en skjerm og må oppdatere fargen i hvert punkt i et rutenett av piksler), men behøver ikke å ha noen visuell betydning. Det kan være snakk om dimensjoner av informasjon på en mer abstrakt måte. F.eks. kan de to dimensjonene være tall og verdier i kortstokken, vi kan da generere en hel kortstokk ved en dobbel løkke som følger:

# In[ ]:


for farge in ['♠', '♣', '♥', '♦']:
    for verdi in ['A', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K']:
        print(farge+verdi, end=" ")
    print()


# Den innerste løkka går 13 runder hver gang den kjører fordi det er 13 elementer i sekvensen som gis til for-løkka. Den printer de 13 kortene i en farge; end=" " i print-setninga gjør at vi ikke skifter linje men bare setter en blank mellom hvert kort.
# 
# print() nederst tilhører den ytre løkka (merk margen), denne sørger for at vi skifter linje etter hver rekke. Den ytre løkka går 4 ganger, en for hver farge i kortstokken

# ## a)

# **Eksempel på nøstet løkke:**

# In[ ]:


for x in range(5):
    for y in range(3):
        print("Jeg elsker ITGK! ", end=" ")
    print()


# Koden over vil skrive ut “Jeg elsker ITGK!” tre ganger ved siden av hverandre fem ganger nedover.
# 
# Kopier koden i eksemplet "Jeg elsker ITGK!" over og kjør programmet. Denne utskriften trenger man strengt tatt ikke dobbel løkke for å få til; selve utskriften gir riktig nok et todimensjonalt inntrykk, men siden den underliggende informasjonen ikke er todimensjonal men derimot konstant (samme utskrift "Jeg elsker ITGK!" i alle tilfeller), er det også greit mulig å klare dette med enkel løkke, eller helt uten løkker, som følger:

# In[4]:


# Løsning med enkel løkke:
#for x in range(5):
 #   print("Jeg elsker ITGK!  Jeg elsker ITGK!  Jeg elsker ITGK!")

# Løsning uten løkker; "\n" er tegnet for linjeskift (newline på engelsk)
#print((("Jeg elsker ITGK!  " * 3) + "\n") * 5)

antallStudenter = int(input("Hvor mange studenter? ")) + 1
antallEmner = int(input("Hvor mange emner? ")) + 1

for Student in range(1, antallStudenter):
    for Emne in range(1, antallEmner):
        print("Stud", Student, "elsker Emne", Emne, ";", end=" ")
    print()


# Hvis vi derimot endrer litt på kravene til programmet, så det skal handle om flere studenter enn "Jeg" og flere emner enn "ITGK", vil vi ha et genuint todimensjonalt problem (én dimensjon er studenter, en annen emner) hvor dobbel løkke vil være klart enkleste løsning. **Din oppgave: endre programmet så det gir utskrift som vist nedenfor**. Fra forrige oppgave skal altså Jeg byttes ut med Stud &lt;nummer>, og ITGK skal byttes ut med Emne &lt;nummer>. Brukeren skal angi ønsket antall for både studenter og emner, 4 og 3 er bare eksempler.
# 
# ```
# Hvor mange studenter? 4
# Hvor mange emner? 3
# Stud 1 elsker Emne 1 ; Stud 1 elsker Emne 2 ; Stud 1 elsker Emne 3 ;
# Stud 2 elsker Emne 1 ; Stud 2 elsker Emne 2 ; Stud 2 elsker Emne 3 ;
# Stud 3 elsker Emne 1 ; Stud 3 elsker Emne 2 ; Stud 3 elsker Emne 3 ;
# Stud 4 elsker Emne 1 ; Stud 4 elsker Emne 2 ; Stud 4 elsker Emne 3 ;
# ```
# 
# **EKSTRA UTFORDRING** (ikke nødvendig for å få godkjent (a)): For å gjøre programmet litt mindre tørt og abstrakt, kan du prøve å endre så det skriver fornavn på personer i stedet for "Stud x", og navn på faktiske emner i stedet for Emne y - jfr eksempel med kortstokk i teksten "Intro til nøstede løkker" øverst i denne oppgaven. For å gjøre det mindre forutsigbart, kan du dessuten bruke funksjonen random() for å generere tilfeldige tall for hver runde av løkka, og ha en if-setning for å velge verb basert på verdien av dette. F.eks. "elsker" bare hvis tallet ble > 0.9, og gradvis litt mer beskjedne verb til lavere tallverdien var.

# ## b)

# Bruk en dobbel løkke til å skrive ut en liste over alle klokkeslett i løpet av et døgn på en fin måte. Du trenger kun å tenke på timer og minutter. Klokkeslettene skal gå fra 0:0 til 23:59 som vist nedenfor.
# 
# Eksempel på kjøring av kode:
# 
# ```python
# 0:0
# 0:1
# 0:2
# .
# .       # Alle klokkeslett i mellom her skal skrives ut
# .
# 23:58
# 23:59```
# 
# ***Skriv koden din her:***

# In[25]:


for timer in range(24):
    for minutter in range(60):
        print(str(timer) + ":" + str(minutter))


# ## c)

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Bruk doble løkker til å skrive ut alle tallene i den lille gangetabellen, dvs. lag to for-løkker opp til 11 og multipliser variabelen x fra den ene løkken med variabelen y fra den andre løkken og skriv det ut i den innerste løkken. Du trenger ikke å tenke på formatet til utskriften.
# 
# Eksempel på kjøring:
# 
# ```python
# 1
# 2
# 3
# 4
# 5
# .
# .
# .
# 60
# 70
# 80
# 90
# 100
# ```
# ***Skriv koden din her:***

# In[27]:


for x in range(1, 11):
    for y in range(1, 11):
        print(x * y)
    print()


# **Bonus**: Forsøk å legg inn en tom print() etter den innerste løkken i c) har kjørt (dvs. på samme innrykk som innerste for, men nedenfor print-funksjonen som skriver ut tallene). Legg også til end = '  ' på slutten av print-funksjonen som printer ut tallene. Ser du nå at det ligner mer på en gangetabell?
