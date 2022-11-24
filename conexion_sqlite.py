  # Aplicacion de CRUD con pyQt5 y SQLite
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import sqlite3
import psycopg2
connetion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="2020",
            database="BdRefaccionaria_",
            port="5432"
        ) 
connetion.autocommit=True

class Comunicacion():

    def inserta_producto(self,codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO tabla_datos (CODIGO, NOMBRE, MODELO, PRECIO, CANTIDAD) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()


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
        bd = "SELECT * FROM tabla_datos " 
        cursor.execute(bd)
        registro = cursor.fetchall()
        return registro

    def busca_productos(self, nombre_producto):
        cursor=connetion.cursor()
        query= f"""    select * from refacciones where codigobarras={nombre_producto} """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()    
        
        return nombreX 



         



    def busca_producto(self, nombre_producto):
        cursor=connetion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()     
        return nombreX 

    def elimina_productos(self, nombre):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM tabla_datos WHERE NOMBRE = {}'''.format(nombre)
        cursor.execute(bd)
        self.conexion.commit()    
        cursor.close()

    def elimina_productoss(self, nombre):
        print(nombre)
        cursor=connetion.cursor()
        query= f"""    delete  from refacciones where codigobarras={nombre} """ 
        cursor.execute(query)
        #self.connetion.commit()    
        cursor.close()
  
    def actualiza_productos(self,Id, codigo, nombre, modelo, precio, cantidad):
        cursor = self.conexion.cursor()
        bd = '''UPDATE tabla_datos SET  CODIGO ='{}', NOMBRE = '{}' , MODELO = '{}', PRECIO = '{}', CANTIDAD = '{}'
        WHERE ID = '{}' '''.format(codigo, nombre, modelo, precio, cantidad, Id)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexion.commit()    
        cursor.close()
        return a  


    def actualizacion_(self,id,codigop,categoria,preciocosto,precioventa,existencias,descripcion):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" UPDATE refacciones set values('{id}','{codigop}','{categoria}','{preciocosto}','{precioventa}','{existencias}','{descripcion}') """
        cursor.execute(query)
        cursor.close()

    def actual(self,id,codigop,categoria,preciocosto,precioventa,existencias,descripcion):#registra a un empleado
        print("hola")
        cursor=connetion.cursor()
        query= f""" UPDATE refacciones set  codigop='{codigop}',categoria='{categoria}',preciocosto='{preciocosto}',precioventa='{precioventa}',existencias='{existencias}',descripcion='{descripcion}'  where codigobarras='{id}'"""       
        cursor.execute(query)
        cursor.close()

