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
        self.bt_refrescar.clicked.connect(self.mostrar_productos)
        self.bt_agregar.clicked.connect(self.registrar_productos)
        self.bt_borrar.clicked.connect(self.eliminar_productos)
        self.bt_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar) 
        self.btregistra.clicked.connect(self.registrar_provedor) 
        self.btnLimpiarProvedor.clicked.connect(self.LimpiarProvedor) 
        self.reg_refaccion_p.clicked.connect(self.registrar_Refaccion) 
        self.btnBuscar.clicked.connect(self.buscar_p)
        self.radioButton.clicked.connect(self.buscar_po)
        self.btneliminar.clicked.connect(self.eliminar_refaccion)
        self.bt_actualiza_buscar.clicked.connect(self.actualiza)
        self.bt_12.clicked.connect(self.modificar_productosss)
        self.ingreso.clicked.connect(self.buscarp)
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)     
        self.bt_restaurar.clicked.connect(self.control_bt_normal)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
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
 

    # Configuracion Pagina Base de datos
    def mostrar_productos(self): 
        

       

        datos = self.base_datos.mostrar()
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
            self.signal_actualizar.setText("") 
            self.signal_registrar.setText("") 
            self.signal_eliminacion.setText("") 

    def registrar_productos(self):#registrar vendedor
        if (len(self.txtcp.text())==0  and len(self.txtexterior.text())==0  and len(self.txtsalario.text())==0  and len(self.txtnombre.text())==0 and len(self.txtpaterno.text())==0 and len(self.txtmaterno.text())==0 and len(self.txtcalle.text())==0 and len(self.txttelefono.text())==0 and len(self.txtestado.text())==0):
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
                self.txtnombre.clear()
                self.txtpaterno.clear()
                self.txtmaterno.clear()
                self.txtsalario.clear()
                self.txtexterior.clear()
                self.txtcalle.clear()
                self.txttelefono.clear()
                self.txtestado.clear()
                self.txtcp.clear()
                self.signal_registrar.setText('Productos Registrados')
            else:
                self.signal_registrar.setText('Hay Espacios Vacios o incorrectos')

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

    def registrar_provedor(self):#registrar vendedor
        marca = self.marcatxt.text().upper() 
        telefono = self.telefonotxt_.text().upper() 
        IDprovedor = self.telefonotxt_.text().upper()+self.marcatxt.text().upper() 
        calle = self.calle_txt.text().upper()
        bandera=self.is_valid(self.exteriortxt_.text())
        if bandera==True:
            exterior = int(self.exteriortxt_.text())
        else:
            exterior=0
        bandera=self.is_valid(self.CP_txt.text())
        if bandera==True:
            codigopostal = int(self.CP_txt.text())
        else:
            codigopostal=0
        estado=self.estado_txt.text().upper() 
        if (marca != ''    and exterior > 0 and calle != '' and telefono != '' and estado !='' and codigopostal > 0):
            validacion=self.base_datos.busquedaDuplicidadP(IDprovedor)
            if(validacion==True):
                self.base_datos.altaProvedor(IDprovedor,marca,telefono,calle,exterior,codigopostal,estado)
                self.IDsprovedor.setText('Provedor Registrado con ID '+IDprovedor)
                self.ID_provedor_.setText(IDprovedor)
            
        else:
            self.IDsprovedor.setText('Hay Espacios Vacios o incorrectos')
    def registrar_Refaccion(self):#registrar vendedor
        bandera=self.is_valid(self.CBtxt.text())
        if bandera==True:
            codigoBarras=int(self.CBtxt.text())
        else:
            codigoBarras=0
        codigoProducto = self.codigoProduct.text().upper() 
        categoria = self.categoriatxtregistrorefa.text().upper() 
        bandera=self.is_valid(self.precioProvedor.text())
        if bandera==True:
            PrecioProvedor=int(self.precioProvedor.text())
        else:
            PrecioProvedor=0
        bandera=self.is_valid(self.precioPublic.text())
        if bandera==True:
            PrecioPublico=int(self.precioPublic.text())
        else:
            PrecioPublico=0
        bandera=self.is_valid(self.precioPublic.text())
        if bandera==True:
            UnidadesRecibidas=int(self.UnidadesRecibidas.text())
        else:
            UnidadesRecibidas=0        
        descripcion = self.descripcion_txt_.text().upper() 
        if descripcion != '' and codigoProducto != ''    and categoria != '' and PrecioProvedor > 0 and PrecioPublico > 0 and UnidadesRecibidas > -1 and codigoBarras > 0:
            validacion=self.base_datos.busquedaDuplicidad_P(codigoProducto)
            if validacion==True:
                    self.base_datos.altaRefaccion(codigoBarras,codigoProducto,categoria,PrecioProvedor,PrecioPublico,UnidadesRecibidas,descripcion)
                    self.avisoregistro.setText('Refaccion Registrada')
                    self.CBtxt.clear()
                    self.codigoProduct.clear()
                    self.categoriatxtregistrorefa.clear()
                    self.precioProvedor.clear()
                    self.precioPublic.clear()
                    self.UnidadesRecibidas.clear()
                    self.descripcion_txt_.clear()
        else:
            self.IDsprovedor.setText('Hay Espacios Vacios o incorrectos')

    def is_valid(self,cadena):
            longitud=len(cadena)
            contador=0
            for validar in cadena:
                if validar.isdigit():
                    contador=contador+1
            if(contador==longitud and cadena!=''):
                return True
            return False
        

        #valor=self.base_datos.busquedaDuplicidad(str(cadena))



    def buscar_p(self):
        nombre_producto = self.buscar.text()
        if len(nombre_producto)==0:
            return
        else:
            bandera=self.is_valid(nombre_producto)
            if(bandera==True):
                nombre_producto = str("'" + nombre_producto + "'")
                producto = self.base_datos.busca_productos(nombre_producto)
                self.tabla_productos.setRowCount(len(producto))
                if len(producto) == 0:
                    self.buscar.setText(' No Existe')       
                else:
                    self.buscar.setText('Producto Encontrado')
                tablerow = 0
                for row in producto:
                    self.producto_a_borrar = row[2]
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

    def buscarp(self):
        nombre_producto = self.buscar_2.text()
        if len(nombre_producto)==0:
            return
        else:
            bandera=self.is_valid(nombre_producto)
            if(bandera==True):
                nombre_producto = self.buscar_2.text()
                nombre_producto = str("'" + nombre_producto + "'")
                producto = self.base_datos.busca_productos(nombre_producto)
                self.total=self.total+producto[4]
                
                self.subtotal.setText(str(self.total))


               

    def finanzas(self):
            producto = self.base_datos.financiar()
            
    def actualiza(self):
        nombre_producto = self.act_buscar.text()
        if len(nombre_producto)==0:
            return
        else:
            bandera=self.is_valid(nombre_producto)
            if(bandera==True):
                nombre_producto = str("'" + nombre_producto + "'")
                producto = self.base_datos.busca_refaccioness(nombre_producto)
                self.tableWidget.setRowCount(len(producto))
                if len(producto) == 0:
                    self.signal_actualizar.setText(' No Existe')       
                else:
                    self.signal_actualizar.setText('Producto Encontrado')
                tablerow = 0
                for row in producto:
                    self.producto_a_borrar = row[2]
                    columna1=QtWidgets.QTableWidgetItem(str(row[0]))
                    columna3=QtWidgets.QTableWidgetItem(str(row[3]))
                    columna4=QtWidgets.QTableWidgetItem(str(row[4]))
                    columna5=QtWidgets.QTableWidgetItem(str(row[5]))
                    self.tableWidget.setItem(tablerow,0,columna1)
                    self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow,3,columna3)
                    self.tableWidget.setItem(tablerow,4,columna4)
                    self.tableWidget.setItem(tablerow,5,columna5)
                    self.tableWidget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
                    tablerow +=1

    def buscar_po(self):
        nombre_producto = '0'
        nombre_producto = str("'" + nombre_producto + "'")
        producto = self.base_datos.busca_refacciones()
        self.tabla_productos.setRowCount(len(producto))
        if len(producto) == 0:
            self.buscar.setText(' No Existe')       
        else:
            self.buscar.setText('Producto Encontrado')
        tablerow = 0
        for row in producto:
            self.producto_a_borrar = row[2]
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

    def modificar_productos(self):
        if self.producto != '':
            codigo = self.act_codigo.text().upper()  
            nombre = self.act_nombre.text().upper() 
            modelo = self.act_modelo.text().upper() 
            precio = self.act_precio.text().upper() 
            cantidad = self.act_cantidad.text().upper() 
            act = self.base_datos.actualiza_productos(self.Id, codigo, nombre, modelo, precio, cantidad)
            if act == 1:
                self.signal_actualizar.setText("ACTUALIZADO")                
                self.act_codigo.clear()
                self.act_nombre.clear()
                self.act_modelo.clear()
                self.act_precio.clear()                
                self.act_cantidad.clear()
                self.act_buscar.setText('')
            elif act == 0:
                self.signal_actualizar.setText("ERROR")
            else:
                self.signal_actualizar.setText("INCORRECTO")        

    def buscar_por_nombre_eliminar(self):
        nombre_producto = self.eliminar_buscar.text().upper()  
        nombre_producto = str("'" + nombre_producto + "'")
        producto = self.base_datos.busca_producto(nombre_producto)
        self.tabla_borrar.setRowCount(len(producto))
        if len(producto) == 0:
            self.signal_eliminacion.setText(' No Existe')       
        else:
            self.signal_eliminacion.setText('Producto Seleccionado')
        tablerow = 0
        for row in producto:
            self.producto_a_borrar = row[2]
            self.tabla_borrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_borrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_borrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_borrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_borrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1

    def eliminar_productos(self):
        self.row_flag = self.tabla_borrar.currentRow()
        if self.row_flag == 0:
            self.tabla_borrar.removeRow(0)
            self.base_datos.elimina_productos("'" + self.producto_a_borrar + "'")
            self.signal_eliminacion.setText('Producto Eliminado')
            self.eliminar_buscar.setText('')



    def eliminar_refaccion(self):
        nombre_producto = self.buscar.text()
        if len(nombre_producto)==0:
            return
        else:
            bandera=self.is_valid(nombre_producto)
            if(bandera==True):
                nombre_producto = str("'" + nombre_producto + "'")
                self.base_datos.elimina_productoss(nombre_producto)



    def modificar_productosss(self):
        if(self.act_codigo.text()!=''):
            bandera=self.is_valid(self.act_codigo.text())
            if(bandera==True):
                codigo = int(self.act_codigo.text())
                codigop = self.act_nombre.text().upper() 
                categoria = self.categoria.text().upper() 
                precio = int(self.act_precio.text())
                cantidad = int(self.act_cantidad.text())
                unidades = int(self.unidades_2.text())
                descripcion = self.descripcion.text().upper() 
                act = self.base_datos.actual(codigo,codigop,categoria,precio,cantidad,unidades,descripcion)
                self.act_codigo.clear()
                self.act_nombre.clear()
                self.categoria.clear()
                self.act_precio.clear()
                self.act_cantidad.clear()
                self.unidades_2.clear()
                self.descripcion.clear()
if __name__ == "__main__":
     app = QApplication(sys.argv)
     mi_app = VentanaPrincipal()
     mi_app.show()
     sys.exit(app.exec_())  

