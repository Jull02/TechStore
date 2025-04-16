from PosVenta import registrar_venta
from Inventario import actualizar_producto

# Ejemplo: Cambiar precio y descripción del producto 1
actualizar_producto(1, 1000.00, "Laptop Gamer - 32GB RAM, SSD 1TB")


# Ejemplo: Venta de 1 laptop gamer desde Quito Centro
registrar_venta(id_producto=2, cantidad=1, tienda="Quito Centro")
