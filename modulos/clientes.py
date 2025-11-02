import streamlit as st
from modulos.config.conexion import obtener_conexion
import pandas as pd

def mostrar_clientes():
    st.subheader("📋 Lista de clientes registrados")

    con = obtener_conexion()
    if not con:
        st.error("❌ No se pudo conectar a la base de datos.")
        return

    try:
        cursor = con.cursor()
        cursor.execute("SELECT ID, Nombre, Usuario FROM Clientes")
        datos = cursor.fetchall()

        if datos:
            df = pd.DataFrame(datos, columns=["ID", "Nombre", "Usuario"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No hay clientes registrados.")
    except Exception as e:
        st.error(f"⚠️ Error al obtener los datos: {e}")
    finally:
        con.close()

def registrar_cliente():
    st.subheader("📝 Registrar nuevo cliente")

    nombre = st.text_input("Nombre completo")
    usuario = st.text_input("Usuario")
    contra = st.text_input("Contraseña", type="password")

    if st.button("Registrar"):
        if not nombre or not usuario or not contra:
            st.warning("Por favor, completa todos los campos.")
            return

        con = obtener_conexion()
        if not con:
            st.error("❌ No se pudo conectar a la base de datos.")
            return

        try:
            cursor = con.cursor()
            query = "INSERT INTO Clientes (Nombre, Usuario, Contra) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, usuario, contra))
            con.commit()
            st.success(f"✅ Cliente '{nombre}' registrado exitosamente.")
        except Exception as e:
            st.error(f"⚠️ Error al registrar cliente: {e}")
        finally:
            con.close()
