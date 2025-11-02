import streamlit as st
import pandas as pd

def mostrar_venta():
    # Menú de navegación
    opcion = st.selectbox("Selecciona una opción:", ["Inicio", "Ventas", "Inventario"])

    # Datos simulados de ventas
    ventas_data = pd.DataFrame({
        'Producto': ['Café', 'Pan', 'Leche', 'Azúcar'],
        'Cantidad': [10, 5, 8, 3],
        'Fecha': ['2025-11-01', '2025-11-01', '2025-11-02', '2025-11-02']
    })

    # Mostrar tabla si se selecciona "Ventas"
    if opcion == "Ventas":
        st.subheader("Tabla de Ventas")
        st.dataframe(ventas_data)
