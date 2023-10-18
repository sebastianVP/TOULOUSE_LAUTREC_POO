def main():
    try:
      msg="Dime el valor de X:"
      x= get_int(msg)
    except:
        print("Ingresa o declara el msg para evitar el error")
    print(f"El valor de x es: {x}")
              
def get_int(msg):
    while True:
        try: 
            return int(input(msg))
        except ValueError:
            pass

main()
