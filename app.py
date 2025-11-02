import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login
from modulos.productos import mostrar_productos
from modulos.inicio import mostrar_inicio  # ✅ Importación agregada

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:
    # Mostrar el menú lateral
    opciones = ["Ventas", "Productos", "Inicio"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada, mostramos el contenido correspondiente
    if seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()
    elif seleccion == "Inicio":  # ✅ Corregido: antes decía "inicio"
        mostrar_inicio()
else:
    # Si la sesión no está iniciada, mostrar el login
    login()
