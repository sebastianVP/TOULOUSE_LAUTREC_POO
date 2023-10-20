'''
TRABAJO 4: Grabador de voz

DESARROLLO:

1. UTILIZAR LAS LIBRERIAS: sounddevice,scipy,wavio
2. DECLARAR UNA CLASE, por ejemplo MyApp()
3. DEFINIR LOS METODOS:
    - Ingresa y declara frecuencia de muestreo y duracion de grabado de voz.
    - Metodo de grabado de voz y tiempo de grabado.
    - Generar archivo de audio con un nombre definido utilizando la libreria wavio

'''
# Importar las librerias requeridas.
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
# Atributo de entrada frecuencia de muestreo
freq = 44100
 
# Atributo de entrada duracion de grabado
duration = 5
 
# Iniciar el grabado con los atributos definidos
# Duracion y frecuencia de muestreo
# grabado y linea wait seguida para indicar el tiempo.
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
 
#  Grabado de audio durante el tiempo establecido
sd.wait()
 

# Este comando convertira el arreglo de tipo numpy en un
# archivo de audio con la frecuencia de muestreo definida
write("recording0.wav", freq, recording)
 
# Podemos emplear la libreria wavio para grabar tambien el archivo de audio
wv.write("recording1.wav", recording, freq, sampwidth=2)
# utilizar una de las dos lineas(36 o 39) para genear el grabado de archivo de audio.

'''
RECOMENDACION  FINAL:
- EL TRABAJO CONSISTE EN DECLARAR UNA CLASE Y CREAR LOS METODOS 
  UTILIZANDO LAS LINEAS DE CODIGO DESCRITAS SIGUIENDO EL ESQUEMA 
  MOSTRADO EN ejemplo.py 
'''