import mysql.connector
from mysql.connector import errorcode
import verifica


class DBConn:

    

    def __init__(self, db_host='localhost', db_user='darwin', db_pass='gmd123456',
                 db_name='test'):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
    try:
       

        def conectar(self):
            """Crear una conexión con la base de datos"""
            #mysql.connector.connect
      


            self.db = mysql.connector.connect(host=self.db_host, user=self.db_user,
                                  passwd=self.db_pass, db=self.db_name)

            print("**************************************************")

             
        def abrir_cursor(self):
            """Abrir un cursor"""
            self.cursor = self.db.cursor()
            print(self.cursor)

        def ejecutar_consulta(self, query, values=''):
            if values != '':
                self.cursor.execute(query, values)
           

            else:
            
                self.cursor.execute(query)

        def traer_datos(self, query):
            """Traer todos los registros"""

        
            sql = query.lower()
            es_select = sql.count('select')
            if es_select < 1:
           
                self.rows = self.cursor.rowcount
            else:
           
                self.rows = self.cursor.fetchall()
        
           
           

        def send_commit(self, query):
            """Enviar commit a la base de datos"""
            sql = query.lower()
            es_lectura = sql.count('select')
            if es_lectura < 1:
                self.db.commit()

        def cerrar_cursor(self):
            """Cerrar cursor"""
            self.cursor.close()

        def ejecutar(self, query, values=''):
            """Compilar todos los procesos"""
            # ejecuta todo el proceso solo si las propiedades han sido definidas
            if verifica.inicio():
               
                if (self.db_host and self.db_user and self.db_pass and self.db_name and  query ):
                   
                    self.conectar()
                    self.abrir_cursor()
            
                    self.ejecutar_consulta(query, values)
            
                    self.send_commit(query)
            
                    self.traer_datos(query)
            
                    self.cerrar_cursor()
                    
                    return self.rows
            else:
                print("****************no se pudo conectar base datos *******************")
                return []
        

    except mysql.connector.Error as err:

            
            
            
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(err)
            print("Su nombre de usuarios o password es incorrecto")
        elif err.errno== errorcode.ER_BAD_DB_ERROR:
            print(err)
            print("Base de Datos no existe")
        else: 
            print(err)
              
        

   
