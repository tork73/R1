#!/usr/bin/env python
# coding: utf-8

# # Installasjon av Python
# 
# Vi anbefaler å laste ned Anaconda på din datamaskin. Med Anaconda får du det meste av det du trenger for å programmere. 
# 
# Du finner Anaconda her: https://www.anaconda.com/products/individual 
# 
# ![anaconda](anaconda.png)
# 
# Når du har installert Anaconda kan du åpne Anaconda navigator. Der finner du en rekke program som kan brukes. Noen liker å bruke Spyder, andre liker å bruke Jypyter lab. Vi vil i R1 bruke sistnevnte. 
# 
# Når du starter Jupyter lab vil du få mulighet til å lagen en ny «Notebook». Før du klikker på denne (3), er det lurt å bla seg gjennom til den mappen du ønsker å lagre notebook-en. (2). Det gjør du ved å først klikke på mappen øverst i margen til venstre (1). 
# 
# ![mappe](mapper-jupyter.png)

# Når du så har åpnet en slik notebook, er du klar til å programmere. I Jupyter lab fungerer det slik at du skriver inn koden i ulike celler. Disse kan du så «kjøre». Det vil si at du kan be Python lese koden. Output (resultatet av kjøringen) vil da komme fram like nedenfor cellen:

# In[1]:


a = 1
b = 2
c = a+b
print(c)


# I cellen over har vi laget et veldig enkelt program. Det første som skjer er at det blir laget tre variabler, a, b og c. Variabelen c er summen av a og b. På den fjerde linjen skriver vi ut verdien til c på skjermen. Trykker vi på «play»-knappen (eller shift-enter) vil koden fra cellen blir kjørt og du får resultatet nedenfor cellen. 

# Det fine med Jupyter lab er at du ikke trenger å lagre underveis. Det skjer automatisk. Men det kan være en god idé å endre navnet til jupyter-filen til noe som er mer dekkende for det du gjør i notebook-en. 
# 
# Du kan endre navn ved å høyreklikke på filnavnet i margen til venstre. 

# 
