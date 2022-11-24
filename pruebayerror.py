import psycopg2
connetion = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="2020",
            database="BdRefaccionaria_",
            port="5432"
        ) 
connetion.autocommit=True

def altaRefaccion():#registra a un empleado
        cursor=connetion.cursor()
        query= """ SELECT """
        cursor.execute(query)
        cursor.close()


