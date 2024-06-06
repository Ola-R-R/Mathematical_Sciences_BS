#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving7.ipynb">Øving 7</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Aksessering.ipynb">Aksessering av karakter</a></li>
#     <li class="active"><a href="Strenger%20og%20konkatinering.ipynb">Konkatinering</a></li>
#     <li ><a href="Slicing.ipynb">Slicing</a></li>
#     <li ><a href="Tekstbehandling.ipynb">Tekstbehandling</a></li>
#     <li ><a href="Strenghandtering.ipynb">Strenghåndtering</a></li>
#     <li ><a href="Innebygde%20funksjoner.ipynb">Innebygde funksjoner og lister</a></li>
#     <li><a href="Fjesboka.ipynb">Fjesboka</a></li>
#     <li ><a href="Akkorder%20og%20toner.ipynb">Akkorder og toner</a></li>
#     <li ><a href="Ideel%20gasslov.ipynb">Ideel Gasslov</a></li>
#     <li><a href="Sammenhengende%20tallrekke.ipynb">Sammenhengende Tallrekke</a></li>
#     <li ><a href="Sortering.ipynb">Sortering</a></li>
#     <li ><a href="Strengmanipulasjon.ipynb">Strengmanipulasjon</a></li>
#     <li ><a href="Kryptering.ipynb">Kryptering</a></li>
#     <li ><a href="Litt%20sjakk.ipynb">Litt Sjakk</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Strenger og konkatinering
# 
# **Læringsmål:**
# 
# * Strenger
# * Løkker
# * Funksjoner
# * Lister
# 
# **Starting Out with Python:**
# 
# * Kap. 7.2
# * Kap. 8.1

# ### Kort om konkatinering

# Konkatinering er å tilføye en streng ved slutten av en annen streng. Dette gjøres enten vha. + eller +=. For å bruke += må variabelen på venstre side av += være en allerede eksisterende variabel. Kjør eksemplene under og se om du skjønner hvordan de virker. Du må gjerne endre eksemplene og kjøre de igjen.

# In[1]:


# eksempel 1
# Bruk av +
melding = "Hei " + "der"
print(melding)


# In[2]:


# eksempel 2
s1 = "Hei"
s2 = "der"
melding1 = s1 + " " + s2
print(melding1)


# In[3]:


# eksempel 3
# Bruk av +=
navn = "Bob"
navn += " " + "Bernt"
print(navn)


# In[4]:


# eksempel 4
liste = ["Geralt","of","Rivia"]
navn2 = ""
for streng in liste:
    navn2 += streng + " "
print(navn2)


# In[5]:


# eksempel 5
# Vil utløse et unntak (exception) siden variabelen navnet ikke eksisterer fra før.
# Unntaket som utløses vil være NameError
navnet += "Bob"       


# ### a)

# Skriv en funksjon som tar inn to strenger (s1 og s2), og returnerer én streng bestående av disse med et mellomrom mellom.
# 
# **Eksempel**:
# ```python
# #s1 = "James", s2 = "Bond"
# -> James Bond
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[7]:


def funksjon(s1,s2):
    s3 = s1 + " " + s2
    return s3

print(funksjon("laste", "bil"))


# ### b)

# Skriv en funksjon som tar inn en liste av strenger, og returnerer én streng bestående av disse uten mellomrom mellom dem.
# 
# **Eksempel på kjøring:**
# ```python
# #list = ["abc","defg","hijklm","nop"]
# -> abcdefghijklmnop
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[11]:


def funksjon(liste):
    x = " "
    for streng in liste:
        x += streng
    return x

print(funksjon(["hei","der"]))


# ### Ikke-muterbarhet

# Strenger er ikke-muterbare, som vil si at man ikke kan endre på deler av strengen uten å lage en ny streng. Konkatinering kan gi inntrykket av å endre på en streng, mens det egentlig opprettes en ny en.

# In[ ]:


navn = "Bob"        # tilordner strengen "Bob" til variabelen navn
navn += " Bernt"    # tilordner en NY streng "Bob Bernt" til variabelen navn


# Siden strenger er ikke-muterbare, betyr det at man ikke kan endre på enkelte karakterer i strengen. Altså kan man ikke skrive string[index] = "c".

# In[ ]:


navn = "Bob Bernt"
navn[0] = "H"       # IKKE MULIG!! Vil få utløst et unntak (prøv selv)


# Om man ønsker å beholde store deler av en streng, men endre på enkelte deler av den, kan man bruke slicing til å opprette en ny streng med de ønskede endringene. Mer om slicing i neste oppgave.

# ### c)

# Skriv en funksjon som tar inn en liste med strenger og skriver ut den første karakteren i hver av dem.
# 
# **Eksempel:**
# ```python
# #list = ["UKA","lever","videre"]
# U
# l
# v
# ```
# 
# ***Skriv koden din i kodeblokken under:***

# In[27]:


def funksjon(liste):
    x = " "
    for i in range(len(liste)):
        print(liste[i][0])

funksjon(["hei","der","hei"])


# ### d)

# Hva vil kodesnutten under skrive ut til skjerm?
# 
# >```python
# def func1(liste):
#     streng = ""
#     for s in liste:
#         if len(s)>3:
#             streng += s[3]
#     return streng
# ```
# >```python  
# def func2(streng):
#     streng += streng
#     return streng
# ```
# >```python
# print(func2(func1(["Klabert","Oslo","Tur","stubbe"])))
# ```
# 
# Dobbeltklikk på teksten under for å svare.

# **Svar:** bobbob
