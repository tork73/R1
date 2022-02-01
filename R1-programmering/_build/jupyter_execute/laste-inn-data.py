#!/usr/bin/env python
# coding: utf-8

# # Vi laster inn data fra internett
# 
# Vi kan finne datafiler lagt ut på nettet. Disse kan vi laste inn i Python på en elegant måte ved å bruke pandas. Vi viser ved hjelp av en del eksempler. 

# ### Eksempel 1
# 
# Filen https://vincentarelbundock.github.io/Rdatasets/csv/quantreg/gasprice.csv innhol- der tidsserie for ukentlige bensinpriser i USA i perioden 1990:8-2003:26
# 
# a) Lag en grafisk framstilling av hele tidsserien.
# 
# b) Lag en grafiske gramstilling der du kun ser på årene 2000-2003.
# 
# #### Løsning:

# In[1]:


import pandas as pd             # For å lese og behandle CSV-filer
import matplotlib.pyplot as plt # For plotting

url = "https://vincentarelbundock.github.io/Rdatasets/csv/quantreg/gasprice.csv"
# Vi leser inn data fra URLen og lagrer det i en dataframe som vi kaller df:
df = pd.read_csv(url, index_col=0)
df


# Vi kan nå plotte disse tallene ved å bruke time på x-aksen og value på y-aksen. Dette kan gjøres ved å bruke plt.plot(). Vi kan også bruke en egen plotte-metode på datarammen df som pandas gir oss. Vi viser begge metodene. 

# In[2]:


# Metode 1

x = df["time"] # x er en liste med datoer
y = df["value"] # y er en liste med priser

plt.plot(x, y)
plt.xlabel("Dato")
plt.ylabel("Pris")
plt.show()


# In[3]:


# Metode 2

df.plot("time", "value")
plt.xlabel("Dato")
plt.ylabel("Pris")
plt.show()


# Vi kan finne gjennomsnittsprisen for disse årene ved å bruke pandas mean-metode på datarammen. 
# 

# In[4]:


df["value"].mean()


# Vi kunne også funnet gjennomsnittsprisen for årene 2000-2003:

# In[5]:


# Vi lager en ny dataramme som kun har med de rader vi ønsker å behandle:
D = df[df["time"]>=2000]
D


# In[6]:


D["value"].mean()


# Vi ser at gjennomsnittsprisen i perioden 2000-2003 er 141.87 dollar. 

# ### Eksempel 2
# 
# Filen https://vincentarelbundock.github.io/Rdatasets/csv/datasets/nottem.csv har data fra Nottingham slott. Den har to kolonner. Den første er tiden (i år) og den andre er temperaturen målt i Fahrenheit. 
# 
# Vi ønsker å plotte temperaturen målt i grader Celsius som funksjon av tiden. 
# 
# Vi bruker da følgende formel for å regne om fra Fahrenheit til Celsius:
# $$ C = \frac{5\cdot (F-32)}{9}$$
# 

# In[7]:


import pandas as pd
import matplotlib.pyplot as plt

# Vi lager en dataramme med tallene fra filen:
url = "https://vincentarelbundock.github.io/Rdatasets/csv/datasets/nottem.csv"
df = pd.read_csv(url, index_col=0)
df


# In[8]:


# Vi legger til kolonnen med temperaturen i Celsius. 

df["temperatur"] = 5*(df["value"]- 32)/9
df


# In[9]:


plt.style.use("seaborn")
df.plot(x="time", y="temperatur", figsize=(10,5))
plt.xlabel("År")
plt.show()


# ### Oppgave
# 
# Hva var gjennomsnittstemperaturen i denne perioden? 

# ### Eksempel 3
# 
# På nettsiden seklima.met.no kan du laste ned klima-data for ulike målestasjoner. I dette eksempelet skal vi se på hvor kraftig det blåste i vindkastene i tidsrommet 26.-31. januar 2022. 
# 
# ![vind-stord](vindkast-stord.png)
# 
# Når vi har gjort de ulike valgene for hvilke data vi vil laste ned, så klikker vi på «Last ned» nederst til venstre på nettsiden. Velg csv-fil. Denne blir da lastet ned i din nedlastningsmappe (litt avhengig av nettleser og innstillinger). Pass på å ikke åpne denne filen med Excel. Dra så filen over i mappen som selve jupyter-filen din er lagret i. 
# 
# ![vindkst-last-ned](last-ned1.png)
# 
# Vi kan nå importere denne filen inn i Python, plotte og gjøre beregninger. 
# 
# Når vi laster inn denne filen, får vi et par problemer. Vi må for det første spesifisere at verdiene skilles ved hjelp av semikolon. Dette gjør vi ved å skrive inn sep=";". Så får vi et lite problem ved at desimaltallene er gitt med komma, ikke punktum (som er standard i Python). Dette løser vi ved å skrive decimal=",". 

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("table.csv", sep=";", decimal=",")
df


# Vi ønsker nå å finne ut når vi hadde det høyeste vindkastet. 

# In[11]:


m = df["Høyeste vindkast (10 min)"].max()
m


# In[12]:


for i in range(859):
    if df["Høyeste vindkast (10 min)"][i] == m:
        print(df["Tid(norsk normaltid)"][i])


# Vi må selvsagt også plotte dataene våre:

# In[13]:


df.plot(x="Tid(norsk normaltid)", y="Høyeste vindkast (10 min)", figsize=(12,5))
plt.show()


# In[ ]:




