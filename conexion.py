

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

   


    def alta(self,nombre,npaterno,nmaterno,salario,exterior,calle,telefono,estado,cp):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" INSERT INTO vendedor(nombre,paterno,materno,salario,telefono,calle,numexterior,codigopostal,estado) values('{nombre}','{npaterno}','{nmaterno}','{salario}','{telefono}','{calle}','{exterior}','{cp}','{estado}') """
        cursor.execute(query)
        cursor.close()

    def altaProvedor(self,IDprovedor,marca,telefono,calle,exterior,codigopostal,estado):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" INSERT INTO provedor(idprovedor,marca,telefono,calle,numexterior,codigopostal,estado) values('{IDprovedor}','{marca}','{telefono}','{calle}','{exterior}','{codigopostal}','{estado}') """
        cursor.execute(query)
        cursor.close()

    def altaRefaccion(self,codigoBarras,codigoProducto,categoria,PrecioProvedor,PrecioPublico,UnidadesRecibidas,descripcion):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" INSERT INTO refacciones(codigobarras,codigop,categoria,preciocosto,precioventa,existencias,descripcion) values('{codigoBarras}','{codigoProducto}','{categoria}','{PrecioProvedor}','{PrecioPublico}','{UnidadesRecibidas}','{descripcion}') """
        cursor.execute(query)
        cursor.close()


    def mostrar(self):
        cursor = connetion.cursor()
        bd = """ SELECT * FROM refacciones """
        cursor.execute(bd)
        registro = cursor.fetchall()
        return (registro)



    def busca_refaccion(self, nombre_producto):
        cursor=connetion.cursor()
        query= f"""    select * from refacciones where codigobarras={nombre_producto} """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()     
        #nombreX devuelve todos los datos
        return nombreX 


    def busca_refacciones(self):
        cursor=connetion.cursor()
        query= f"""    select * from refacciones where existencias=0 """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()     
        #nombreX devuelve todos los datos
        return nombreX 
    

    def busca_refaccioness(self,nombre):
        cursor=connetion.cursor()
        query= f"""    select * from refacciones where codigobarras={nombre} """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()     
        #nombreX devuelve todos los datos
        return nombreX 

    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        bd = """SELECT * FROM tabla_datos """
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_productos(self, nombre_producto):
        cursor=connetion.cursor(cursor_factory=extras.DictCursor)
        query= f"""    select  * from refacciones where codigobarras={nombre_producto} """   
        cursor.execute(query)
        nombreX = cursor.fetchone()
        print(nombreX)
        
        cursor.close()    
        return nombreX 

    def elimina_productoss(self, nombre):
        cursor=connetion.cursor()
        query= f"""    delete  from refacciones where codigobarras={nombre} """ 
        cursor.execute(query)
        #self.connetion.commit()    
        cursor.close()
  
    def actualizacion_(self,id,codigop,categoria,preciocosto,precioventa,existencias,descripcion):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" UPDATE refacciones set values('{id}','{codigop}','{categoria}','{preciocosto}','{precioventa}','{existencias}','{descripcion}') """
        cursor.execute(query)
        cursor.close()

    def actual(self,id,codigop,categoria,preciocosto,precioventa,existencias,descripcion):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" UPDATE refacciones set  codigop='{codigop}',categoria='{categoria}',preciocosto='{preciocosto}',precioventa='{precioventa}',existencias='{existencias}',descripcion='{descripcion}'  where codigobarras='{id}'"""       
        cursor.execute(query)
        cursor.close()

    def busquedaDuplicidad(self,cadena):
        cursor=connetion.cursor()
        query=f"""   select * from vendedor where telefono='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def busquedaDuplicidadP(self,cadena):
        cursor=connetion.cursor()
        query=f"""   select * from provedor where idprovedor='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def busquedaDuplicidad_(self,cadena):
        cursor=connetion.cursor()
        query=f"""   select * from refacciones where codigobarras='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def busquedaDuplicidad_P(self,cadena):
        cursor=connetion.cursor()
        query=f"""   select * from refacciones where codigop='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False



