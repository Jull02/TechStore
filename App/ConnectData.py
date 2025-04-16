# filepath: d:\UDLA\Noveno Semestre\Integración de sistemas\Productos\ConnectData.py
import mysql.connector


def conectar():
    conexion = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='productos_is',
        port=3306
    )
    return conexion
