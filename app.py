import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login
from modulos.productos import mostrar_productos
from modulos.inicio import mostrar_inicio

def mostrar_menu():
    nombre = st.session_state.get("nombre_cliente", "Cliente")
    st.sidebar.markdown(f"👤 **Bienvenido, {nombre}**")

    seleccion = st.sidebar.selectbox("Selecciona una opción", ["Inicio", "Ventas", "Productos"])

    if seleccion == "Inicio":
        mostrar_inicio()
    elif seleccion == "Ventas":
        mostrar_venta()
    elif seleccion == "Productos":
        mostrar_productos()

if st.session_state.get("sesion_iniciada", False):
    mostrar_menu()
else:
    login()
