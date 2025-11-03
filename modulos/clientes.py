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
        # Se eliminó la columna ID para evitar el error 1054
        cursor.execute("SELECT Nombre, Usuario FROM Clientes")
        datos = cursor.fetchall()

        if datos:
            df = pd.DataFrame(datos, columns=["Nombre", "Usuario"])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("ℹ️ No hay clientes registrados.")
    except Exception as e:
        st.error(f"⚠️ Error al obtener los datos: {e}")
    finally:
        con.close()

def registrar_cliente():
    st.subheader("📝 Registrar nuevo cliente")

    nombre = st.text_input("Nombre completo").strip()
    usuario = st.text_input("Usuario").strip()
    contra = st.text_input("Contraseña", type="password").strip()

    if st.button("Registrar"):
        if not nombre or not usuario or not contra:
            st.warning("⚠️ Por favor, completa todos los campos.")
            return

        con = obtener_conexion()
        if not con:
            st.error("❌ No se pudo conectar a la base de datos.")
            return

        try:
            cursor = con.cursor()

            # Validación para evitar usuarios duplicados
            cursor.execute("SELECT COUNT(*) FROM Clientes WHERE Usuario = %s", (usuario,))
            existe = cursor.fetchone()[0]
            if existe > 0:
                st.error("❌ El usuario ya está registrado. Usa otro nombre de usuario.")
                return

            query = "INSERT INTO Clientes (Nombre, Usuario, Contra) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre, usuario, contra))
            con.commit()
            st.success(f"✅ Cliente '{nombre}' registrado exitosamente.")
        except Exception as e:
            st.error(f"⚠️ Error al registrar cliente: {e}")
        finally:
            con.close()
