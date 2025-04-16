import mysql.connector
from ConnectData import conectar


def actualizar_producto(id_producto, precio, descripcion):
    conexion = conectar()
    cursor = conexion.cursor()
    query = """
        UPDATE productos
        SET precio = %s, descripcion = %s
        WHERE id_producto = %s
    """
    cursor.execute(query, (precio, descripcion, id_producto)
                   )  # Ensure all parameters are passed
    conexion.commit()
    cursor.close()
    conexion.close()
