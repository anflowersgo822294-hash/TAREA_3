# modulos/productos.py
import streamlit as st
import pandas as pd

def mostrar_productos():
    productos = [
        {"ID": 1, "Nombre": "Shampoo Herbal", "Precio": 4.50, "Stock": 120},
        {"ID": 2, "Nombre": "Acondicionador Natural", "Precio": 5.25, "Stock": 80},
        {"ID": 3, "Nombre": "Jabón Artesanal", "Precio": 3.75, "Stock": 150},
        {"ID": 4, "Nombre": "Aceite Esencial Lavanda", "Precio": 6.00, "Stock": 60},
    ]
    df_productos = pd.DataFrame(productos)
    st.title("Listado de Productos")
    st.dataframe(df_productos, use_container_width=True)
