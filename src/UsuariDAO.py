import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import decoder
cx=Conexion()

class Usuario:
    idusuario = 0
    nomuser = ""
    clave = ""
    estado = ""
    def readAll(self):
        try:
            sql = "select * from USUARIO"
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            '''lista = cursor.fetchall()'''
            for row in cursor:
                return row
        finally:
            conexion.close()


obj = Usuario()
print(obj.readAll())