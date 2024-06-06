#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving2.ipynb">Øving 2</a>
#     </div>
#     <ul class="nav navbar-nav">
#     <li><a href="Ulike%20typer%20if-setninger.ipynb">Ulike typer if-setninger</a></li>
#     <li><a href="Sammenligning%20av%20strenger.ipynb">Sammenligning av strenger</a></li>
#     <li><a href="Logiske%20operatorer%20og%20logiske%20uttrykk.ipynb">Logiske operatorer og logiske uttrykk</a></li>
#     <li class="active"><a href="Forbrytelse%20og%20straff.ipynb">Forbrytelse og straff</a></li>
#     <li><a href="Aarstider.ipynb">Årstider</a></li>
#         <li ><a href="Tekstbasert%20spill.ipynb">Tekstbasert spill</a></li>
#     <li><a href="Sjakkbrett.ipynb">Sjakkbrett</a></li>
#     <li><a href="Billettpriser%20og%20rabatter.ipynb">Billettpriser og rabatter</a></li>
#     <li><a href="Skatteetaten.ipynb">Skatteetaten</a></li>
#     <li><a href="Epletigging.ipynb">Datamaskinen som tigget epler</a></li>
#     <li><a href="Andregradsligning.ipynb">Andregradsligning</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Forbrytelse og straff

# **Læringsmål:**
# - Kodeforståelse, hvordan tenke om oppsett av if-setninger
# - Kunne forstå og rette typiske feil med if-setninger
# 
# **Starting Out with Python:**
# - Kap. 3.1-3.2

# I denne oppgaven skal vi rette kodefeil og lære hvordan man tenker om strukturen av både enkle og komplekse if-setninger.

# #### Forklaring av syntaksfeil (hint oppg a)

# Noen typiske syntaksfeil som nybegynnere gjerne gjør i bruk av if-setninger:
# 
# - Glemme kolon bakerst i linjer med `if`, `else` og `elif`. Det må være kolon `:` disse stedene
# - Feil med logiske operatorer, f.eks. bruke tilordning = når man egentlig mener sammenligning `==`. Eller unødig mellomrom i operatorer som skrives med to symboler, som `> =`, disse må stå helt inntil hverandre
# - Feil med parenteser som ikke matcher i sammensatte logiske uttrykk med `and`, `or`, `not`
# - Feil med marg / innrykk - alle setninger som hører til en if må stå med eksakt ett tabulator-innrykk, en else må stå på eksakt samme marg som den if den hører sammen med, etc. Bare ett mellomrom i forskjell vil være nok til at koden feiler.

# ## a) Syntaksfeil

# Kjør koden under. Som du vil se, inneholder den syntaksfeil i de nederste linjene (if-else-setningen).
# 
# ***Rett alle syntaksfeilene, slik at koden kjører*** og gir en konklusjon ut på skjermen (om det var promillekjøring eller ikke) – for denne deloppgaven behøver ikke konklusjonen være riktig, det er nok å få programmet til å kjøre. NB! Du skal **ikke** slette noen kodelinjer eller betingelser!

# In[8]:


# leser inn data
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ")
f = input("Var personen fører av vognen? (j/n) ")
leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
n = input("Var det nødrett? (j/n) ")
 
# vurderer straffbarhet
if prom > 0.2 and motor == "j" and (f == "j" or leds == "j") and n == "n":
    print("Det var straffbar promillekjøring.")
else:
    print("Ikke straffbart, ingen bot.")


# ## b) Enkle logiske feil

# ***Jobb videre med koden fra oppgave (a) hvor du korrigerte syntaksfeilene. Prøv ut programmet med følgende input:***
# 
# - promille = 0.1, motor = "j", fører = "j", ledsager = "n", nødrett = "n". Du vil da se at programmet feilaktig sier at det var promillekjøring selv om promillen var for liten. ***Rett denne feilen (men ikke noe annet)***, kjør programmet med samme input og se at det nå konkluderer rett, test også med promille 0.3 men ellers samme input og se at det gjør rett med dette også. 
# - Kjør deretter programmet med følgende input: promille = 0.1, motor = "j", fører = "n", ledsager = "j", nødrett = "n". Du vil se at programmet igjen feilaktig konkluderer med promillekjøring, til tross for rettingen du gjorde i sted. Dette skyldes en litt mer komplisert feil i betingelsen. ***Rett denne feilen*** og test deretter at koden nå virker som den skal med litt ulike kombinasjoner av verdier.

# #### Enkle logiske feil (hint oppgave b)

# Vi går nå videre med enkle logiske feil, som vil føre til at if-setninger kommer til feil konklusjon. Typiske eksempler på slike feil:
# 
# **(I)** Bruk av feil sammenligningsoperator, f.eks. `<` i stedet for `>`, eller `>` i stedet for `>=`. Koden under viser ett eksempel på dette:

# In[ ]:


alder = int(input("Alder: "))
if alder > 18:
    print("Kunden har lov til å kjøpe vin")


# Her vil kunden måtte være 19 eller mer for en positiv konklusjon, mens det skulle holdt med 18. Dvs., operatoren skulle vært `>=` , ikke `>`
# 
# **(II)** Bruk av feil operator (typisk forveksle `and` og `or`) i sammensatte betingelser, eller feil / manglende parentesbruk i sammensatte betingelser. Koden under viser to feilaktige forsøk på å beslutte om en kunde kan kjøpe vin eller ikke (forrige feil med `>=` rettet):

# In[ ]:


# FORSØK 1:
alder = int(input("Alder: "))
ruset = input("Er kunden beruset? (J/N) ")
um = input("Er kunden umyndiggjort? (J/N) ")
if alder >= 18 or ruset == "N" or um == "N":
    print("Kunden har lov til å kjøpe vin")
  
# FORSØK 2:
alder = int(input("Alder: "))
ruset = input("Er kunden beruset? (J/N) ")
um = input("Er kunden umyndiggjort? (J/N) ")
if alder >= 18 and not ruset == "J" or um == "J":
    print("Kunden har lov til å kjøpe vin")


# Forsøk 1 feiler her fordi man har brukt `or` der man skulle brukt `and`. Alle de tre betingelsene må være tilfredsstilt, siden Polet ikke selger vin til noen som er synlig ruset, eller som man vet er umyndiggjort. En korrekt løsning ville være:

# In[ ]:


# KORREKT LØSNING, VARIANT 1:
alder = int(input("Alder: "))
ruset = input("Er kunden beruset? (J/N) ")
um = input("Er kunden umyndiggjort? (J/N) ")
if alder >= 18 and ruset == "N" and um == "N":
    print("Kunden har lov til å kjøpe vin")


# Forsøk 2 feiler fordi `or` har lavere presedens enn `not` og `and`. Python vil derfor først sjekke betingelsen `alder >= 18 and not ruset=="J"`, deretter vil den sette hele dette sammen med `or um == "J"`. Dette vil føre til at en person som er umyndiggjort vil få lov til å kjøpe vin uansett, også om man er under 18 og ruset. For at denne betingelsen skal evalueres korrekt må man sette parentes rundt de to betingelsene som har `or` mellom seg som vist nedenfor. Da vil disse to bli sammenholdt først, og begge disse vil bli berørt av det foregående `not`, altså at man **ikke** må være umyndiggjort.

# In[ ]:


# KORREKT LØSNING, VARIANT 2:
alder = int(input("Alder: "))
ruset = input("Er kunden beruset? (J/N) ")
um = input("Er kunden umyndiggjort? (J/N) ")
if alder >= 18 and not (ruset == "J" or um == "J"):
    print("Kunden har lov til å kjøpe vin")


# VARIANT 1 og 2 gir eksakt samme resultat - det vil ofte være flere mulige måter å skrive sammensatte betingelser på. I dette tilfellet kan man vel si at Variant 1 er å foretrekke, siden den slipper å bruke `not` og parentes, og dermed blir litt lettere å lese.

# ## c) Feil i rekkefølge på if-elif-setninger.

# Nedenfor er en ny variant av promilleprogrammet. For kjappere testing ser vi nå bort fra spørsmålene om det var motorvogn, om vedkommende førte kjøretøyet, og eventuell nødrett - dvs. vi antar at alt dette i boks fra før, og spørsmål dermed bare er størrelse på promillen og resulterende straff.
# 
# Kjør programmet nedenfor et par ganger med ulike verdier, f.eks. med promille 0.1 deretter 0.3 deretter 0.9.
# 
# Som du vil se, vil man aldri få større forelegg enn 6000,- med dette programmet, uansett hvor høy promillen var. Hvis promillen var over 0.4, f.eks. 0.45, skulle man hatt 10000,- i forelegg, og med promille høyere enn 0.5 skulle man hatt bot basert på månedslønn, samt fengselsstraff.
# 
# ***Korriger programmet*** så det gjør riktige beslutninger på straffenivå for alle mulige verdier av promille.

# In[4]:


prom = float(input("Hvor stor var promillen? "))
if prom > 0.5:
    print("Bot: en halv brutto månedslønn, samt fengsel.")
elif prom > 0.4:
    print("Forelegg: 10000,-")
elif prom > 0.2:
    print("Forelegg: 6000,-")
else:
    print("Ikke straffbart, ingen bot.")


# #### Rekkefølge if-elif-setninger (hint oppgave c)

# Ved bruk av if-elif-else er det avgjørende at betingelsene kommer i riktig rekkefølge. I Eksempel 1 under skal vi regne ut karakter fra poengscore på en eksamen (hvor toppscore er 100 og blank besvarelse gir 0 poeng). På grunn av feil rekkefølge på testene vil programmet ikke funke som det skal. Problemet er at den første testen, `score >= 0`, vil slå til for absolutt alle eksamenskandidater - og de andre betingelse etter `elif` vil dermed aldri bli evaluert. Alle kandidatene ender da med F.

# In[ ]:


# EKSEMPEL 1 (HVOR VI MED VILJE HAR GJORT FEIL)
score = int(input("Antall poeng: "))
  
if score >= 0:
    karakter = "F"
elif score >= 41:
    karakter = "E"
elif score >= 53:
    karakter = "D"
elif score >= 65:
    karakter = "C"
elif score >= 77:
    karakter = "B"
elif score >= 89:
    karakter = "A"
  
print("Du fikk", karakter)


# Setter vi derimot testene motsatt rekkefølge, som i Eks 2, vil det funke. Generelt er det viktig å sørge for at alle alternativene i en if-elif-else kan nås gitt en passende verdi. Her vil studenter med `score >= 89` få A mens de med lavere score vil bli fordelt videre nedover i if-elif-strukturen.

# In[ ]:


# EKSEMPEL 2 (MED KORRIGERT REKKEFØLGE)
score = int(input("Antall poeng: "))
   
if score >= 89:
    karakter = "A"
elif score >= 77:
    karakter = "B"
elif score >= 65:
    karakter = "C"
elif score >= 53:
    karakter = "D"
elif score >= 41:
    karakter = "E"
else:
    karakter = "F"
  
print("Du fikk", karakter)


# ## d) Feil i valg av overordnet struktur på if-setninger.

# I den neste kodesnutten ser vi på et relatert problem, nemlig hvor lenge førerkortet skal inndras. Alt i alt er reglene som følger:
# - Førerkort skal inndras på livstid dersom det er gjentatt promillekjøring (dømt for det også tidligere), eller hvis man slo seg vrang og nektet og samarbeide ved legetesten, og dette skjer mindre enn 5 år etter en tidligere dom for promillekjøring. (Dvs., hvis man slår seg vrang ved legetesten, kan man få inndratt førerkortet selv om blodprøven deretter viser at promillen var under 0.2.)
# - For personer som **ikke** er tidligere dømt for promillekjøring, gjelder følgende:
#   - Hvis promillen var over 1.2, inndras førerkort for minst 2 år. Inndragelse for 2 år gis også hvis man slår seg vrang under legetesten - da uavhengig av hva promillen var.
#   - Promille i området 0.8-1.2 gir inndragning i 20-22 måneder.
#   - Promille 0.5-0.8 gir vanligvis 18 måneder.
#   - Promille 0.2-0.5 gir inntil 1 års inndragelse.
# 
# Koden under skulle implementere disse reglene, men gjør feil i noen tilfeller. 
# 
# - Hvis det svares "j" på "Tidligere dømt..." sier programmet at førerkort skal inndras på livstid uansett hva det svares på de andre spørsmålene, dvs. også om promille var 0 og man oppførte seg pent ved legetesten.
# - Med f.eks. 1.4 eller 0.9 for promille (og "n" på tidligere dømt, "n" på nektet å samarbeide) vil programmet først skrive ut korrekt straffereaksjon, men vil deretter fortsette med å skrive ut også mildere straffereaksjoner. 
# 
# ***Rett disse feilene så programmet gir riktig konklusjon på straffereaksjonen for alle mulige kombinasjoner av input-verdier.***

# In[8]:


# leser inn data
prom = float(input("Hvor stor var promillen? "))
nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
if tidl == "j":
    aar = int(input("Antall år siden siste domfellelse: "))
else:
    aar = 999
  
# vurderer inndragning av førerkort
if tidl == "j" or nekt == "j" and aar < 5:
    print("Førerkort inndras for alltid.")
elif prom > 1.2 or nekt == "j":
    print("Førerkort inndras minst 2 år.")
elif prom > 0.8:
    print("Førerkort inndras 20-22 mnd.")
elif prom > 0.5:
    print("Førerkort inndras vanligvis 18 mnd.")
elif prom > 0.2:
    print("Førerkort inndras inntil 1 år.")
else:
    print("Ingen inndragning av førerkort.")


# #### Feil valg av struktur for if-setninger (hint til oppg d)

# Ofte skal vi ikke treffe bare én beslutning men flere forskjellige beslutninger i samme program. Dette tilsier bruk av flere if-setninger, og det er viktig å finne fram til en korrekt struktur for if-setningene. Her skal vi se på forskjellen mellom tre ulike situasjoner:
# 
# 1. beslutning med alternative handlinger som er gjensidig utelukkende: Bruk **if-else** (hvis 2 alternativer) eller **if-elif-else** (hvis 3 eller flere alternativer). 
# 2. flere beslutninger som er uavhengige av hverandre: **Bruk frittstående if-setninger**
# 3. beslutninger som er avhengig av andre beslutninger, dvs. bare relevant å vurdere gitt et visst utfall av en tidligere beslutning: Kan løses ved **nøstede if-setninger**.
# 
# Hvis man velger feil struktur på if-setningene, vil man få programmer som tar feil beslutninger.

# **Eksempel 1: Gjensidig utelukkende alternativer:**
# 
# Omregning fra poengscore til karakter på en eksamen er eksempel på en beslutning med diverse gjensidig utelukkende konklusjoner - det skal gis A, B, C, D, E eller F ut fra poeng. Som vist i hint før oppgave c, løses dette typisk med en if-elif-struktur. Om man i stedet velger frittstående if-setninger, vil dette bli feil:

# In[ ]:


# EKSEMPEL HVOR VI MED VILJE HAR GJORT FEIL
score = int(input("Antall poeng: "))
   
if score >= 89:
    karakter = "A"
if score >= 77:
    karakter = "B"
if score >= 65:
    karakter = "C"
if score >= 53:
    karakter = "D"
if score >= 41:
    karakter = "E"
else:
    karakter = "F"
  
print("Du fikk", karakter)


# Studenter med høy poengscore, f.eks. tilsvarende A eller B, vil i første omgang få tilordnet en riktig verdi for karakter ved at den tilsvarende if-setningen slår til. MEN: Siden hver setning begynner med `if`, er den uavhengig av forrige if-setning, så alle disse blir utført uavhengig av utfallet av forrige if-setning. Alle med høy score, vil jo også ha nok poeng til en dårligere karakter. Til slutt vil derfor alle studenter enten ende opp med E (hvis >=41 poeng) eller F (hvis < 41 poeng). Korreksjonen her er å bytte ut alle `if` unntatt den øverste med `elif` da blir alle de påfølgende testene kun utført hvis foregående tester har feilet, så en student som allerede har fått A vil ikke få denne overskrevet av en dårligere karakter.
# 
# (Eksemplet kunne ha funket med frittstående if-setninger hvis testene inneholdt både øvre og nedre grense for score, f.eks. `89 > score >= 77` for B, `77 > score >= 65` for C, osv. Dette ville imidlertid ha vært en klart dårligere løsning enn if-elif-... både fordi betingelsene blir mer kompliserte å skrive, og fordi programmet kaster bort tid med å evaluere ekstra if-setninger hvis en av de tidlige betingelsene har slått til. En if-elif...-elif-else-struktur er vanligvis lettere å forstå fordi den klart får fram at det dreier seg om gjensidig ekskluderende alternativ.)

# **Eksempel 2: To uavhengige beslutninger**
# 
# Det neste eksemplet viser derimot et tilfelle hvor det er riktig å bruke frittstående if-setninger. Skal vi ta paraply eller ikke? Skal vi ta brodder eller ikke? Dette er to uavhengige beslutninger, den ene avhenger av regn, den andre om det er glatt. Hadde vi i stedet brukt if-elif her, ville programmet ikke ha virket som det skulle, da det kun ville ha vært i stand til å anbefale brodder i oppholdsvær (mens det jo kan være minst like glatt om det regner).

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
glatt = int(input("Hvor glatt er det, fra 0 (ikke) til 10 (blank is)? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply.")
if glatt > 8:
    print("Da anbefaler jeg sko med brodder eller pigger.")


# Hvis vi her hadde skrevet `elif glatt > 8:` ville programmet kun ha vært i stand til å anbefale brodder hvis det ikke regnet, mens isen jo vil være minst like glatt hvis den i tillegg er våt.
# 
# Et tvilstilfelle på hvilken struktur man bør velge, inntreffer hvis man har beslutninger som er delvis avhengige av hverandre, men også delvis uavhengige. La oss si at kriteriet for brodder var enten `glatt > 8` eller hvis det regner, `glatt > 7` (fordi man antar at det da vil kunne bli glattere underveis på spaserturen fordi isen blir våtere). Nedenstående viser to mulige løsninger på dette:

# In[ ]:


# ALTERNATIV 1: frittstående if-setninger
regn = float(input("Hvor mange mm regn er det meldt? "))
glatt = int(input("Hvor glatt er det, fra 0 (ikke) til 10 (blank is)? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply.")
if glatt > 8 or regn > 0.2 and glatt > 7:
    print("Da anbefaler jeg sko med brodder eller pigger.")
  
# ALTERNATIV 2: nøstede if-setninger
regn = float(input("Hvor mange mm regn er det meldt? "))
glatt = int(input("Hvor glatt er det, fra 0 (ikke) til 10 (blank is)? "))
if regn > 0.2:
    print("Da anbefaler jeg paraply.")
    if glatt > 7:
        print("Da anbefaler jeg sko med brodder eller pigger.")
elif glatt > 8:
    print("Da anbefaler jeg sko med brodder eller pigger.")


# Her vil begge alternativer funke, hver har sine fordeler og ulemper. Ulempen med alt. 1 er at den gjentar betingelsen `regn > 0.2` to steder, som dermed tilsier at den også må evalueres to ganger i enkelte kjøringer av programmet. Forskjellen dette innebærer i tidsforbruk er imidlertid marginal. Ulempen med alternativ 2 er derimot at print-setningen om brodder forekommer to steder... det blir dermed litt vanskeligere å forstå programmet, mens det i alt. 1 fremgår klarere eksakt hvilken kombinasjon av betingelser som utløser hver konsekvens.
# 
# I andre tilfeller kan en beslutning være avhengig av en annen, f.eks. kun være aktuell ved et visst utfall av en foregående if-setning:

# In[ ]:


regn = float(input("Hvor mange mm regn er det meldt? "))
vind = float(input("Hvor mange m/s vind er det meldt? "))
if regn > 0.2:
    if vind < 7.0:
        print("Da anbefaler jeg paraply.")
    else:
        print("Anbefaler regntøy, for mye vind for paraply.")


# Her ville if `regn > 0.2: .....elif vind < 7.0` ha blitt feil. Programmet ville da ha gjort vurderinger av vinden kun hvis det ikke regnet, og dermed ha vært ute av stand til å fraråde paraply hvis det regner og samtidig blåser kraftig.
# 
# Oppsummert:
# 
# - flere helt uavhengige beslutninger: bruk frittstående if-setninger
# - beslutning med gjensidig utelukkende handlingsalternativer: bruk if-else (2 alternativer) eller if-elif-else (3 eller flere alternativer)
# - beslutninger relatert på annen måte, f.eks. at en betingelse (som `vind < 7.0 ovenfor`) kun er aktuell gitt et visst utfall av en annen betingelse: kan løses ved å nøste flere if-setninger inni hverandre

# ## e) FRIVILLIG EKSTRAOPPGAVE

# Det er ikke nødvendig å gjøre denne for å få godkjent deloppgaven "Forbrytelse og straff". ***Ta utgangspunkt i nedenstående kode med input-setninger. Bruk deretter det du har laget i tidligere deloppgaver a-d for å sette sammen et komplett program som både gir riktig konklusjon på bot og på inndragelse av førerkort***. Husk som nevnt tidligere at det er mulig å få inndratt førerkortet selv i tilfeller hvor man ikke får noen bot for promillekjøring, nemlig hvis man slår seg vrang i forbindelse med legetesten.

# In[ ]:


# leser inn data
prom = float(input("Hvor stor var promillen? "))
motor = input("Var farkosten en motorvogn? (j/n) ")
f = input("Var personen fører av vognen? (j/n) ")
leds = input("Var personen ledsager ved øvekjøring? (j/n) ")
n = input("Var det nødrett? (j/n) ")
nekt = input("Nektet å samarbeide ved legetest? (j/n) ")
tidl = input("Tidligere dømt for promillekjøring? (j/n) ")
if tidl == "j":
    aar = int(input("Antall år siden siste domfellelse: "))
  
# legg til din kode nedenfor her:

