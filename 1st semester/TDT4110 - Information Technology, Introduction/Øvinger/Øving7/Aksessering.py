#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving7.ipynb">Øving 7</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li class="active"><a href="Aksessering.ipynb">Aksessering av karakter</a></li>
#     <li ><a href="Strenger%20og%20konkatinering.ipynb">Konkatinering</a></li>
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
# # Aksessering av karakterer i en streng
# 
# **Læringsmål:**
# 
# * Strenger
# * Funksjoner
# 
# **Starting Out with Python:**
# 
# * Kap. 8.1
# 
# Denne oppgaven handler om hvordan man får tak i og returnerer karakterer i en streng.

# ### Generelt om aksessering

# **Å iterere over strenger:**
# 
# Man kan lett iterere over en streng ved hjelp av en for-løkke. Den generelle formen for dette er:

# In[ ]:


for character in string:
    # do something


# For hver iterasjon vil character-variabelen referere til en karakter i string, og den vil starte med å referere til den første karakteren. Vi sier at løkken itererer over strengen. Prøv å kjør koden under.

# In[ ]:


name = "Bob Bernt"
for ch in name:
    print(ch)


# **Indeks:**
# 
# Å iterere over en streng med for-løkke er en måte å aksessere hver enkelt karakter i en streng. En annen måte for å aksessere karakterene i en streng på er å bruke indeks. Alle karakterene i en streng har hver sin indeks knyttet til deres plassering i strengen:
# 
# ![img](./../../Resources/Images/streng-eksempel.png)
# 
# Som man kan se på bildet, starter indekseringen med 0, akkurat som for lister. For å få tak i en av karakterene og tilordne den til en variabel, skriver man
# ch = my_string[3],
# dette vil tilordne ch til 'e'.
# 
# Hver karakter i strengen kan aksesseres vha. to tall: et positivt og et negativt. Om man skal ha tak i siste karakter i strengen kan man enten bruke 12 eller -1 som indeks, dvs. både 
# 'ch = my_string [12]' og 'ch = my_string[-1]' vil tilordne ch til 'd'. Tilsvarende vil 1 og -12 begge være indekser for 'o' i my_string.

# In[1]:


#prøv å kjøre koden
my_string = 'Roses are red'
  
for i in range(5):
    print(my_string[i])
  
for j in range(-7,0,1):
    print(my_string[j])


# ### a)

# Skriv en funksjon som tar inn en streng, itererer over denne, og skriver ut hver enkelt karakter til skjerm.
# 
# **Eksempel på kjøring**:
# 
# ```python
# #Argumentet er `Nilfgaard`
# N
# i
# l
# f
# g
# a
# a
# r
# d
# ```
# 
# ***Skriv inn koden din i kodeblokken under:***

# In[4]:


my_string = "Nilfgaard"

for i in range(len(my_string)):
    print(my_string[i])


# ### b)

# Skriv en funksjon `third_letter(string)` som tar inn en streng og returnerer den tredje bokstaven i strengen. Om lengden til strengen ikke er stor nok, skal funksjonen returnere 'q'.
# 
# ***Skriv inn koden din i kodeblokken under:***

# In[12]:


def third_letter(string):
    if len(string) >= 3:
        return string[2]
    else:
        return "q"


# Dersom du har implementert funksjonen rett, sjekk om koden under gir forventet resultat:

# In[13]:


print(third_letter("Temeria")) #skal gi "m"
print(third_letter("IT")) #skal printe ut "q"


# ### c)

# Skriv en funksjon som tar inn en streng og returnerer største gyldige indeks, dvs. den største indeksen som ikke gir IndexError.
# 
# **Eksempel på kjøring:**
# ```python
# #Argumentet er "The White Wolf"
# 13
#   
# #Argumentet er "Redania"
# 6
# ```
# 
# ***Skriv koden i kodeblokken under:***

# In[15]:


def funksjon(streng):
    x = len(streng) - 1
    return x

print(funksjon("Redania"))

