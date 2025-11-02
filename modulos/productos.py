# app.py
import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login
from modulos.productos import mostrar_productos  # Importación del módulo de productos

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Mostrar el menú lateral
    opciones = ["Ventas", "Productos", "Otra opción"]  # Agregamos "Productos" al menú
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada, mostramos el contenido correspondiente
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")
else:
    # Si la sesión no está iniciada, mostrar el login
    login()
