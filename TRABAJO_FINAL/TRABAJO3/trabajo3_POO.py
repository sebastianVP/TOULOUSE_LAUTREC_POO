'''
TRABAJO 3: Grabado de pantalla con python

DESARROLLO:

1. UTILIZAR LAS LIBRERIAS: pyautogui,cv2(opencv-python),numpy
2. DECLARAR UNA CLASE, por ejemplo MyApp()
3. DEFINIR LOS METODOS:
    - Declarar e ingresar el Nombre de video, resolucion,codificacion de video,tasa de frame.
    - Declarar metodo de configuracion.
    - Declarar metodo de grabado.
    - Declarar metodo de cierre.
    - El programa debe grabar un archivo con el nombre especificado.
'''

# Librerias y paquetes a utilizar
import pyautogui
import cv2
import numpy as np
 
# Resolucion del video a grabar
resolution = (1920, 1080)
 
# Especificar el tipo de video -> *"XVID"
codec = cv2.VideoWriter_fourcc(*"XVID")
 
# Definir el nombre del archivo termina con .avi
filename = "Recording.avi"

# Definir la tasa de frames. Podemos escoger 
# cualquier valor y experimentar con el.
fps = 60.0
 
 # CONFIGURACION, CREANDO EL OBJETO VideoWriter
out = cv2.VideoWriter(filename, codec, fps, resolution)
 
# Creacion de una ventana Vacia.
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
 
# Redimensionando la pantalla
cv2.resizeWindow("Live", 480, 270)
 
# Operacion de grabado, al presionar la tecla q se interrumpe y finaliza
while True:
    # Tomar imagen usando pyautogui
    img = pyautogui.screenshot()
 
    # Convirtiendo la imagen en un arreglo
    frame = np.array(img)
 
    # Conversion desde  BGR(Blue, Green, Red) hacia
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
 
    # Escribiendolo en un archivo de salida
    out.write(frame)
     
    # OPTION: Mostrar la ventana en vivo.
    cv2.imshow('Live', frame)
     
    # Detener el grabado al oprimir la letra q
    if cv2.waitKey(1) == ord('q'):
        break
 
# Liberar el VideoWriter
out.release()
 
# Cerrado de ventanas(Destruccion de la ventana)
cv2.destroyAllWindows()
'''
RECOMENDACION  FINAL:
- EL TRABAJO CONSISTE EN DECLARAR UNA CLASE Y CREAR LOS METODOS 
  UTILIZANDO LAS LINEAS DE CODIGO DESCRITAS SIGUIENDO EL ESQUEMA 
  MOSTRADO EN ejemplo.py 
'''