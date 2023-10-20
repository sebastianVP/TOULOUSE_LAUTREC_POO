'''
TRABAJO 1: WEBSCRAPING

DESARROLLO:

1. UTILIZAR LAS LIBRERIAS: requests,bs4
2. DECLARAR UNA CLASE, por ejemplo MyApp()
3. DEFINIR LOS METODOS:
    - Ingresa Nombre de usuario.
    - Mostrar perfil de usuario.
    - Mostrar link de descarga de imagen.
    - 

'''
# DECLARACION DE LIBRERIAS
import requests
from bs4 import BeautifulSoup as bs
# INSTANCIA DE ATRIBUTO DE ENTRADA
# perfil de usuario en github a utilizar 
# no se requiere tener una cuenta en Github pueden buscar cualquier usuario
# ejemplo: https://github.com/samedsay
# nombre de usuario-->samedsay
github_user= input("Ingrese el nombre del usuario:")
url = 'https://github.com/'+github_user
r   = requests.get(url)
print("url:", url)


# Link de descarga de imagen en github
soup = bs(r.content,'html.parser')

profile_image = soup.find('img')['src']
print(profile_image)
#EJEMPLO:
# https://avatars.githubusercontent.com/u/14846293?s=64&v=4


# -------OJO--------
# LES RECOMIENDO EXTRAER O QUITAR LAS LETRAS----> s=64& del link anteterior
#  y solo trabajar con la cadena de texto 
# https://avatars.githubusercontent.com/u/14846293?v=4
# EN EL LINK ANTERIOR LA IMAGEN SE APRECIA MEJOR
profile_image=profile_image.replace('s=64&', '')
print(profile_image)
#profile_image="https://avatars.githubusercontent.com/u/14846293?v=4"
response = requests.get(profile_image)


## GRABADO FINAL DE IMAGE EN FORMATO PNG
imagen = github_user+".png"
open(imagen,"wb").write(response.content)


'''
RECOMENDACION  FINAL:
- EL TRABAJO CONSISTE EN DECLARAR UNA CLASE Y CREAR LOS METODOS 
  UTILIZANDO LAS LINEAS DE CODIGO DESCRITAS SIGUIENDO EL ESQUEMA 
  MOSTRADO EN ejemplo.py 
'''