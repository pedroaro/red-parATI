from flask import Flask, render_template, request
from pymongo import *
from app import app_flask

#Hace falta realizar la logica de obtener los datos del formulario
#y permitir el acceso a index desde login, también la de registro.
#En general, hace falta toda la logica de analisis de datos y la
#parte de la base de datos.

#Conexión a MongoDB usando PyMongo
client = MongoClient()
db = client.redparATI_db

@app_flask.route('/')
def login():
	# Primera pantalla que se muestra al ingresar a la página
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

@app_flask.route('/index')
def index():
	return render_template("index.html")