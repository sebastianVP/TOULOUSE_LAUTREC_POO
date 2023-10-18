import streamlit as st
import yfinance as yf
import pandas as pd

# $ python numero10.py
# $ streamlit run numero10.py
#AAPL', 'GOOG' ; 'SPY'
class MyApp():
    def __init__(self, identificador):
        self.identificador = identificador

    def get_data(self):
        tickerData = yf.Ticker(self.identificador)
        self.tickerDF= tickerData.history(period='1d',start="2010-5-31",end="2023-7-1")

    def mostrar_web(self):
        st.write(
            '''
            # SIMPLE STOCK PRICE
            Muestra el precio del stock y el volumen del stock de google
            1- Extraer datos con la libreria yfinance
            2- Pandas, limpiar u ordernar mi data
            3- streamlite hacer mi despliegue


            '''
        )

        st.line_chart(self.tickerDF.Close)
        st.line_chart(self.tickerDF.Volume)


def main():
    identificador=input("Ingresa el identificador de la Empresa:").strip()
    test= MyApp(identificador)
    test.get_data()
    test.mostrar_web()

if __name__=="__main__":
    main()

