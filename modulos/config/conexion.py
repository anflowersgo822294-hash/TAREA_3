import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bdhzgugh2n5aomi8gbnb-mysql.services.clever-cloud.com',
            user='uikmi0cozxpsooss',
            password='hz7AxRCrsQP57DKsxXwf',
            database='bdhzgugh2n5aomi8gbnb',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
