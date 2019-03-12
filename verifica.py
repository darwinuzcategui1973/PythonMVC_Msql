import mysql.connector
from mysql.connector import errorcode




def inicio():

    try:
        cnx = mysql.connector.connect(user='darwin',password="gmd123456",database='test')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(err)
            print("Su nombre de usuarios o password es incorrecto")
            return False
        elif err.errno== errorcode.ER_BAD_DB_ERROR:
            print(err)
            print("Base de Datos no existe")
            return False
        else:
           
            print(err)
            return False
    else:
	    print("conexion exitosa")
	    cnx.close()
	    return True
