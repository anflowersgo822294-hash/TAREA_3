import streamlit as st
import pandas as pd

def mostrar_productos():
    # Lista de productos simulada
    productos = [
        {"ID": 1, "Nombre": "Shampoo Herbal", "Precio": 4.50, "Stock": 120},
        {"ID": 2, "Nombre": "Acondicionador Natural", "Precio": 5.25, "Stock": 80},
        {"ID": 3, "Nombre": "Jabón Artesanal", "Precio": 3.75, "Stock": 150},
        {"ID": 4, "Nombre": "Aceite Esencial Lavanda", "Precio": 6.00, "Stock": 60},
    ]

    # Crear DataFrame
    df_productos = pd.DataFrame(productos)

    # Mostrar en Streamlit
    st.title("📦 Listado de Productos")
    st.write("Consulta rápida de productos disponibles en inventario:")
    st.dataframe(df_productos, use_container_width=True)
