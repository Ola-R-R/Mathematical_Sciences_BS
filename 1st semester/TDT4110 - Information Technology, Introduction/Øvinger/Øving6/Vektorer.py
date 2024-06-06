#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving6.ipynb">Øving 6</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Generelt%20om%20lister.ipynb">Generelt om lister</a></li>
#     <li ><a href="Lett%20og%20blandet.ipynb">Lett og blandet</a></li>
#     <li ><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li class="active"><a href="Vektorer.ipynb">Vektorer</a></li>
#     <li ><a href="Lister%20og%20lokker.ipynb">Lister og løkker</a></li>
#     <li ><a href="Teoridelen%20paa%20eksamen.ipynb">Teoridelen på eksamen</a></li>
#     <li><a href="Gangetabell%20og%20lister.ipynb">Gangetabell og lister</a></li>
#     <li ><a href="Lotto.ipynb">Lotto</a></li>
#     <li ><a href="Tannfeen.ipynb">Tannfeen</a></li>
#         <li><a href="Chattebot.ipynb">Chattebot</a></li>
#     <li ><a href="Matriseaddisjon.ipynb">Matriseaddisjon</a></li>
#     <li ><a href="Intro%20til%20numpy-arrays.ipynb">Intro til numpy-arrays</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Vektorer
# 
# **Læringsmål:**
# 
# * Lister
# 
# **Starting Out with Python:**
# 
# * Kap. 7.1-7.3
# 
# I denne oppgaven skal vi studere lister bestående av tall, dvs. en vektor. Videre skal vi studere prikkprodukt og skalering av vektorer. 
# 
# En liste kan brukes til å representere en matematisk vektor.
# En av forskjellene mellom lister og vektorer er at lister kan inneholde elementer av forskjellige typer (f.eks både tall og strenger). I denne oppgaven skal du bruke lister til å implementere tredimensjonale vektorer, altså vektorer med tre elementer.
# 
# **En vektor x=(x,y,z) har lengde $\sqrt{x^{2}+y^{2}+z^{2}}$. Den kan multipliseres med tall, og vektormultipliseres med andre vektorer.**
# 
# Multiplikasjon med tall, også kalt skalarmultiplikasjon, ganger hver komponent i vektoren med et tall (skalar).
# 
# Prikkprodukt er multiplikasjon av to vektorer med samme lengde. Prikkprodukt og skalarmultiplikasjon er forklart i Eksempel 1.
# 
# Eksempel 1:
# 
# ```python
# Prikkprodukt:
# u*v = u1*v1 + v2*u2 + v3*u3, hvor v = [v1,v2,v3] og u = [u1,u2,u3]
# Numerisk eksempel:
# [3,7,1]*[2,-4,8]=3*2+7*(-4)+1*8=-14
# ```
# ```python
# Skalarmultiplikasjon:
# c*[v1,v2,v3] = [c*v1,c*v2,c*v3]
# Numerisk eksempel:
# 2*[3,7,1] = [6,14,2]
# ```
# 
# Gjennom oppgave a til f skal du lage et program som bruker forskjellige funksjoner til å gjøre forskjellige beregninger på vektorer.

# ### a)

# Lag en funksjon som lager en liste med 3 elementer, hvor alle elementene er heltall f.o.m. -10 t.o.m. 10, og returnerer denne. Benytt deg av random-biblioteket.
# 
# Eksempel på kjøring
# 
# ```python
# >>>print(make_vec())
# [0, -9, 5]
# ```
# ***Skriv svaret ditt i boksen under.***

# In[32]:


import random
def make_vec():
    liste = [random.randint(-10, 10),random.randint(-10, 10),random.randint(-10, 10)]
    return liste

print(make_vec())


# ### b)

# Lag en funksjon som tar inn en liste/vektor og et navn til denne vektoren som argumenter. Funksjonen skal skrive ut vektoren på en vakker måte.
# 
# Eksempel på utskrift:
# ```python
# >>>vector_print([1.20,4.50,4.40],'vec1')
# vec1 = [1.20, 4.50, 4.40]
# ```
# ***Skriv svaret ditt i boksen under.***

# In[35]:


def vector_print(liste, listenavn):
    x = str(listenavn) + " = " + str(liste)
    return x

vector_print([1.20,4.50,4.40],'vec1')


# ### c)

# Lag en funksjon `scalar_mult(liste,skalar)` som tar inn en liste/vektor og en skalar som argumenter. Skalarmultipliserer vektoren og returnerer den nye vektoren, liste2. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[36]:


def scalar_mult(liste, skalar):
    x = liste[0] * skalar
    y = liste[1] * skalar
    z = liste[2] * skalar
    return [x,y,z]


# Dersom du har gjort det riktig skal kodesnutten under printe lista **[4.8, 18.0, 17.6]**. Trykk `ctrl + enter` for å kjøre testen.

# In[37]:


print(scalar_mult([1.2,4.5,4.4],4))


# ### d)

# Lag en funksjon `vec_len(vektor)` som tar inn en vektor som argument, og regner ut og returnerer dens lengde. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[28]:


import math

def vec_len(vektor):
    lengde = math.sqrt((vektor[0]**2) + (vektor[1])**2 + (vektor[2])**2)
    return lengde


# Dersom du har gjort det riktig skal kodesnutten under printe tallet **5.0990195135927845**

# In[29]:


print(vec_len([1,4,3]))


# ### e)

# Lag en funksjon `vector_dot_product(vec1,vec2)` som tar inn to vektorer som argumenter og returnerer indreproduktet/prikkproduktet av de to vektorene. 
# Du kan gå ut ifra at vektorene har lik lengde. 
# 
# ***Skriv svaret ditt i boksen under.***

# In[30]:


def vector_dot_product(vec1,vec2):
    svar = vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]
    return svar


# Dersom du har gjort det riktig skal koden under printe **29.400**

# In[31]:


vec1 = [1, 4, 3]
vec2 = [2, 3.1, 5]
print(format(vector_dot_product(vec1,vec2),".3f"))


# ### f)

# Lag en main-funksjon som:
# 
# 1. Oppretter en vektor med 3 elementer (vec1).
# 2. Skriver ut vektoren på fin form.
# 3. Tar inn en skalar fra bruker. (Skal kunne ta inn både heltall og flyttall.)
# 4. Skriver ut lengden til vektoren før og etter skalering med to desimaler.
# 5. Skriver ut forholdet mellom de to lengdene. (Forholdet bør være lik skalaren.)
# 6. Skriver ut prikkproduktet mellom vektoren før skalering og vektoren etter skalering. Dvs. prikkproduktet mellom vec1 og (vec1*skalar), altså vec1*(vec1*skalar).
# 
# Eksempel på kjøring:
# 
# ```python
# vec1 = [9, 3, 0]
# Skriv inn en skalar: 2.5
# Lengden før skalering er: 9.49
# Lengden etter skalering er: 23.72
# Forholdet mellom lengden før og etter skalering er: 2.5
# Prikkproduktet av [9, 3, 0] og [22.5, 7.5, 0.0] er: 225.0
# ```
# 
# ***Skriv svaret ditt i boksen under.***

# In[59]:


import random
import math
def main():
    vec1 = [random.randint(-10, 10),random.randint(-10, 10),random.randint(-10, 10)]
    print("vec1 = " + str(vec1))
    skalar = float(input("Skriv inn en skalar: "))
    vec2 = [vec1[0] * skalar, vec1[1] * skalar, vec1[2] * skalar]
    lengdeF = math.sqrt((vec1[0])**2 + (vec1[1])**2 + (vec1[2])**2)
    print("Lengden før skalering er:", round(lengdeF, 2))
    lengdeE = math.sqrt((vec2[0])**2 + (vec2[1])**2 + (vec2[2])**2)
    print("Lengden etter skalering er:", round(lengdeE, 2))
    forhold = lengdeE / lengdeF
    print("Forholdet mellom lengden før og etter skalering er:", forhold)
    prikk = vec1[0] * vec2[0] + vec1[1] * vec2[1] + vec1[2] * vec2[2]
    print("Prikkproduktet av", vec1, "og", vec2, "er:", prikk)

main()

