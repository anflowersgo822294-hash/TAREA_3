import streamlit as st
import pandas as pd

def mostrar_venta():
    # Lista simulada de ventas
    ventas = [
        {"Producto": "Shampoo Herbal", "Cantidad": 3, "Fecha": "2025-11-01"},
        {"Producto": "Acondicionador Natural", "Cantidad": 2, "Fecha": "2025-11-01"},
        {"Producto": "Jabón Artesanal", "Cantidad": 5, "Fecha": "2025-11-02"},
        {"Producto": "Aceite Esencial Lavanda", "Cantidad": 1, "Fecha": "2025-11-03"},
    ]

    # Crear DataFrame
    df_ventas = pd.DataFrame(ventas)

    # Mostrar en Streamlit
    st.title("🧾 Registro de Ventas")
    st.write("Consulta de productos vendidos con cantidad y fecha:")
    st.dataframe(df_ventas, use_container_width=True)
