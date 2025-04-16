import mysql.connector
from ConnectData import conectar


def registrar_venta(id_producto, cantidad, tienda):
    conn = conectar()
    cursor = conn.cursor()

    # Registrar venta
    cursor.execute("""
        INSERT INTO Ventas (id_producto, cantidad_vendida, tienda)
        VALUES (%s, %s, %s)
    """, (id_producto, cantidad, tienda))

    # Actualizar inventario
    cursor.execute("""
        UPDATE Inventario
        SET cantidad = cantidad - %s
        WHERE id_producto = %s AND tienda = %s
    """, (cantidad, id_producto, tienda))

    conn.commit()
    print("✅ Venta registrada y stock actualizado")
    conn.close()
