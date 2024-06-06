#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li class="active"><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#     <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Generelt om dictionary
# 
# **Læringsmål:**
# - Dictionary
# 
# **Starting Out with Python:**
# - Kap. 9: Dictionaries

# ## Generelt om dictionaries

# En dictionary er et objekt som lagrer en samling av data, og kan minne mye om en liste. Det som skiller en dictionary fra en liste er at hvert element i en dictionary består av to deler: En nøkkel(a key) og en verdi(a value). En nøkkel peker til en verdi, og man bruker nøkkelen for å hente ut verdien.
# 
# - key: Nøklene kan være flyttall, heltall strenger eller tupler. Nøklene må være unike.
# - values: Innholdet som nøkkelen peker til. Dette kan være lister, strenger, heltall, osv.
# 
# For eksempel kan du tenke på en engelsk-norsk ordbok hvor engelske ord er ramset opp i alfabetisk rekkefølge, og til hvert engelske ord finner du en rekke norske alternativer for dette ordet.
# 
# ![img](./../../Resources/Images/dictionary_eksempel.png)
# 
# På bildet over er "Learning" nøkkelen, mens verdien kan være en liste av de norske alternativene, verdi = \[bli opplært, innlæring, lærdom etc.\]. For å få tak i denne verdien (listen med norske oversettelser) må man slå opp på nøkkelen (Learning).
# 
# En dictionary opprettes på to måter
# 
# - dictionary = dict()
# - dictionary = {}, til forskjell fra lister er det her krøllparenteser(bracets) og ikke hakeparenteser.
# 
# Et eksempel på bruk av dictionaries er gitt nedenfor:

# In[ ]:


telephone_numbers = {'arne': 99748391, 'knut': 74839220, 'siri': [92835674, 65748329]}  # Oppretter en dictionary med tre oppføringer
print(telephone_numbers['knut'])  # Skriver ut knut sitt telefonnummer
print(telephone_numbers['siri'][1])  # Skriver ut det andre telefonnummeret i listen av Siri sine telefonnummer


# Her er 'arne' den første nøkkelen, og 99748391 er den tilhørende verdien. 'knut' er den andre nøkkelen og 'siri' er den siste nøkkelen.
# 
# For å legge til et nytt key-value-par i dictionarien kan du gjøre følgende:

# In[ ]:


telephone_numbers['stian'] = 82935829  # Legger Stian til i dictionarien
print (telephone_numbers)  # Skriver ut hele telefonlisten


# Dersom du skal ha tak i en verdi, må du slå opp på nøkkelen. La oss si at du ønsker å vite nummeret til arne, da må du skrive følgende:

# In[ ]:


telephone_numbers['arne']


# # a)

# ***Opprett en tom dictionary my_family i kodeblokken under.***

# In[1]:


my_family = {}


# # b)

# Lag en funksjon `add_family_member(role, name)` som tar inn to strenger, `rolle`(key) og `navn`(value), og legger familiemedlemmet til i dictionaryen `my_family`.
# 
# ***Skriv koden din i kodeblokken under***

# In[2]:


def add_family_member(role, name):
    my_family[role] = name


# For å teste koden din kan du kjøre kodeblokken under. 

# In[3]:


add_family_member('bror', 'Arne')
print (my_family)
add_family_member('far', 'Bob Bernt')
print (my_family)


# Hvis du har gjort alt riktig skal output fra blokken over bli:
# ```
# {'bror': 'Arne'}
# {'bror': 'Arne', 'far': 'Bob Bernt'}
# ```

# # c)

# Hvis du ønsker å legge til flere familiemedlemmer med samme rolle (f.eks. to brødre), må du lage en liste som inneholder alle dine brødre.
# 
# Når du har gjort dette kan du bruke vanlige liste-metoder som .append() og .pop() for å legge til eller fjerne elementer fra listen.
# 
# *Nå skal du utvide funksjonaliteten fra b) slik at du kan legge til flere familiemedlemmer med samme rolle.*
# 
# 
# **Hint:** 
# - Du må ha en liste med navn for hver rolle.
# 
# - For å sjekke om en rolle finnes fra før av kan du bruke "if key in dict". Du kan også løse dette med unntakshåndtering.
# 
# ***Kopier koden din fra oppgave b) til kodeblokken under og utvid programmet til å støtte flere familiemedlemmer med samme rolle***

# In[15]:


def add_family_member(role, name):
    if role in my_family:
        my_family[role].append(name)
    else:
        my_family[role] = [name]


# For å teste koden kan du kjøre kodeblokken under

# In[16]:


my_family={}
add_family_member('bror', 'Arne')
add_family_member('mor', 'Anne')
add_family_member('bror', 'Geir')
print (my_family)


# Hvis du har gjort alt riktig skal output fra denne bli:
# ```
# {'mor': ['Anne'], 'bror': ['Arne', 'Geir']}
# ```

# # d) (frivillig)

# *(Du trenger ikke gjøre denne for å få godkjent oppgaven)* ***Skriv ut den ferdige dictionarien på et fint format med kodeblokken under***

# In[ ]:





# #### Hint

# Du kan bruke en for-løkke med syntaksen for key, value in my_family.items(): for å iterere gjennom dictionarien. 
