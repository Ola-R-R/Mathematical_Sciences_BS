#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving9.ipynb">Øving 9</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li ><a href="Generelt%20om%20dictionary.ipynb">Generelt om dictionary</a></li>
#     <li ><a href="Innebygde%20funksjoner%20i%20dictionaries.ipynb">Innebygde funksjoner</a></li>
#     <li ><a href="Generelt%20om%20sets.ipynb">Generelt om sets</a></li>
#     <li class="active"><a href="Generelt%20om%20filbehandling.ipynb">Generelt om filbehandling</a></li>
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
# # Generelt om filbehandling
# 
# **Læringsmål:**
# - Filbehandling
# - Betingelser
# - Løkker
# 
# **Starting Out with Python:**
# - Kap. 6: Files and Exceptions
# 
# I denne oppgaven skal vi skrive til en fil og lese fra en fil.

# ## Generelt om filer
# Det kan være lurt å lese dette før du går videre

# Det er ofte nyttig å kunne lagre data til en fil, eller lese data fra en fil når man skriver et program i Python. De mest brukte funksjonene er for åpning, redigering og lukking av eksterne filer. 
# 
# Når du åpner filen må du spesifisere hvordan du skal bruke filen. Det er derfor viktig å åpne filen på riktig måte. Måten dette gjøres på er som inn-parameter i `open()`-funksjonen, noen eksempler er:
# 
# - **'r'** - for lesing av filen (default)
# - **'w'** - for skriving til filen
# - **'a'** - for å legge til data (**a**ppend) til den eksisterende filen
# 
# I denne oppgaven skal vi bli bedre kjent med hvordan dette fungerer:
# 
# - For å åpne en fil i Python kan vi skrive: `f = open('filename', Bruksmåte)`. Bruksmåte er enten `'r'`, `'w'` eller `'a'` avhengig av hva hvordan filen skal brukes.
# - For å lese data fra en fil kan vi bruke: `innhold = f.read()`
# - For å legge til data til en fil kan vi skrive: `f.write(data)`
# 
# Filer lukkes på følgende måte: `f.close()`

# ### Lesing av fil

# Eksempelet under viser lesing av en fil. **Kjør koden under og test det ut da vel!**

# In[ ]:


# LESING AV FIL
f = open('example_file1.txt','r') #r spesifiserer at man skal lese fra en fil
innhold = f.read()
print(innhold)
f.close()


# Når man leser en fil slik som over, må man lagre innholdet i en variabel (her bruker vi `innhold`). **Husk alltid å lukke filen!**
# 
# Filen som ble lest, _example_file1.txt_ finnes i [denne mappen](https://itgkhub.apps.stack.it.ntnu.no/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgitlab.stud.idi.ntnu.no%2Fitgk2020%2Fitgk-2020-vinger&urlpath=tree%2Fitgk-2020-vinger%2FOvinger%2FOving09&branch=master). Følg lenken, åpne _example_file1.txt_ og endre på filen. Lagre endringene med `file -> save` i toppmenyen. Kjør så kodeblokken over på nytt - blokken burde da skrive ut det nye innholdet i filen!

# ### Skriving av fil

# For å skrive til en fil kan man gjøre slik som under. **Kjør koden under og test!**

# In[ ]:


f = open('example_file1.txt','w')  #w spesifiserer at filen skal skrives til
f.write('En hatefull ytring')
f.close()


# Etter at du har kjørt koden over vil du kunne se at innholdet i _example_file1.txt_ har endret seg. Hvis du vil kan du bytte ut `'w'` over med `'a'` og se hva som da skjer.

# ## a)

# Lag en funksjon `write_to_file(data)` som tar inn strengen `data` og legger denne inn i en fil **my_file.txt**
# 
# ***Skriv din kode i kodeblokken under***

# In[ ]:


def write_to_file(data):
    f = open("my_file.txt", "w")
    f.write(data)
    f = open("my_file.txt", "r")
    innhold = f.read()
    print(innhold)
    f.close()

write_to_file("hei")


# Hvis du lurer på om du gjorde riktig kan du kalle på funksjonen og sjekke innholdet i filen ved å åpne den på samme måte som med _example_file1.txt_, altså å åpne _my_file.txt_ gjennom [denne mappen](https://itgkhub.apps.stack.it.ntnu.no/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgitlab.stud.idi.ntnu.no%2Fitgk2020%2Fitgk-2020-vinger&urlpath=tree%2Fitgk-2020-vinger%2FOvinger%2FOving09&branch=master).

# #### Hint

# Her skal du skrive til fil og må derfor benytte deg av
# 
# ```python
# f = open('my_file.txt', 'w')
# ```

# ## b)

# Lag en funksjon `read_from_file(filename)` som tar inn strengen `filename` med filnavnet og skriver ut innholdet.
# 
# ***Skriv koden i kodeblokken under***

# In[ ]:


def read_from_file(filename):
    f = open(filename, "r")
    innhold = f.read()
    print(innhold)
    f.close()

read_from_file("my_file.txt")


# Du kan teste ut funksjonen ved å kalle den med `'my_file.txt'` som argument.

# #### Hint

# Her skal du lese fra fil og må derfor benytte deg av
# ```python
# f = open('my_file.txt', 'r')
# ```

# # c)

# Lag en funksjon `main()` hvor bruker får valget mellom å skrive til fil eller lese fra fil. Funksjonen skal kjøre så lenge brukeren ikke svarer `'done'`. (Se eksempelkjøring)
# 
# - Hvis brukeren velger **write** skal du bruke **a)** til å skrive data til **my_file.txt**
# - Hvis brukeren velger **read** skal du skrive ut innholdet (dersom det er noe) i **my_file.txt** vha. **b)**
# 
# **Eksempel på kjøring:**
# ```
# Do you want to read or write? write
# What do you want to write to file? hei allan
# hei allan was written to file.
# Do you want to read or write? read
# hei allan
# Do you want to read or write? done
# You are done.
# ```
# 
# ***Skriv koden din i kodeblokken under***

# In[3]:


def main():
    svar = input("Do you want to read or write?")
    if svar.lower() == "write":
        tekst = input("What do you want to write to file?")
        f = open("my_file.txt", "w")
        f.write(tekst)
        f.close()
        print(tekst, "was written to file.")
    elif svar.lower() == "read":
        f = open("my_file.txt", "r")
        innhold = f.read()
        print(innhold)
        f.close()
    elif svar.lower() == "done":
        print("You are done.")

main()


# Du kan når som helst sjekke innholdet i _my_file.txt_ ved å åpne den fra [denne mappen](https://itgkhub.apps.stack.it.ntnu.no/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgitlab.stud.idi.ntnu.no%2Fitgk2020%2Fitgk-2020-vinger&urlpath=tree%2Fitgk-2020-vinger%2FOvinger%2FOving09&branch=master).
