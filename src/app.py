from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from json import dumps
from UsuariDAO import Usuario
from ProductoDao import Producto
from ClienteDao import Cliente
user = Usuario()
producto = Producto()
cliente = Cliente()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def listar():
    return jsonify({'mensaje': 'Bienvenidos a Flask'})

#-----------------------metodos para usuario--------------------------#
@app.route('/usuario/listar', methods=['GET'])
def users():
    try:
        rows = user.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)


@app.route('/usuario/buscar/<int:id>')
def buscarusuario(id):
	try:
		user.idusuario = id
		row = user.buscarusuario()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)


@app.route('/usuario/create', methods=['POST'])
def agregarusuario():
    try:
        _json = request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        print(user.clave,user.nomuser)
        if request.method=='POST':
            resp=user.agregarusuario()
            resp=jsonify('USUARIO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/usuario/eliminar/<int:id>', methods=['GET'])
def eliminarusuario(id):
    try:
        user.idusuario=id
        resp=user.delete()
        resp=jsonify('Usuario Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)    
@app.route('/usuario/modificar', methods=['PUT'])
def modificarusuario():
    try:
        _json=request.json
        user.nomuser=_json['nomuser']
        user.clave=_json['pass']
        user.idusuario=_json['iduser']
        if request.method == 'PUT':
            resp = user.modificarusuario()
            resp = jsonify('Usuario Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

#-----------------------metodos para producto--------------------------#

@app.route('/producto/listar', methods=['GET'])
def productos():
    try:
        rows = producto.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/producto/buscar/<int:id>')
def buscarescuela(id):
	try:
		producto.idproducto = id
		row = producto.buscarproductos()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/producto/create', methods=['POST'])
def agregarproducto():
    try:
        _json = request.json
        producto.nomproducto=_json['nomproducto']
        producto.precio=_json['precio']
        producto.cantidad=_json['cantidad']
        if request.method=='POST':
            resp=producto.agregarproducto()
            resp=jsonify('PRODUCTO')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)
@app.route('/producto/eliminar/<int:id>', methods=['GET'])
def eliminarproducto(id):
    try:
        producto.idproducto=id
        resp=producto.delete()
        resp=jsonify('Producto Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)  

@app.route('/producto/modificar', methods=['PUT'])
def modificarproducto():
    try:
        _json=request.json
        producto.precio=_json['precio']
        producto.cantidad=_json['cantidad']
        producto.nomproducto=_json['nomproduc']
        producto.idproducto=_json['idproduc']
        if request.method == 'PUT':
            resp = producto.modificarproducto()
            resp = jsonify('Usuario Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

#-----------------------metodos para cliente--------------------------#
@app.route('/cliente/listar', methods=['GET'])
def clientes():
    try:
        rows = cliente.readAll()
        respuesta = jsonify(rows)
        respuesta.status_code = 200
        return respuesta
    except Exception as e:
        print(e)

@app.route('/cliente/buscar/<int:id>')
def buscarclient(id):
	try:
		cliente.idcliente = id
		row = cliente.buscarcliente()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

@app.route('/cliente/create', methods=['POST'])
def agregarcliente():
    try:
        _json = request.json
        cliente.nomcliente=_json['nomcliente']
        cliente.apellido=_json['apellido']
        cliente.dni=_json['dni']
        cliente.correo=_json['correo']
        cliente.direccion=_json['direccion']
        cliente.telefono=_json['telefono']
        if request.method=='POST':
            resp=cliente.agregarcliente()
            resp=jsonify('CLIENTE')
            resp.status_code=200
        return resp
    except Exception as e:
        print(e)

@app.route('/cliente/modificar', methods=['PUT'])
def modificarcliente():
    try:
        _json=request.json
        cliente.nomcliente=_json['nomcliente']
        cliente.apellido=_json['apellido']
        cliente.dni=_json['dni']
        cliente.correo=_json['correo']
        cliente.direccion=_json['direccion']
        cliente.telefono=_json['telefono']
        cliente.idcliente=_json['idcliente']
        if request.method == 'PUT':
            resp = cliente.modificarcliente()
            resp = jsonify('Cliente Modificada')
            resp.status_code=200
            return resp
    except Exception as e:
        print(e)

@app.route('/cliente/eliminar/<int:id>', methods=['GET'])
def eliminarcliente(id):
    try:
        producto.idcliente=id
        resp=cliente.delete()
        resp=jsonify('Producto Elimindado')
        resp.status_code=200
        return resp
    except Exception as e:
        print(e)  

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)    