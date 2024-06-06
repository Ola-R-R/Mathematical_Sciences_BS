#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li class="active"><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
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
# # Varierte funksjoner
# 
# **Læringsmål:**
# - Kodeforståelse
# - Funksjoner
# 
# **Starting Out with Python:**
# - Kap. 5.1, 5.2, 5.5, 5.8
# 
# Oppgaven *grunnleggende om funksjoner* dreier seg mest om å omstrukturere eksisterende kode. I denne oppgaven skal du få prøve å skrive funksjoner helt fra grunnen av.

# ## a)

# Absoluttverdi er en funksjon med mange nyttige anvendelser, bl.a. i statistisk analyse (f.eks. utregning av standardavvik).
# 
# Python har allerede funksjonen `abs()`. Men siden dette er en enkel funksjon å lage, later vi her som om den ikke fins, slik at det er behov for å skrive den.
# 
# Kall din funksjon `absol()` så ikke navnet kolliderer med den eksisterende funksjonen. Reglene for `absol(x)` skal da være:
# 
# - hvis x >= 0, er absoluttverdien til x identisk med x
# - hvis x < 0, er absoluttverdien -x (minus minus gir pluss, absoluttverdi skal alltid være positiv)
# 
# ***Skriv koden i feltet under***

# In[11]:


def absol(x):
    
    if x >= 0:
        print("Absoluttverdi av", x, "er", x)
        return x
    else:
        y = 0 - x
        print("Absoluttverdi av", x, "er", y)
        return y

absol(float(input("Skriv inn et positivt eller negativt tall: ")))

print("Absoluttverdien til 5 er", absol(5))
print("Absoluttverdien til -3 er", absol(-3))
print("Absoluttverdien til 0 er", absol(0))


# Under har vi skrevet et test-skript slik at du kan teste funksjonen etter at du har skrevet den

# In[14]:


# skript for å teste funksjonen:
print("Absoluttverdien til 5 er", absol(5))
print("Absoluttverdien til -3 er", absol(-3))
print("Absoluttverdien til 0 er", absol(0))


# Resultat av kjøring med det gitte testskriptet skal bli:
# 
# ```python
# Absoluttverdien til 5 er 5
# Absoluttverdien til -3 er 3
# Absoluttverdien til 0 er 0
# ```
# 
# Kjør kodeblokken og sjekk om din kode gir det samme resultatet

# ## b)

# Skriv en funksjon som får inn hastighet i knop og returnerer hastighet i km/t ved hjelp av følgende opplysninger:
# 
# - 1 knop er 0.514444444 m/s
# - 1 m/s er 3.6 km/t
# 
# ***Kall funksjonen for `knop2km_t` og skriv den i feltet under***

# In[2]:


def kmop2km_t(knop):
    km_t = (knop * 0.514444444) * 3.6
    print(knop, "knop er", round(km_t, 2), "km/t")

kmop2km_t(float(input("Skriv inn hastighet i knop: ")))


# Under har du et skript for å teste funksjonen din:

# In[1]:


# testskript for knop2km_t
knop = float(input("Oppgi fart i knop:"))
km_t = knop2km_t(knop)
print("Det blir", round(km_t, 2), "km/t")


# Hvis du har skrevet funksjonen riktig skal skriptet gi følgende output:
# ```python
# Oppgi fart i knop: 15.2
# Det blir 28.15 km/t.
# ```

# ## c)

#  I England og USA har det vært vanlig å oppgi personers høyde i fot og tommer (feet, inches - såkalte **imperial** måleenheter).
# 
# Lag en funksjon med navn `imp2cm()` som får inn som parametrenen antall fot og antall tommer og returnerer antall cm som dette tilsvarer.
# 
# Til dette kan man bruke følgende opplysninger:
# 
# en fot tilsvarer 12 tommer
# en tomme tilsvarer 2.54 cm
# Funksjonen skal returnere antall cm avrundet til nærmeste heltall.
# 
# ***Skriv funksjonen din under***

# In[34]:


def imp2cm():
    fot = int(input("Oppgi antall fot: "))
    tommer = int(input("Oppgi antall tommer: "))
    cm = (fot * 12 + tommer) * 2.54
    print("Det blir", round(cm), "cm")
    
imp2cm()


# Kjør skriptet under for å teste funksjonen:

# In[ ]:


# Testskript for funksjonen imp2cm
fot = int(input("Oppgi antall fot: "))
tommer = int(input("Oppgi antall tommer: "))
cm = imp2cm(fot, tommer)
print("Det blir", cm, "cm")


# Eksempel på kjøring av testskript dersom funksjonen din er riktig:
# ```python
# Oppgi antall fot: 5
# Oppgi antall tommer: 9
# Det blir 175 cm
# ```

# ## d)

# Farger for utskrift på papir angis i CMYK, med 4 flyttall mellom 0-1 for hvor mye cyan (C), gult (Y), magenta (M) og sort (K) printerblekk.
# 
# Når farger skal vises på skjerm, angis de i RGB, dvs. som 3 heltall 0-255 som angir intensiteten av rødt (R), grønt (G) og blått (B) lys.
# 
# "Nina" har jobbet som designer av brosjyremateriell på papir og vet om mange kule farger som hun kjenner CMYK-verdiene for.
# 
# Kundene går i økende grad over til nettbasert infomateriell, så hun ønsker nå et program for å konvertere fra CMYK til RGB.
# 
# Gitt verdier for C, M, Y, K som flyttall mellom 0 og 1, er formlene for konvertering slik:
# 
# - R = 255 * (1-C) * (1-K)
# - G = 255 * (1-M) * (1-K)
# - B = 255 * (1-Y) * (1-K)
# Mesteparten av programmet er gjort ferdig av en annen programmerer, men funksjonen **cmyk2rgb()** for selve konverteringen mangler.
# 
# ***Skriv inn den manglende koden i kodeblokken nedenfor; kjør deretter koden og se om den virker.***

# In[45]:


# skriv funksjonen cmyk2rgb() her øverst
def cmyk2rgb(C, M, Y, K):
    R = round(255 * (1 - C) * (1 - K))
    G = round(255 * (1 - M) * (1 - K))
    B = round(255 * (1 - Y) * (1 - K))
    return R, G, B

print("Oppgi farge i CMYK og få det konvertert til RGB.")
C = float(input("C: "))
M = float(input("M: "))
Y = float(input("Y: "))
K = float(input("K: "))
R, G, B = cmyk2rgb(C, M, Y, K)
print("Som RGB:", R, G, B)


# #### Hint

# **Hint 1:** Du må navngi funksjonen akkurat `cmyk2rgb` hvis den skal virke med den koden som er gitt på forhånd, siden dette navnet brukes i et kall midt nede i koden.
# 
# Funksjonen må ha et antall parametre som stemmer med antallet argumenter i kallet cmyk2rgb(C, M, Y, K) -  dvs. 4 parametre.
# 
# 
# 
# **Hint 2:** Siden det står R, G, B = cmyk2rgb... i skriptet, må det komme **3 verdier** fra funksjonen for at alle disse variablene skal få innhold.
# 
# Altså trenger funksjonen å returnere 3 verdier, ikke  bare 1 som vi har sett tidligere.
# 
# Dette er imidlertid ikke spesielt vanskelig - å returnere flere verdier fra en funksjon gjøres simpelthen ved å liste opp flere returverdier med komma mellom.
# 
# F.eks., `return x, y, z` vil  returnere verdiene til 3 variable x, y, z fra en funksjon (men du kan godt gi dine variable litt mer intelligente navn)
# 
#  
# 
# **Hint 3:** C, M, Y, K  inneholder flyttall mellom 0 og 1. Utregningene med formlene  gitt over vil dermed også gi flyttall som resultat.
# 
# Du trenger imidlertid heltall 0-255 som verdier for R, G, B. Husk derfor å bruke round() eller int() på sluttresultatet av formlene før du returnerer verdier fra funksjonen.
