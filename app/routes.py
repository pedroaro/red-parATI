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
    return render_template("login.html")

@app_flask.route('/login', methods=['POST'])
def login_after_register():
	usuario = request.form['usuario_reg']
	nombre = request.form['nombre_reg']
	correo = request.form['correo_reg']
	password = request.form['password_reg']

	db.Usuario.insert_one( { "user_name": usuario, "password": password, "email": correo, "nombre": nombre, "descripcion": "n/a", "color": "n/a", "libro": "n/a", "musica": "n/a", "video_juego": "n/a", "lenguajes": "n/a", "genero": "n/a", "ci": "n/a", "fecha_nacimiento": "n/a", "ruta_foto_perfil": "n/a", "telefono": "n/a", "facebook": "n/a", "twitter": "n/a", "activa": "n/a" } )

	return render_template("login.html")

@app_flask.route('/index')
def index():
	return render_template("index.html")