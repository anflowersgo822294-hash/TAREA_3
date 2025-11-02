import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login
from modulos.productos import mostrar_productos
from modulos.inicio import mostrar_inicio

# Verificar si la sesión está iniciada
if st.session_state.get("sesion_iniciada", False):
    # Menú lateral
    seleccion = st.sidebar.selectbox("Selecciona una opción", ["Inicio", "Ventas", "Productos"])

    # Mostrar contenido según la opción seleccionada
    if seleccion == "Inicio":
        mostrar_inicio()
    elif seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
else:
    # Mostrar pantalla de login si no hay sesión activa
    login()
