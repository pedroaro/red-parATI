from flask import Flask, render_template, request
from pymongo import *
from app import app_flask
from bson.json_util import dumps

#Hace falta realizar la logica de obtener los datos del formulario
#y permitir el acceso a index desde login, también la de registro.
#En general, hace falta toda la logica de analisis de datos y la
#parte de la base de datos.

#Conexión a MongoDB usando PyMongo
client = MongoClient()
db = client.redparATI_db

@app_flask.route('/')
def login():
	# Primera pantalla que se muestra al ingresar a la página -> Login del usuario
    return render_template("login.html")

@app_flask.route('/login', methods=['POST'])
def login_after_register():
	# Tomo los valores que se suministraron en "Registrar" y valido si ya se encuentra un usuario o e-mail igual en base de datos
	usuario = request.form['usuario_reg']
	nombre = request.form['nombre_reg']
	correo = request.form['correo_reg']
	password = request.form['password_reg']

	# Buscamos alguna similitud en base de datos, con user_name
	query_existe = db.Usuario.find( { "user_name": usuario } ).count()

	# Si query_existe >= 1, quiere decir que ya hay un usuario con el mismo user_name
	if query_existe >= 1:
		return "Ya existe un usuario registrado con el nombre de usuario o correo suministrado, intente nuevamente."
	else:
		# Buscamos alguna similitud en base de datos, con email
		query_existe = db.Usuario.find( { "email": correo } ).count()

		# Si query_existe >= 1, quiere decir que ya hay un usuario con el mismo email
		if query_existe >= 1:
			return "Ya existe un usuario registrado con el nombre de usuario o correo suministrado, intente nuevamente."
		else:
			# Al no encontrar similitudes, podemos registrar al usuario agregando sus datos a base de datos
			db.Usuario.insert_one( { "user_name": usuario, "password": password, "email": correo, "nombre": nombre, "descripcion": "n/a", "color": "n/a", "libro": "n/a", "musica": "n/a", "video_juego": "n/a", "lenguajes": "n/a", "genero": "n/a", "ci": "n/a", "fecha_nacimiento": "n/a", "ruta_foto_perfil": "n/a", "telefono": "n/a", "facebook": "n/a", "twitter": "n/a", "activa": "n/a" } )

			# Regresamos a la pantalla de login
			return render_template("login.html")

@app_flask.route('/index', methods=['POST'])
def index():
	# Verificación de los datos ingresados en login
	# Tomo los valores suministrados en el login y procedemos a hacer las verificaciones para permitir o no el acceso
	usuario_email = request.form['usu_mail_login']
	password = request.form['password_login']

	# Buscamos alguna similitud en base de datos, con user_name o correo
	query_existe1 = db.Usuario.find_one( { "user_name": usuario_email } )
	cant1 = db.Usuario.find( { "user_name": usuario_email } ).count()
	query_existe2 = db.Usuario.find_one( { "email": usuario_email } )
	cant2 = db.Usuario.find( { "email": usuario_email } ).count()

	# Si no se consigue ningún usuario, sea por user_name o por email
	if cant1 < 1 and cant2 < 1:
		return "El usuario o e-mail suministrado no es correcto. Intente nuevamente."
	else:
		# Si se encuentra una coincidencia por user_name, se verifica si la contraseña coincide con los datos en BD
		if cant1 >= 1:
			if query_existe1['password'] == password:
				return render_template("index.html")
			else:
				return "La contraseña es incorrecta. Intente nuevamente."
		else:
			# Si se encuentra una coincidencia por correo, se verifica si la contraseña coincide con los datos en BD
			if cant2 >= 1:
				if query_existe2['password'] == password:
					return render_template("index.html")
				else:
					return "La contraseña es incorrecta. Intente nuevamente."
			else:
				return "La contraseña es incorrecta. Intente nuevamente."