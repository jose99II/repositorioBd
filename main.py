import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import  QPropertyAnimation,QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        self.total=0
        super(VentanaPrincipal, self).__init__()
        loadUi('diseño.ui', self)
        self.bt_menu.clicked.connect(self.mover_menu)
        self.base_datos = Comunicacion() 
        self.bt_restaurar.hide()
        self.bt_refrescar.clicked.connect(self.mostrarRefacciones)
        self.bt_agregar.clicked.connect(self.registrar_productos)
        self.btregistra.clicked.connect(self.registrar_provedor) 
        self.btnLimpiarProvedor.clicked.connect(self.LimpiarProvedor) 
        self.reg_refaccion_p.clicked.connect(self.registrar_Refaccion) 
        self.btnBuscar.clicked.connect(self.Buscar_LlavePrimariaVarchar)
        self.radioButton.clicked.connect(self.buscar_MateriaInexistente)
        self.btneliminar.clicked.connect(self.eliminar_refaccion)
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)     
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.INGRESAR.clicked.connect(self.ingresarMercancia)
        self.registra.clicked.connect(self.registrar_CLIENTE)
        self.VERIFICAR.clicked.connect(self.verificarUsuario)
        self.bt_actualiza_buscar.clicked.connect(self.agregar)



        self.bt_cerrar.clicked.connect(lambda: self.close())
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        # mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        # coneccion botones
        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_datos))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.bt_COBRAR.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.bt_ajustes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_ajustes))
        self.btnProvedor.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_provedor))
        self.RefaccionesBTN.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_refacciones))
        self.actua.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_actualizar))
        self.surtir.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_INGRESAR))
        self.CLIENTE.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_registrarCliente))

        # Ancho de columna adaptable
        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
    def control_bt_minimizar(self):
        self.showMinimized()        
    def  control_bt_normal(self): 
        self.showNormal()       
        self.bt_restaurar.hide()
        self.bt_maximizar.show()

    def  control_bt_maximizar(self): 
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

    def resizeEvent(self, event):
        rect = self.rect()
        self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)

    ## mover ventana
    def mousePressEvent(self, event):
        self.click_position = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:         
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.click_position)
                self.click_position = event.globalPos()
                event.accept()
        if event.globalPos().y() <=10:
            self.showMaximized()
            self.bt_maximizar.hide()
            self.bt_restaurar.show()
        else:
            self.showNormal()
            self.bt_restaurar.hide()
            self.bt_maximizar.show()

    def mover_menu(self):
        if True:            
            width = self.frame_control.width()
            normal = 0
            if width==0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
#restauracion
    def Buscar_LlavePrimariaVarchar(self):#busca codigo por codigo de barras {integer o varchar}
        nombre_producto = self.buscar.text()
        if len(nombre_producto)==0:
            self.aviso.setText('ESPACIO VACIO')  
            return
        else:
                bandera=self.is_valid(nombre_producto)
                if bandera==True:
                    nombre_producto = str("'" + nombre_producto + "'")
                    producto = self.base_datos.BuscarRefaccion(nombre_producto)
                    self.mostraTabla_productos(producto)
                    
    def is_valid(self,cadena):#valida si todos sus caracteres son numericos
            longitud=len(cadena)
            contador=0
            for validar in cadena:
                if validar.isdigit():
                    contador=contador+1
            if(contador==longitud and cadena!=''):
                return True
            self.aviso.setText('PRODUCTO NO VALIDO')
            return False

    def mostrarRefacciones(self): #boton refrescar muestra todas las refacciones
        datos = self.base_datos.mostrar()
        self.mostraTabla_productos(datos)
       
    def buscar_MateriaInexistente(self):#muestra solo los que no tienen en existencia
        nombre_producto = '0'
        nombre_producto = str("'" + nombre_producto + "'")
        producto = self.base_datos.busca_refacciones()
        self.mostraTabla_productos(producto)

    def mostraTabla_productos(self,datos):#muestra la tabla tabla_productos
        self.tabla_productos.setRowCount(len(datos))
        if len(datos) == 0:
            self.aviso.setText(' NO EXISTE')       
        else:
            self.aviso.setText('PRODUCTO ENCONTRADO')
        i = len(datos)
        self.tabla_productos.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.Id = row[0]
            columna1=QtWidgets.QTableWidgetItem(str(row[0]))
            columna3=QtWidgets.QTableWidgetItem(str(row[3]))
            columna4=QtWidgets.QTableWidgetItem(str(row[4]))
            columna5=QtWidgets.QTableWidgetItem(str(row[5]))
            self.tabla_productos.setItem(tablerow,0,columna1)
            self.tabla_productos.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_productos.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_productos.setItem(tablerow,3,columna3)
            self.tabla_productos.setItem(tablerow,4,columna4)
            self.tabla_productos.setItem(tablerow,5,columna5)
            self.tabla_productos.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
            tablerow +=1

    def eliminar_refaccion(self):#elimina refaccion por codigo de barras
        nombre_producto = self.buscar.text()
        if len(nombre_producto)==0:
            return
        else:
            bandera=self.is_valid(nombre_producto)
            if(bandera==True):
                nombre_producto = str("'" + nombre_producto + "'")
                self.base_datos.elimina_productoss(nombre_producto)
                self.mostrarRefacciones()

    def registrar_productos(self):#registrar vendedor
        if (len(self.txtcp.text())==0  and len(self.txtexterior.text())==0  and len(self.txtsalario.text())==0  and len(self.txtnombre.text())==0 and len(self.txtpaterno.text())==0 and len(self.txtmaterno.text())==0 and len(self.txtcalle.text())==0 and len(self.txttelefono.text())==0 and len(self.txtestado.text())==0):
            self.signal_registrar.setText('ESPACIOS VACIOS')
            return
        else:
            nombre = self.txtnombre.text().upper()  
            npaterno = self.txtpaterno.text().upper() 
            nmaterno = self.txtmaterno.text().upper() 
            bandera=self.is_valid(self.txtsalario.text())
            if bandera==True:
                salario = int(self.txtsalario.text())
            else:
                salario=0
            bandera=self.is_valid(self.txtexterior.text())
            if bandera==True:
                exterior = int(self.txtexterior.text())
            else:
                exterior=0
            calle =self.txtcalle.text().upper() 
            telefono=self.txttelefono.text().upper() 
            estado=self.txtestado.text().upper() 
            bandera=self.is_valid(self.txtcp.text())
            if bandera==True:
                cp = int(self.txtcp.text())
            else:
                cp=0
            if nombre != '' and npaterno != '' and nmaterno != '' and salario > 0 and exterior > 0 and calle != '' and telefono != '' and estado !='' and cp > 0:
                validacion=self.base_datos.busquedaDuplicidad(str(telefono))
                if validacion==True:
                    self.base_datos.alta(nombre,npaterno,nmaterno,salario,exterior,calle,telefono,estado,cp)
                    self.signal_registrar.setText('VENDEDOR REGISTRADO CON EXITO')
                else:
                    self.signal_registrar.setText('ERROR TELEFONO YA REGISTRADO')
                self.txtnombre.clear()
                self.txtpaterno.clear()
                self.txtmaterno.clear()
                self.txtsalario.clear()
                self.txtexterior.clear()
                self.txtcalle.clear()
                self.txttelefono.clear()
                self.txtestado.clear()
                self.txtcp.clear()
            else:
                self.signal_registrar.setText('ESPACIOS INCORRECTOS')

    def registrar_Refaccion(self):#registrar refaccion
        if (len(self.CBtxt.text())==0  and len(self.codigoProduct.text())==0  and len(self.categoriatxtregistrorefa.text())==0  and len(self.precioProvedor.text())==0 and len(self.precioPublic.text())==0 and len(self.UnidadesRecibidas.text())==0 and len(self.descripcion_txt_.text())==0 ):
            self.avisoregistro.setText('ESPACIOS VACIOS')
            return
        bandera=self.is_valid(self.CBtxt.text())
        if bandera==True:
            codigoBarras=int(self.CBtxt.text())
        else:
            self.avisoregistro.setText('CODIGO DE BARRAS INVALIDO')
            return
            codigoBarras=0
        codigoProducto = self.codigoProduct.text().upper() 
        categoria = self.categoriatxtregistrorefa.text().upper() 
        bandera=self.is_valid(self.precioProvedor.text())
        if bandera==True:
            PrecioProvedor=int(self.precioProvedor.text())
        else:
            self.avisoregistro.setText('PRECIO PROVEDOR INVALIDO')
            PrecioProvedor=0
        bandera=self.is_valid(self.precioPublic.text())
        if bandera==True:
            PrecioPublico=int(self.precioPublic.text())
        else:
            PrecioPublico=0
            self.avisoregistro.setText('PRECIO AL PUBLICO INVALIDO')
        bandera=self.is_valid(self.precioPublic.text())
        if bandera==True:
            UnidadesRecibidas=int(self.UnidadesRecibidas.text())
        else:
            UnidadesRecibidas=0        
        descripcion = self.descripcion_txt_.text().upper() 
        if descripcion != '' and codigoProducto != ''    and categoria != '' and PrecioProvedor > 0 and PrecioPublico > 0 and UnidadesRecibidas > -1 and codigoBarras > 0:
            validacion=self.base_datos.busquedaDuplicidadP(codigoBarras)
            
            if validacion==True:
                        #ME QUEDE
                    verifica=self.base_datos.busquedaDuplicidadProve(self.prov.text())
                    if verifica==False:
                        self.base_datos.altaRefaccion(codigoBarras,codigoProducto,categoria,PrecioProvedor,PrecioPublico,UnidadesRecibidas,descripcion,self.prov.text())
                        self.avisoregistro.setText('REFACCION REGISTRADA')
                        self.CBtxt.clear()
                        self.codigoProduct.clear()
                        self.categoriatxtregistrorefa.clear()
                        self.precioProvedor.clear()
                        self.precioPublic.clear()
                        self.UnidadesRecibidas.clear()
                        self.descripcion_txt_.clear()
                        self.prov.clear()
                    else:
                        self.avisoregistro.setText('ID DE PROVEDOR NO VALIDO')
            else:
                self.avisoregistro.setText('CODIGO DE BARRAS REGISTRADO PPREVIAMENTE')
        else:
            self.IDsprovedor.setText('EXISTEN ESPACIOS VACIOS O INCORRECTOS')

    def registrar_provedor(self):#registrar provedor
        marca = self.marcatxt.text().upper() 
        telefono = self.telefonotxt_.text().upper() 
        IDprovedor = self.telefonotxt_.text().upper()+self.marcatxt.text().upper() 
        calle = self.calle_txt.text().upper()
        bandera=self.is_valid(self.exteriortxt_.text())
        if bandera==True:
            exterior = int(self.exteriortxt_.text())
        else:
            self.IDsprovedor.setText('NUMERO EXTERIOR INVALIDO')
            exterior=0
        bandera=self.is_valid(self.CP_txt.text())
        if bandera==True:
            codigopostal = int(self.CP_txt.text())
        else:
            self.IDsprovedor.setText('CODIGO POSTAL INVALIDO')
            codigopostal=0
        estado=self.estado_txt.text().upper() 
        if (marca != ''    and exterior > 0 and calle != '' and telefono != '' and estado !='' and codigopostal > 0):
            validacion=self.base_datos.busquedaDuplicidadProve(IDprovedor)
            self.IDsprovedor.setText('PROVEDOR PREVIAMENTE REGISTRADO')
            if(validacion==True):
                self.base_datos.altaProvedor(IDprovedor,marca,telefono,calle,exterior,codigopostal,estado)
                self.IDsprovedor.setText('PROVEDOR REGISTRADO CON ID '+IDprovedor)
                self.ID_provedor_.setText(IDprovedor)
        else:
            self.IDsprovedor.setText('ESPACIOS VACIOS O INVALIDOS')

    def registrar_CLIENTE(self):#registrar provedor
        nombre = self.nombre.text().upper() 
        peterno = self.paterno.text().upper() 
        materno = self.materno.text().upper() 
        bandera = self.is_valid(self.atiende.text())
        if bandera==True:
            Patiende = (self.atiende.text())
        
        email=self.email.text().upper()
        bandera = self.is_valid(self.telefono.text())
        if bandera==True:
            telefono = (self.telefono.text())
        calle = self.calle.text().upper() 
        bandera = self.is_valid(self.nume.text())
        if bandera==True:
            nume = int(self.nume.text())
        else:
            nume=0
        bandera = self.is_valid(self.cp.text())
        if bandera==True:
            cp = int(self.cp.text())
        else:
            cp=0
        estado=self.estado.text().upper()
        if ( nombre != '' and self.atiende.text() != ''and peterno != ''and materno != ''and email != ''   and nume > 0 and calle != '' and telefono != '' and estado !='' and cp > 0):
            validacion=self.base_datos. busquedaDuplicidadCliente(telefono)
           
            if(validacion==True):
                validacion=self.base_datos.busquedaDuplicidad(Patiende)
                if validacion==False:
                    self.base_datos.altaCliente(nombre,peterno,materno,Patiende,email,telefono,nume,calle,estado,cp)
                    self.avisar.setText('REGISTRADO')
                    var=self.base_datos.devolver(telefono)
                    self.avisar.setText(str(var[0]))

                else:
                    self.avisar.setText('CLAVE DE VENDEDOR INVALIDA')
            else:
                self.avisar.setText('CLIENTE PREVIAMENTE REGISTRADO O CLAVE DE VENDEDOR INVALIDA')
        
        else:
            self.avisar.setText('ESPACIOS VACIOS O INVALIDOS')
        self.nombre.clear()
        self.paterno.clear()
        self.materno.clear()
        self.atiende.clear()
        self.email.clear()
        self.telefono.clear()
        self.calle.clear()
        self.nume.clear()
        self.cp.clear()
        self.estado.clear()





    def LimpiarProvedor(self):
        self.marcatxt.clear()
        self.telefonotxt_.clear()
        self.marcatxt.clear() 
        self.ID_provedor_.clear()
        self.calle_txt.clear()
        self.exteriortxt_.clear()
        self.CP_txt.clear()
        self.estado_txt.clear() 
        self.IDsprovedor.clear()

    def ingresarMercancia(self):
        if(self.id.text()!='' and self.barras.text() !=''  and  self.cantidad_.text()!=''):
                verifica=self.is_valid(self.barras.text())
                if verifica==True:
                    barras=int(self.barras.text())  
                    verifica=self.is_valid(self.cantidad_.text())
                    if verifica ==True:
                            cantidad=int(self.cantidad_.text())
                            if cantidad > 0:
                                verifica=self.base_datos.busquedaDuplicidadProveYrefa(self.id.text(),barras)
                                if verifica==False:
                                    self.base_datos.UPDATESurte(barras,cantidad)
                                    self.info.setText('REFACCIONES INGRESADAS')
                                else:
                                    self.info.setText('CODIGO DE BARRAS NO COINCIDE CON ID DE PROVEDOR')
                            else:   
                                self.info.setText('INGRESE UNA CANTIDAD VALIDAD DE REFACCIONES')
        else:
            self.info.setText('ESPACIOS VACIOS')

  
    def verificarUsuario(self):
        if self.X.text() !='':
            valido=self.is_valid(self.X.text())
            if valido==True:
                numerocliente=int(self.X.text())
                var=self.base_datos.buscarCliente(numerocliente)
                if var!=None:
                   self.NUMFACTURA= self.base_datos.crearfactura(numerocliente)
                   self.Nombre.setText(str(var[0]))
                   self.Apellido.setText(str(var[1]))
                   self.Materno.setText(str(var[2]))
                else:
                    self.Nombre.setText("NO ENCONTRADO")

    def agregar(self):
        barras=self.act_buscar.text()
        self.base_datos.bsuca(self.NUMFACTURA[0],barras)
        datos=self.base_datos.mostrarM(self.NUMFACTURA[0])
        #self.mostraTabla_productos(datos)
        self.tableWidget.setRowCount(len(datos))
        if len(datos) == 0:
            self.aviso.setText(' NO EXISTE')       
        else:
            self.aviso.setText('PRODUCTO ENCONTRADO')
        i = len(datos)
        self.tableWidget.setRowCount(i)
        tablerow = 0
        for row in datos:
            self.Id = row[0]
            columna1=QtWidgets.QTableWidgetItem(str(row[0]))
            columna3=QtWidgets.QTableWidgetItem(str(row[1]))
            columna4=QtWidgets.QTableWidgetItem(str(row[2]))
            self.tableWidget.setItem(tablerow,0,columna1)
            self.tableWidget.setItem(tablerow,3,columna3)
            self.tableWidget.setItem(tablerow,4,columna4)
            tablerow +=1




               








                              
        
        



if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = VentanaPrincipal()
     mi_app.show()
     sys.exit(app.exec_())  

