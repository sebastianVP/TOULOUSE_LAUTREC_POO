'''
TRABAJO 2: Obtencion de Informacion de Clima

DESARROLLO:

1. UTILIZAR LAS LIBRERIAS: requests,pprint
2. DECLARAR UNA CLASE, por ejemplo MyApp()
3. DEFINIR LOS METODOS:
    - Ingresa Ciudad para consultar informacion de clima.
    - Mostrar informacion de clima.
    - Mostrar informacion de.
    - 
'''
#DECLARACION DE LIBERIAS
import requests
from pprint import pprint

# INSTANCIA DE ATRIBUTO DE ENTRADA 
# CIUDAD DE INTERES

city= input('Enter a city:')
# Pueden escribir Lima, London de prueba

#DECLARAR CON AYUDA DEL APIKEY Y DE LA LIBRERIA REQUEST
#el atributo base_url para solicitar la informacion

API_Key='f2e0821b4faa6a5611b43a56fe34752b'

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city
weather_data= requests.get(base_url).json()

# MOSTRAR LA INFORMACION RECIBIDA
pprint(weather_data)
# MOSTRAR LA INFORMACION SIGUIENTE DE LA CIUDAD INGRESADA

temperatura=weather_data['main']['temp']
#ojo para mostrar la temperatura en °C restarle 273
print("City: ",city)
print("Temperatura: ",round(temperatura-273,2))
'''
Mostrar la informacion adicional proporcionada por el dictionary de 
weather -> description
main    -> humidity
main    -> pressure
'''
'''
RECOMENDACION  FINAL:
- EL TRABAJO CONSISTE EN DECLARAR UNA CLASE Y CREAR LOS METODOS 
  UTILIZANDO LAS LINEAS DE CODIGO DESCRITAS SIGUIENDO EL ESQUEMA 
  MOSTRADO EN ejemplo.py 
'''