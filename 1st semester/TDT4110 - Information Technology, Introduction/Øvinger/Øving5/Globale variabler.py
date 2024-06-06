#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving5.ipynb">Øving 5</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Grunnleggende%20om%20funksjoner.ipynb">Grunnleggende om funksjoner</a></li>
#     <li><a href="Varierte%20funksjoner.ipynb">Varierte funksjoner</a></li>
#     <li><a href="Lokale%20variabler.ipynb">Lokale variabler</a></li>
#     <li class="active"><a href="Globale%20variabler.ipynb">Globale variabler</a></li>
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
# # Globale variabler
# 
# **Læringsmål:**
# - Funksjoner
# 
# **Starting Out with Python:**
# - Kap. 5.6

# ## Generelt om globale variabler
# 
# Det kan være lurt å lese gjennom dette før du går videre

# En global variabel er en variabel som kan aksesseres av alle funksjonene i et program, ved at den opprettes utenfor en funksjon. Globale variabler kan for eksempel brukes for å lagre data som man trenger å huske gjennom hele programutførelsen. Selv om bruk av globale variabler kan være praktisk, er det ofte bedre å bruke lokale variabler i for eksempel en main-funksjon, og så sende dette videre til andre funksjoner ved behov. Ulempen ved å ha funksjoner som bruker globale variabler, er tapet av forutsigbarhet. Funksjonene vil ikke lengre oppføre seg kun som en matematisk funksjon som alltid spytter ut samme svar gitt samme input, men vil kunne oppføre seg forskjellig basert på tilstanden til de globale variablene som funksjonen bruker. Dette betyr at i praksis brukes globale variabler som oftest for å lagre konstanter, altså variabler som bare leses og ikke endres. Slike variabler bruker ofte kun store bokstaver i navnet.

# In[ ]:


# EKSEMPEL PÅ GLOBALE VARIABLER BRUKT FOR Å LAGRE KONSTANTER
# Det er verdt å merke seg at denne konstanten også
# er definert i Pythons innebygde math-bibliotek
PI = 3.1415926
  
# Funksjon som finner omkretsen til en sirkel med gitt radius
def omkrets(radius):
    return 2 * PI * radius
  
# Funksjon som finner arealet til en sirkel med gitt radius
def areal(radius):
    return PI * radius ** 2


# Som sagt er det også mulig å endre på globale variabler. For å gjøre dette, må man eksplisitt informere om at man skal bruke en global variabel med å bruke nøkkelordet global. Dette er illustrert i eksempelet under, hvor det er verdien som settes i fra kallet til funksjon a som blir stående, selv om b også endrer en variabel med samme navn og kjører etter at funksjon a kjører. Det som skjer her, er at i b lagres tallet i en lokal variabel med samme navn.

# In[ ]:


# HVORDAN ENDRE GLOBALE VARIABLER
stored_number = 30
  
def a():
    global stored_number
    stored_number = 20

def b():
    stored_number = 10

a()
b()
  
print(stored_number) # => 20


# ## Funksjoner med valgfrie argumenter
# 
# Det kan være lurt å lese gjennom dette før du går videre

# I Python er det mulig for et funksjonsargument å ha en default-verdi. Hvis en funksjon kalles uten en verdi for dette funksjonsargumentet, vil argumentet få denne default-verdien - koden kan altså fortsatt kjøre, selv om man gir funksjonen færre argumenter enn den egentlig tar inn. Du kan definere at en funksjon har default-verdier som vist i koden under.

# In[5]:


# Printer navnet til brukeren med store bokstaver i starten av hvert ord
def pretty_print_name(name, message = 'Hei'):
    print(message, name.title())
    
pretty_print_name('ola nOrDMaNN')
pretty_print_name('OLA Nordmann', 'Hello')


# ## a) Lagring av konstanter

# Gravitasjonsakselerasjonen g på jordoverflaten er omtrent 9.81 m/s². For våre formål kan denne antas å være konstant. Tiden som trengs for at et objekt i fritt fall skal ramle d meter er gitt ved formelen
# \begin{equation*}
# t = \sqrt{\frac{2d}{g}}
# \end{equation*}
# hvor $g$ er gravitasjonsakselerasjonen som gitt tidligere.
# 
# I denne deloppgaven skal du lagre gravitasjonskonstanten i en global variabel med navnet `GRAVITY` på toppen av programmet ditt. Deretter skal du lage en funksjon `get_fall_time` som tar inn et gitt antall meter, og bruker formelen gitt over til å returnere hvor lang tid det tar et objekt å ramle det gitte antallet meter. La så programmet ditt ta inn en fall-lengde i meter fra brukeren, og bruk funksjonen du har laget til å regne ut hvor lang tid det tar å ramle den gitte distansen. Print ut resultatet.
# 
# ***Skriv koden i kodeblokken under***

# In[ ]:


import math
GRAVITY = 9.81

def get_fall_time():
    d = float(input("Antallet meter objektet skal ramle: "))
    t = math.sqrt((2 * d) / GRAVITY)
    return t, d


t, d = get_fall_time()
print("Det tar", t, "sekunder å ramle", d, "meter")


# Eksempel på kjøring:
# ```python
# Antallet meter objektet skal ramle: 20
# Det tar 2.019275109384609 sekunder å ramle 20 meter
# ```

# ## b) Oppdatere en global variabel
# 
# I denne oppgaven ønsker vi å legge til rette for flere verdier av gravitasjonsakselrasjonen, ettersom denne ikke er helt konstant over hele jordoverflaten, i tillegg til at den vil være forskjellig på f.eks. månen. En mulig måte å løse dette på kunne vært å introdusere en ny funksjon som lar brukeren overskrive verdien til den globale konstanten, som vist i følgende eksempel.
# 
# ```python
# def set_gravity(gravity):
#   global GRAVITY
#   GRAVITY = gravity
#  
# set_gravity(9.67)
#  
# print(get_fall_time(20)) # => 1.4381419703158196
# ```
# Synes du dette er en god løsning på problemet? ***Argumenter for eller i mot denne løsningen***  
# ***Dobbeltklikk på teksten under og skriv i feltet som dukker opp***

# Svar: 

# I tillegg skal du skrive om om funksjonen din fra oppgave a slik at den tar inn et ekstra parameter som lar deg sette hvilken verdi for gravitasjonsakselerasjonen som skal brukes. Parameteret skal ha konstanten GRAVITY som default-verdi. Under demonstreres hvordan denne nye funksjonen skal kunne brukes:
# 
# >```python
# print(get_fall_time(20)) # => 2.019275109384609
# print(get_fall_time(20, 1.62)) # => 4.969039949999533
# ```
# 
# ***Kopier inn koden din fra oppgave a) nedenfor og gjør den om etter beskrivelsen over***

# In[8]:


import math
GRAVITY = 9.81

def get_fall_time(d, gravity = GRAVITY):
    #d = float(input("Antallet meter objektet skal ramle: "))
    t = math.sqrt((2 * d) / gravity)
    print("Det tar", t, "sekunder å ramle", d, "meter")


# Du kan teste ut funksjonen din med denne koden som burde kjøre likt som demonstrasjonen over. (husk å kjøre funksjonen i kodeblokken over før du kjører kodeblokken under slik at funksjonen er oppdatert)

# In[9]:


print(get_fall_time(20))
print(get_fall_time(20, 1.62))

