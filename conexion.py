import psycopg2
from psycopg2 import extras
connetion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="2020",
            database="refaccionaria",
            port="5432"
        ) 
connetion.autocommit=True
class Comunicacion():
    def BuscarRefaccion(self, nombre_producto):#busca entero de codigo de barras de refacciones
        cursor=connetion.cursor()
        query= f"""    select  codigobarras,codigop,categoria,precioventa,existencias,descripcion,idprovedorwe from refacciones where codigobarras={nombre_producto} """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()    
        return nombreX 

    def mostrar(self):#muestra todas las refacciones
        cursor = connetion.cursor()
        bd = """ select codigobarras,codigop,categoria,precioventa,existencias,descripcion,idprovedorwe from refacciones  """
        cursor.execute(bd)
        registro = cursor.fetchall()
        return (registro)

    def busca_refacciones(self):#busca refacciones que ya no esten en el stock
        cursor=connetion.cursor()
        query= f"""    select codigobarras,codigop,categoria,precioventa,existencias,descripcion,idprovedorwe from refacciones where existencias<5 """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()     
        return nombreX 

    def elimina_productoss(self, nombre):#elimina por codigo de barras a un refaccion

        cursor=connetion.cursor()
        query= f"""    delete  from genera where codigobarras={nombre} """ 
        cursor.execute(query)
        connetion.commit()  

        cursor=connetion.cursor()
        query= f"""    delete  from refacciones where codigobarras={nombre} """ 
        cursor.execute(query)
        connetion.commit()   

        

        cursor.close()

    def elimina_productoss2(self, nombre):#elimina por codigo de barras a un refaccion
        



        cursor=connetion.cursor()
        query= f"""    select codigobarras from refacciones where categoria='{nombre}' """ 
        cursor.execute(query)
        nombreX = cursor.fetchone()
        
       

        if nombreX!= None:


            query= f"""    delete  from genera where codigobarras='{nombreX[0]}' """ 
            cursor.execute(query)
            connetion.commit()  

            cursor=connetion.cursor()
            query= f"""    delete  from refacciones where codigobarras='{nombreX[0]}' """ 
            cursor.execute(query)
            connetion.commit()   

        

            cursor.close()
        

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
        return False#

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
  
    def altaRefaccion(self,codigoBarras,codigoProducto,categoria,PrecioProvedor,PrecioPublico,UnidadesRecibidas,descripcion,id):#registra a una refaccion
        cursor=connetion.cursor()
        query= f""" INSERT INTO refacciones(codigobarras,codigop,categoria,preciocosto,precioventa,existencias,descripcion,idprovedorwe) values('{codigoBarras}','{codigoProducto}','{categoria}','{PrecioProvedor}','{PrecioPublico}','{UnidadesRecibidas}','{descripcion}','{id}') """
        cursor.execute(query)
        cursor.close()
        

    def altaProvedor(self,IDprovedor,marca,telefono,calle,exterior,codigopostal,estado):#registra a un provedor
        cursor=connetion.cursor()
        query= f""" INSERT INTO provedor(idprovedor,marca,telefono,calle,numexterior,codigopostal,estado) values('{IDprovedor}','{marca}','{telefono}','{calle}','{exterior}','{codigopostal}','{estado}') """
        cursor.execute(query)
        cursor.close()


    def UPDATESurte(self,codigobarras,cantidad):
        cursor=connetion.cursor()
        query= f""" UPDATE refacciones
set existencias = existencias+'{cantidad}'
where refacciones.codigobarras='{codigobarras}' """
        cursor.execute(query)
        connetion.commit()    
        cursor.close()

    def busquedaDuplicidadProveYrefa(self,cadena,codigo):#evita duplicidad de un provedor
        cursor=connetion.cursor()
        query=f"""   select * from refacciones where idprovedorwe='{cadena}' and codigobarras='{codigo}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def busquedaDuplicidadCliente(self,cadena):#evita duplicidad de un provedor
        cursor=connetion.cursor()
        query=f"""   select * from cliente where telefono='{cadena}' """
        cursor.execute(query)
        user=cursor.fetchone()
        if user==None:
           return True
        return False

    def altaCliente(self,nombre,npaterno,nmaterno,clienteclave,email,telefono,exterior,calle,estado,cp):#registra a un empleado
        cursor=connetion.cursor()
        query= f""" INSERT INTO cliente(nombre,paterno,materno,clienteclave,email,telefono,calle,numexterior,codigopostal,estado) values('{nombre}','{npaterno}','{nmaterno}','{clienteclave}','{email}','{telefono}','{calle}','{exterior}','{cp}','{estado}') """
        cursor.execute(query)
        connetion.commit()    
        cursor.close()

    def devolver(self,num):
        cursor=connetion.cursor()
        query=f"""   select numcliente from cliente where telefono='{num}' """
        cursor.execute(query)
        user=cursor.fetchone()
        return user

    def crearfactura(self,numcliente):
        cursor=connetion.cursor()
        query= f""" insert into factura (fechafactura,cantidadproductos,subtotal,iva,total,numcliente)values(current_date,'0','0','0','0','{numcliente}') RETURNING(numfactura)
 """
        cursor.execute(query)
        user=cursor.fetchone()
        connetion.commit()    
        cursor.close()
        return user
       

    def buscarCliente(self,num):
        cursor=connetion.cursor()
        query=f"""   select nombre,paterno,materno from cliente where numcliente='{num}' """
        cursor.execute(query)
        user=cursor.fetchone()
        return user

    def buscarNumfactura(self,num):
        cursor=connetion.cursor()
        query=f"""   select numfactura from factura where numcliente='{num}' """
        cursor.execute(query)
        user=cursor.fetchone()
        return user

    def meterArticulos(self,numbarras,numfacturas,codigo):
        cursor=connetion.cursor()
        query= f""" insert into genera (codigobarras,cantidadp,numfactura,codigoproducto)values('{numbarras}','1','{numfacturas}',{codigo})
 """
        cursor.execute(query)
        connetion.commit()    
        cursor.close()
       
    def bsuca(self,num,barras):
        cursor=connetion.cursor()
        query=f"""   select cantidadp from genera where numfactura='{num}' and  codigobarras='{barras}'  """
        cursor.execute(query)
        user=cursor.fetchone()
        connetion.commit()    
        cursor.close()

        if user==None:
           
           vari=self.busquedaDuplicidadP(barras)
           if vari==False:
            self.meterArticulos(barras,num,'30')
        else:
           
            var=int(user[0])+1
            cursor=connetion.cursor()
            query= f""" UPDATE  genera SET cantidadp='{var}' WHERE numfactura='{num}' and codigobarras='{barras}'"""
            cursor.execute(query)
            connetion.commit()    
            cursor.close()
        

       
        return user

    #def mostrarM(self,numfactu):#muestra todas las refacciones
    #    cursor = connetion.cursor()
    #    bd=f"""   select * from genera where numfactura='{numfactu}' """
    #    cursor.execute(bd)
    #    registro = cursor.fetchall()
   #     return (registro)

   
    def mostrarM(self,numfactu):#muestra todas las refacciones
        cursor = connetion.cursor()
        bd=f"""   select genera.codigobarras,genera.cantidadp,genera.numfactura,refacciones.categoria,refacciones.precioventa,refacciones.descripcion,refacciones.idprovedorwe from genera
inner join refacciones on 
genera.codigobarras=refacciones.codigobarras WHERE numfactura={numfactu}
 """
        cursor.execute(bd)
        registro = cursor.fetchall()
        
        return (registro)

    def BuscarRefaccioncategoria(self, nombre_producto):#busca entero de codigo de barras de refacciones
        cursor=connetion.cursor()
        query= f"""    select  codigobarras,codigop,categoria,precioventa,existencias,descripcion,idprovedorwe from refacciones where categoria ilike '%{nombre_producto}%' """   
        cursor.execute(query)
        nombreX = cursor.fetchall()
        cursor.close()    
        return nombreX 

   
     
    def mostra(self,numfactu,codigobarras):#muestra todas las refacciones
        cursor = connetion.cursor()
        codigop=self.ma(codigobarras)
        
        bd=f"""    select  refacciones.precioventa from genera
inner join refacciones on 
genera.codigobarras=refacciones.codigobarras WHERE codigop='{codigop[0]}' and numfactura='{numfactu}'

 """
        cursor.execute(bd)
        registro = cursor.fetchone()
       
        return (registro)

    def ma(self,codigo):
        cursor=connetion.cursor()
        query=f"""   select codigop from refacciones where codigobarras='{codigo}'   """
        cursor.execute(query)
        user=cursor.fetchone()
        connetion.commit()    
        cursor.close()
        return user
    
    def actualizarFacturas(self,numfactura):
        cursor=connetion.cursor()
        query=f"""   select sum(cantidadp) from genera where numfactura='{numfactura}'   """
        cursor.execute(query)
        user=cursor.fetchone()
        connetion.commit()    
        cursor.close()
        return user

    def meteractualizacon(self,cantidad,subtotal,iva,total,numfactura):
        if cantidad != None:
            cursor=connetion.cursor()
            query= f""" update factura set  cantidadproductos='{cantidad}',subtotal='{subtotal}',iva='{iva}',total='{total}' where numfactura='{numfactura}' 
 """

            cursor.execute(query)
            connetion.commit()    
            cursor.close()


    def bajar(self,factura):
        cursor=connetion.cursor()
        query= f"""UPDATE refacciones
set existencias = existencias-genera.cantidadp
from genera
where refacciones.codigobarras=genera.codigobarras and numfactura='{factura}' and existencias>=genera.cantidadp
 """
        cursor.execute(query)
        connetion.commit()    
        cursor.close()
   


    def imprimir(self,numfactura):
        cursor=connetion.cursor()
        query=f"""   select codigobarras,cantidadp,categoria,precioventa,descripcion from genera natural join refacciones where numfactura='{numfactura}'   """

        

        cursor.execute(query)
        user=cursor.fetchall()
        connetion.commit()    
        cursor.close()
        return user


    def imprimirDATOS(self,numfactura):
        cursor=connetion.cursor()
        query=f"""   select nombre,paterno,materno,fechafactura,numfactura,numcliente from factura natural join cliente where numfactura='{numfactura}'
   """

        

        cursor.execute(query)
        user=cursor.fetchone()
        connetion.commit()    
        cursor.close()
        return user


    def mostrarinformacion(self,numfactura):
        cursor=connetion.cursor()
        query=f"""     select codigobarras,cantidadp,precioventa,descripcion  from genera natural join refacciones where numfactura='{numfactura}'

   """
        cursor.execute(query)
        user=cursor.fetchall()
        connetion.commit()    
        cursor.close()
        return user


    def mostrarinformacion_(self,numfactura):
        cursor=connetion.cursor()
        query=f"""     select fechafactura,cantidadproductos,subtotal,iva,total,numfactura from factura where numcliente='{numfactura}'



   """
        cursor.execute(query)
        user=cursor.fetchall()
        connetion.commit()    
        cursor.close()
        return user


    def mostrarinformacionProvedor(self):
        cursor=connetion.cursor()
        query=f"""     select idprovedor,marca,telefono,calle, numexterior,codigopostal,estado from provedor



   """
        cursor.execute(query)
        user=cursor.fetchall()
        connetion.commit()    
        cursor.close()
        return user

    def mostrarinformacioncLIENTE(self):
        cursor=connetion.cursor()
        query=f"""     select numcliente,  nombre, telefono, calle,numexterior, codigopostal,estado  from cliente"""
        cursor.execute(query)
        user=cursor.fetchall()
        connetion.commit()    
        cursor.close()
        return user

    def verifi(self,barras):
        cursor=connetion.cursor()
        query=f""" select existencias from refacciones where codigobarras='{barras}'
     """
        cursor.execute(query)
        user=cursor.fetchone()
        cursor.close()
        if user==None:
            return False
        if user[0]>0 and user[0]!= None:
            return True
        else:
            return False
        
        

    def ver(self,barras):
        cursor=connetion.cursor()
        query=f""" select numcliente from factura where numcliente='{barras}'
     """
        cursor.execute(query)
        user=cursor.fetchone()
        cursor.close()
        if user==None:
            return False
        else:
            return True


