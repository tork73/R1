#!/usr/bin/env python
# coding: utf-8

# # Dataserier og datarammer
# 
# Store og små datamengder blir lagret i filer av ulik type. Den mest vanlige filtypen er såkalte csv-filer. Bokstavene csv står for «comma separated values». Skal vi for eksempel laste ned temperaturen gjennom et døgn fra en værstasjon, vil vi ofte få en slik fil. 
# 
# For å laste inn slike filer kan vi bruke en modul som heter pandas. Med denne modulen får vi tilgang på en rekke nye funksjoner og objekter. Vi importerer pandas slik: 

# In[1]:


import pandas as pd


# Tidligere har vi jobbet med lister og arrayer i Python. Pandas gir oss tilgang på to nye objekter, nemlig dataserier og datarammer. 
# 
# ```{admonition} Dataserier og datarammer
# En dataserie er en 1-dimensjonal array med verier og en indeks
# 
# En dataramme er en 2-dimensjonal array med både rad- og kolonneindeks.
# ```
# 

# ### Eksempel 1
# 
# Vi ønsker å lage en overisk over hva som er til middag i kantinen de ulike ukedagene. Vi kan da lage en dataserie på følgende måte:

# In[2]:


import pandas as pd

S = pd.Series(["Taco", "Kylling", "Laks", "Pizza", "Pasta"])
S


# Vi ser at vi får listet opp de ulike rettene i rekkefølgen vi skrev dem opp på. Tallene 0, 1, 2, 3, 4 er indeksene. Disse kan vi bruke til å hente ut data fra dataserien. Ønsker vi for eksempel å se hva som var til middag på torsdage, kan vi se hva som står på plass3:

# In[3]:


S[3]


# Vi kan også bytte ut indeksen med for eksempel ukedagene:

# In[4]:


S.index = ["Mandag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
S


# Vi kan også legge til en rad. Vil vi legge til hva som var til middag på lørdagen, skriver vi:

# In[5]:


S["Lørdag"] = "Grøt"
S


# Dersom vi ønsker å legge til kolonner, an vi gjøre dette. Men da må vi bruke datarammer. 

# In[6]:


# Vi kaller datarammen for df og gir første kolonne navnet "Rett":
df = pd.DataFrame(S, columns=["Rett"]) 
df


# Dersom vi nå vil legge til prisen per rett, legger vil en kolonne med de ulike prisene:

# In[7]:


df["Pris"]  = [59, 65, 70, 85, 75, 55]
df


# Ønsker vi å utvide kolonnen med antall retter som ble solgt de ulike dagene og hva inntekten ble de ulike dagene, kan vi gjøre det slik:

# In[8]:


# Lager først en kolonne med antallet:
df["Antall"] = [32, 21, 35, 22, 67, 66]

# Så lager vi en kolonne som gir pris $\cdot $ antall:


# In[9]:


df["Inntekt"] = df["Pris"] * df["Antall"]
df


# Til slutt kan vi summere opp tallene i den siste kolonnen. Det kan vi gjøre ved å bruke sum-metoden på kolonnen:

# In[10]:


df["Inntekt"].sum()


# ### Oppgave
# 
# Per, Anders og Line eier en hytte sammen.
# 
# De skal betale utgiftene til strøm i forhold til hvor mange kilowattimer (kWh) hver av dem bruker. De leser av målerstanden hver gang de kommer til hytta og hver gang de reiser fra hytta. På den måten finner de ut hvor mange kWh hver av dem har brukt.
# 
# Første halvår 2021 ble forbruket slik (tall i kWh):
# 
# | Navn   | Målestand ankomst | Målestand avreise | Strømforbruk | Å betale |
# |--------|------------------:|------------------:|--------------|----------|
# | Per    | 12759             | 127788            |              |             |
# | Line   | 127788            | 128129            |              |             |
# | Anders | 128129            | 128612            |              |             |
# | Line   | 128612            | 129578            |              |             |
# 
# Gå ut fra at prisen på 1 kWh er 0,78 øre. 
# 
# Lag en dataramme som regner ut hvor mye hver av dem må betale. 
# 
