import pymysql
from conexion import Conexion
from sqlalchemy import create_engine
from json import dumps
cx = Conexion()

class Cliente:
    idcliente = 0
    nomcliente = ""
    apellido = ""
    dni = ""
    correo=""
    direccion=""
    telefono=""
    def readAll(self):
        try:
            conexion=cx.conecta()
            cursor = conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('listar_cliente')
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            conexion.close()
    def delete(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('delete_cliente',[self.idcliente])
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def agregarcliente(self):
        nomcliente = self.agregarcliente
        apellido = self.apellido
        dni = self.dni
        correo=self.correo
        direccion=self.direccion
        telefono=self.telefono
        data=[nomcliente,apellido,dni,correo,direccion,telefono]
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("create_cliente",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def buscarcliente(self):
        try:
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc('read_cliente',[self.idcliente,])
            rows=cursor.fetchall()
            return rows
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    def modificarcliente(self):
        try:
            idcliente = self.idcliente
            nomcliente = self.agregarcliente
            apellido = self.apellido
            dni = self.dni
            correo=self.correo
            direccion=self.direccion
            telefono=self.telefono
            data=[idcliente,nomcliente,apellido,dni,correo,direccion,telefono]
            conexion=cx.conecta()
            cursor=conexion.cursor(pymysql.cursors.DictCursor)
            cursor.callproc("update_cliente",data)
            conexion.commit()
            return 1
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()