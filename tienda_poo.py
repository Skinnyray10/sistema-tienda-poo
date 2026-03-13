class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def vender(self, cantidad):
        self.stock -= cantidad

class Electronico(Producto): 
    def __init__(self, nombre, precio, stock, meses_garantia):
        super().__init__(nombre, precio, stock)
        self.meses_garantia = meses_garantia 
        
class Ropa(Producto):
  def __init__(self,nombre,precio,stock,meses_garantia,talla_ropa):
    super().__init__(nombre,precio,stock)
    self.meses_garantia = meses_garantia 
    self.talla_ropa = talla_ropa

mi_telefono = Electronico("iPhone", 800, 5, 12)
mi_telefono.vender(1)
mi_ropa = Ropa("Playera estampado",1200,10,12,"M")
print(f"Vendí un {mi_telefono.nombre}. Quedan {mi_telefono.stock} en stock. Tiene {mi_telefono.meses_garantia} meses de garantía.")
print(f"Vendí una {mi_ropa.nombre}. Talla {mi_ropa.talla_ropa} Quedan {mi_ropa.stock} en stock. Tiene {mi_ropa.meses_garantia} meses de garantía.")
