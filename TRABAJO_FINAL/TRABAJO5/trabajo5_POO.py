'''
TRABAJO 5: Generador y lector de QR

DESARROLLO:

1. UTILIZAR LAS LIBRERIAS: qrcode,cv2(opencv-python)
2. DECLARAR UNA CLASE, por ejemplo MyApp()
3. DEFINIR LOS METODOS:
    - Ingresar o declarar el mensaje data.
    - Ingresar los atributos de configuracion de la libreria QRCode
    - Definir metodo para generar QR
    - Grabado de imagen QR con un nombre definido como atributo previo.
    - La decodificacion se realiza utilizando la libreria cv2
    - Metodo de lectura del archivo generado QR
    - Metodo de deteccion y decodificacion del codigo QR
    - Metodo para mostrar mensaje decodificado.
'''
'''
import qrcode
'''
import qrcode

data= 'Trabajo 5, POO con Python'



# DEFINIR ATRIBUTOS DE TAMAÑO box_size
qr=qrcode.QRCode(version=1,box_size=10,border=5)
# DEFINIR MENSAJE DEL QR ESTABLECIDO EN DATA
qr.add_data(data)
qr.make(fit=True)
# GENERAR EL QR 
img=qr.make_image(fill_color='red',back_color='white')
# GRABAR LA IMAGEN CON UN NOMBRE DEFINIDO
img.save("check.png")

# LECTURA Y DECODIFICACION DE LA IMAGEN CON CODIGO QR
# SE UTILIZA EN ESTA PARTE LA LIBRERIA CV2
import cv2
# LECTURA DEL ARCHIVO GENERADO EN LA PRIMERA PARTE
img = cv2.imread("check.png")
# DETECCION DEL CODIGO QR
det = cv2.QRCodeDetector()
# DECODIFICACION DEL CODIGO QR
valorQRLeido,pts,st_code= det.detectAndDecode(img)
#MOSTRAR MENSAJE DEL CODIGO QR
print(valorQRLeido)
'''
RECOMENDACION  FINAL:
- EL TRABAJO CONSISTE EN DECLARAR UNA CLASE Y CREAR LOS METODOS 
  UTILIZANDO LAS LINEAS DE CODIGO DESCRITAS SIGUIENDO EL ESQUEMA 
  MOSTRADO EN ejemplo.py 
'''