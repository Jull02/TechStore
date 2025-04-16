from PosVenta import registrar_venta
from Inventario import actualizar_producto

# Ejemplo: Cambiar precio y descripción del producto 1
actualizar_producto(1, 1000.00, "Laptop Gamer - 32GB RAM, SSD 1TB")
actualizar_producto(2, 28.00, "Mouse Inalámbrico con sensor óptico mejorado")
actualizar_producto(3, 310.00, "Monitor LED 27 pulgadas Full HD 165Hz")


# Ejemplo: Venta de 1 laptop gamer desde Quito Centro
registrar_venta(id_producto=2, cantidad=1, tienda="Quito Centro")
registrar_venta(id_producto=4, cantidad=3, tienda="Guayaquil Sur")
