
#pip install pyshorteners
import pyshorteners


# Agregamos el enlace
link='https://www.lirvan.com'

# Mostramos el enalce acortado
print(pyshorteners.Shortener().clckru.short(link))