#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li class="active"><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li ><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
#     <li ><a href="Osteviruset.ipynb">Osteviruset</a></li>
#     <li ><a href="Bursdagsdatabasen.ipynb">Bursdagsdatabasen</a></li>
#     <li ><a href="Tallak%20teller%20antall%20tall.ipynb">Tallak teller antall tall</a></li>
#     <li ><a href="Opptaksgrenser.ipynb">Opptaksgrenser</a></li>
#         <li ><a href="Soke%20i%20tekst.ipynb">Søke i tekst</a></li>
#     <li ><a href="Tre%20paa%20rad.ipynb">Tre på rad</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Innebygde funksjoner i dictionaries
# 
# **Læringsmål:**
# - Dictionaries
# - Innebygde funksjoner
# 
# **Starting Out with Python:**
# - Kap. 9.1

# ## Info om innebygde innebygde funksjoner
# 
# Det kan være lurt å lese gjennom dette før du går videre

# Akkurat som at det eksisterer mange innebygde funksjoner for lister, eksisterer det også mange innebygde funksjoner for dictionaries. Fra øving 6 husker du kanskje at du ble introdusert for len() som returnerer lengden til en liste, dvs. antall elementer i listen. Denne funksjonen kan også benyttes på dictionaries. Kjør kodeblokken under og se hva som skjer.

# In[3]:


dictionary = {}
dictionary['red'] = 'primærfarge'
num_items = len(dictionary) 
print(num_items)
dictionary['blue'] = 'primærfarge'
dictionary['green'] = 'sekunærfarge'
num_items2 = len(dictionary)
print(num_items2)


# Dersom du prøver å få tak i en verdi fra en nøkkel som ikke er lagt inn, vil du få en feilmelding. For å hindre dette kan det være lurt å sjekke om nøkkelen er i dictionaryen.

# In[2]:


if 'yellow' in dictionary:
    print(dictionary['yellow'])


# Som du ser skjer det ingenting når man kjører koden over. Dette er fordi 'yellow' ikke finnes i dictionaryen. Hvis du vil kan du prøve å fjerne if-setningen og se hva som da skjer.
# 
# Man kan også fjerne elementer ganske greit i en dictionary, ved bruk av del og pop() som under:

# In[6]:


if 'green' in dictionary:
    del dictionary['green']  # green: sekundærfarge blir nå slettet fra dictionaryen
print(dictionary.pop('blue', 'Entry not found'))  # blue: primærfarge blir nå slettet fra dictionaryen og primærfarge returneres.


# 'Entry not found' er her en default-verdi som blir returnert dersom nøkkelen 'blue' ikke finnes i dictionaryen. Hvis du kjører kodeblokken over to ganger vil du se at 'Entry not found' blir printet den andre gangen. 
# 
# Dersom det er ønskelig å tømme hele dictionaryen kan en bruke `dictionary.clear()`.

# Ettersom en dictionary består av elementer som inneholder både en nøkkel og en verdi, er det litt mer avansert å iterere gjennom en dictionary enn en liste.
# 
# La oss tenke oss at vi har følgende dictionary:

# In[7]:


my_family={'bror': 'Martin', 'søster': 'Helene', 'mor': 'Anne', 'far': 'Bob Bernt', 'hund': 'Lovise'}


# Dersom du ønsker å iterere gjennom alle nøklene i dictionaryen, dvs. 'bror', 'søster', 'mor', 'far' og 'hund' kan du skrive for-løkken som under. **Kjør bare koden under dersom du har kjørt koden over først.**

# In[8]:


for key in my_family:
    print(key)


# Dersom du ønsker å skrive ut alle nøklene samt navnene til familiemedlemmene kan du skrive:

# In[9]:


for key in my_family:
    print(key, my_family[key])


# En annen måte å få denne utskriften på, altså en iterering som itererer gjennom både verdier og nøkler samtidig, er ved å bruke følgende format:

# In[10]:


for key, value in my_family.items():
    print(key, value)


# `items()` returnerer alle nøklene i en dictionary samt deres tilhørende verdier.
# 
# Dersom det hadde vært ønskelig å kun printe ut verdiene, dvs. navnene, kunne man benyttet seg av `values()`:

# In[11]:


for val in my_family.values():
    print(val)


# ## a)

# Gitt følgende dictionary:
# 
# ```python
# scores = {'Amanda': [88, 92, 100], 'Kennet': [30, 45, 50], 'Einstein': [100,100,100]}
# ```
# 
# 1. hva skrives ut dersom vi skriver `print(scores['Amanda'])`
# 2. hva skrives ut dersom vi skriver `print(scores['Amanda'][2])`

# **Ditt svar:** a) [88, 92, 100], b) 100

# ## b)

# Opprett en tom dictionary som kalles fruit, for så å legge til tre frukter du liker som nøkler, og antall frukt av denne typen du pleier å spise hver dag som verdi.
# 
# **Eksempel**
# ```python
# fruit = {'epler': 2, 'pærer': 3, 'appelsiner': 1}
# ```
# 
# ***Skriv koden i kodeblokken under***

# In[62]:


fruit = {}
fruit["vannmelon"] = 0
fruit["mango"] = 0
fruit["appelsiner"] = 0

print(fruit)


# ## c)

# Legg til to frukter som du misliker og fjern de tre fruktene du liker. Benytt deg av de innebygde funksjonene `del()` og `dict[key]=value`.
# 
# ***Skriv koden i kodeblokken under***

# In[64]:


del fruit["vannmelon"]
del fruit["mango"]
del fruit["appelsiner"]

fruit["epler"] = 0
fruit["pærer"] = 0

print(fruit)


# ## d)

# Skriv ut begge verdiene (antall frukt du spiser hver dag som du misliker) i dictionaryen.
# 
# ***Skriv koden i kodeblokken under***

# In[58]:


for val in fruit.values():
    print(val)


# Eksempel på kjøring dersom `fruit = {'bananer': 0, 'druer': 1}`:
# ```
# 0
# 1
# ```

# ## e)

# Sjekk om 'bananer' er i dictionaryen, og fjern 'bananer' fra dictionaryen dersom den er oppført.
# 
# ***Skriv koden din på angitt plass i kodeblokken under***

# In[67]:


fruit = {'bananer': 0, 'druer': 1}
print(fruit)

if "bananer" in fruit:
    del fruit["bananer"]

print(fruit)


# Hvis du har gjort alt riktig skal output fra koden over være:
# ```
# {'bananer': 0, 'druer': 1}
# {'druer': 1}
# ```

# ## f)

# Legg til et par bær som du liker i dictionaryen og skriv ut både verdiene og nøklene i dictionaryen på et greit format.
# 
# ***Skriv koden din i kodeblokken under***

# In[68]:


fruit["jordbær"] = 2
fruit["blåbær"] = 2

for key, value in fruit.items():
    print(key, value)


# **Eksempel på utskrift:**
# ```
# epler 2
# pærer 0
# jordbær 10
# blåbær 50
# ```

# #### Hint

# Benytt deg av for key, value in fruit.items().
