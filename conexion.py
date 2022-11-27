import psycopg2
from psycopg2 import extras
connetion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="2020",
            database="BdRefaccionaria_",
            port="5432"
        ) 
connetion.autocommit=True
class Comunicacion():
    def BuscarRefaccion(self, nombre_producto):#busca entero de codigo de barras de refacciones
        cursor=connetion.cursor()
        query= f"""    select  * from refacciones where codigobarras={nombre_producto} """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()    
        return nombreX 

    def mostrar(self):#muestra todas las refacciones
        cursor = connetion.cursor()
        bd = """ SELECT * FROM refacciones """
        cursor.execute(bd)
        registro = cursor.fetchall()
        return (registro)

    def busca_refacciones(self):#busca refacciones que ya no esten en el stock
        cursor=connetion.cursor()
        query= f"""    select * from refacciones where existencias=0 """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()     
        return nombreX 

    def elimina_productoss(self, nombre):#elimina por codigo de barras a un refaccion
        cursor=connetion.cursor()
        query= f"""    delete  from refacciones where codigobarras={nombre} """ 
        cursor.execute(query)
        connetion.commit()    
        cursor.close()

    def busquedaDuplicidad(self,cadena):#busca que en vendedor no este duplicada la primary key
        cursor=connetion.cursor()
        query=f"""   select * from vendedor where telefono='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def busquedaDuplicidadP(self,cadena):#evita duplicidad con refacciones codigo de barras primary key
        cursor=connetion.cursor()
        query=f"""   select * from refacciones where codigobarras='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def alta(self,nombre,npaterno,nmaterno,salario,exterior,calle,telefono,estado,cp):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" INSERT INTO vendedor(nombre,paterno,materno,salario,telefono,calle,numexterior,codigopostal,estado) values('{nombre}','{npaterno}','{nmaterno}','{salario}','{telefono}','{calle}','{exterior}','{cp}','{estado}') """
        cursor.execute(query)
        connetion.commit()    
        cursor.close()

    def busquedaDuplicidadProve(self,cadena):#evita duplicidad de un provedor
        cursor=connetion.cursor()
        query=f"""   select * from provedor where idprovedor='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False
  
    def altaRefaccion(self,codigoBarras,codigoProducto,categoria,PrecioProvedor,PrecioPublico,UnidadesRecibidas,descripcion):#registra a una refaccion
        cursor=connetion.cursor()
        query= f""" INSERT INTO refacciones(codigobarras,codigop,categoria,preciocosto,precioventa,existencias,descripcion) values('{codigoBarras}','{codigoProducto}','{categoria}','{PrecioProvedor}','{PrecioPublico}','{UnidadesRecibidas}','{descripcion}') """
        cursor.execute(query)
        cursor.close()

    def altaProvedor(self,IDprovedor,marca,telefono,calle,exterior,codigopostal,estado):#registra a un provedor
        cursor=connetion.cursor()
        query= f""" INSERT INTO provedor(idprovedor,marca,telefono,calle,numexterior,codigopostal,estado) values('{IDprovedor}','{marca}','{telefono}','{calle}','{exterior}','{codigopostal}','{estado}') """
        cursor.execute(query)
        cursor.close()

