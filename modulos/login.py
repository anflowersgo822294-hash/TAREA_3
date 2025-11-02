import streamlit as st
from modulos.config.conexion import obtener_conexion

def verificar_usuario(usuario, contra):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None

    st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Nombre FROM Clientes WHERE Usuario = %s AND Contra = %s"
        cursor.execute(query, (usuario, contra))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        st.error(f"❌ Error al ejecutar la consulta: {e}")
        return None
    finally:
        con.close()

def login():
    st.title("🔐 Inicio de sesión")

    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    usuario = st.text_input("Usuario", key="Usuario_input")
    contra = st.text_input("Contraseña", type="password", key="Contra_input")

    if st.button("Iniciar sesión"):
        if not usuario or not contra:
            st.warning("⚠️ Por favor, completa ambos campos.")
            return

        nombre_cliente = verificar_usuario(usuario, contra)

        if nombre_cliente:
            st.session_state["sesion_iniciada"] = True
            st.session_state["usuario"] = usuario
            st.session_state["nombre_cliente"] = nombre_cliente
            st.success(f"Bienvenido, {nombre_cliente} 👋")
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
       
