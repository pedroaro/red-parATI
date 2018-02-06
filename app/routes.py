from flask import Flask, render_template, request
from pymongo import *
from app import app_flask
from bson.json_util import dumps
from flask_mail import Mail, Message

#Conexión a MongoDB usando PyMongo
client = MongoClient()
db = client.redparATI_db
users = db.Usuario

#Configuracion para el servicio de mailing
app_flask.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'redparati.noreply@gmail.com',
	MAIL_PASSWORD = 'redparati2017'
	)

mail = Mail(app_flask)

#Verificador de sesión global
sesion_state = 1
usuario_email = ""
# Desvio de Cierre de Sesión

#Ruta para el envio de mail
@app_flask.route('/recuperar_password', methods=['POST'])
def send_mail():
	# Se toma el correo suministrado del formulario
	correo = request.form['correo_recuperar']

	# Se verifica que el correo suministrado pertenezca a un usuario registrado en BD
	query_existe = users.find_one( { "email": correo } )
	cant = users.find( { "email": correo } ).count()

	# Si existe un usuario registrado con ese correo
	if cant >= 1:
		# Enviar correo Message(Titulo, Emisor, Receptores)
		msg = Message("RedparATI | Solicitud de recuperación de contraseña",
		  sender="redparati.noreply@gmail.com",
		  recipients=[correo])
		# Cuerpo del mensaje -> Aquí insertamos los datos: correo y contraseña
		msg.body = "¡Bienvenido a redparATI!\n\n" + "Se ha solicitado una recuperación de contraseña\n\n" + "Sus credenciales son:\n" + "Correo: " + correo + "\nContraseña: " + query_existe['password'] + "\n\n¡Muchas gracias por utilizar nuestro sistema de recuperación de contraseña!" + "\n\n\nRedparATI - Support Team"         
		mail.send(msg)
		# Se devuelve un mensaje de feedback exitoso, y se envía el correo
		return "Sus datos han sido enviados. Por favor verifique su correo electrónico."
	else:
		# Si no existe el usuario, mostrar mensaje de error
		return "El correo suministrado es inválido. Intente nuevamente."

#Ruta para cerrar sesión
@app_flask.route("/loginOut")
def loginOut():
	global sesion_state
	sesion_state = 1
	return render_template("login.html")

@app_flask.route('/login', methods=['POST'])
def login_after_register():
	# Tomo los valores que se suministraron en "Registrar" y valido si ya se encuentra un usuario o e-mail igual en base de datos
	usuario = request.form['usuario_reg']
	nombre = request.form['nombre_reg']
	correo = request.form['correo_reg']
	password = request.form['password_reg']

	# Buscamos alguna similitud en base de datos, con user_name
	query_existe = users.find( { "user_name": usuario } ).count()

	# Si query_existe >= 1, quiere decir que ya hay un usuario con el mismo user_name
	if query_existe >= 1:
		return render_template("login.html", failed=1, message="Ya existe un usuario registrado con el nombre de usuario.")
	else:
		# Buscamos alguna similitud en base de datos, con email
		query_existe = users.find( { "email": correo } ).count()

		# Si query_existe >= 1, quiere decir que ya hay un usuario con el mismo email
		if query_existe >= 1:
			return render_template("login.html", failed=1, message="Ya existe un usuario registrado con el correo suministrado")
		else:
			# Al no encontrar similitudes, podemos registrar al usuario agregando sus datos a base de datos
			users.insert_one( { "user_name": usuario, "password": password, "email": correo, "nombre": nombre, "apellido": "n/a", "descripcion": "n/a", "color": "n/a", "libro": "n/a", "musica": "n/a", "video_juego": "n/a", "lenguajes": "n/a", "genero": "n/a", "fecha_nacimiento": "n/a", "ruta_foto_perfil": "n/a", "telefono": "n/a", "facebook": "n/a", "twitter": "n/a", "activa": "n/a", "amigos":["n/a"] } )

			# Regresamos a la pantalla de login
			return render_template("login.html")

@app_flask.route('/index', methods=['POST'])
def index():
	global usuario_email
	# Se solicita el verificador de sesión para su modificación
	global sesion_state

	if sesion_state == 1:
		#Se cambia el estado de la sesión.
		
		sesion_state = 0

		# Verificación de los datos ingresados en login
		# Tomo los valores suministrados en el login y procedemos a hacer las verificaciones para permitir o no el acceso
		usuario_email = request.form['usu_mail_login']
		password = request.form['password_login']

		# Buscamos alguna similitud en base de datos, con user_name o correo
		query_existe1 = users.find_one( { "user_name": usuario_email } )
		cant1 = users.find( { "user_name": usuario_email } ).count()
		query_existe2 = users.find_one( { "email": usuario_email } )
		cant2 = users.find( { "email": usuario_email } ).count()

		# Si no se consigue ningún usuario, sea por user_name o por email
		if cant1 < 1 and cant2 < 1:
			return render_template("login.html", failed=1, message="El usuario o e-mail suministrado no es correcto. Intente nuevamente.")
		else:
			# Si se encuentra una coincidencia por user_name, se verifica si la contraseña coincide con los datos en BD
			if cant1 >= 1:
				if query_existe1['password'] == password:
					return render_template("index.html")
				else:
					return render_template("login.html", failed=1, message="La contraseña es incorrecta. Intente nuevamente.")
			else:
				# Si se encuentra una coincidencia por correo, se verifica si la contraseña coincide con los datos en BD
				if cant2 >= 1:
					if query_existe2['password'] == password:
						
						return render_template("index.html")
					else:
						return render_template("login.html", failed=1, message="La contraseña es incorrecta. Intente nuevamente.")
				else:
					return render_template("login.html", failed=1, message="La contraseña es incorrecta. Intente nuevamente.")
	else:
		#En caso de sesión ya iniciada, se permite ir al index
		return render_template("index.html")

# FUNCIONES DE VERIFICACIÓN DE SESIÓN
@app_flask.route("/login")
def login_prepost():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("index.html")

@app_flask.route('/')
def login():
	# Primera pantalla que se muestra al ingresar a la página -> Login del usuario
	# Se verifica la sesión
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("index.html")

# Pantalla principal al iniciar sesión
@app_flask.route("/index")
def post_index():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("index.html")

# Perfil de Usuario
@app_flask.route("/perfil")
def perfil():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("perfil.html")

# Solicitudes y lista de amigos
@app_flask.route("/amigos")
def amigos():
	usuario_auth = users.find_one( { "email" : usuario_email } )
	nombre = usuario_auth["nombre"]

	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("amigos.html", nombre = nombre)

# Página de búsqueda de amigos
@app_flask.route("/buscar")
def buscar():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("buscar.html")

@app_flask.route("/chat")
def chat():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("chat.html")

@app_flask.route("/configuracion")
def config():
	usuario_auth = users.find_one( { "email" : usuario_email } )
	nombre = usuario_auth["nombre"]

	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("configuracion.html", nombre = nombre)

@app_flask.route("/fotos")
def fotos():
	usuario_auth = users.find_one( { "email" : usuario_email } )
	nombre = usuario_auth["nombre"]
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("fotos.html", nombre = nombre)

@app_flask.route("/notificaciones")
def notify():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("notificaciones.html")

@app_flask.route("/personalizar")
def customize_show():
	#Se obtienen de la base de datos los valores que se van a mostrar
	usuario_auth = users.find_one( { "email" : usuario_email } )
	nombre = usuario_auth["nombre"]
	apellido = usuario_auth["apellido"]
	descripcion = usuario_auth["descripcion"]
	libro = usuario_auth["libro"]
	musica = usuario_auth["musica"]
	video_juego = usuario_auth["video_juego"]
	fecha_nacimiento = usuario_auth["fecha_nacimiento"]
	telefono = usuario_auth["telefono"]
	genero = usuario_auth["genero"]
	email = usuario_email

	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("personalizar.html", nombre = nombre, email = email, apellido = apellido, descripcion = descripcion, libro = libro, musica = musica, video_juego = video_juego, fecha_nacimiento = fecha_nacimiento, telefono = telefono, genero = genero)


@app_flask.route("/personalizar", methods=["POST"])
def customize_update():
	#Se realiza la búsqueda por el email del usuario
	usuario_auth = users.find_one( { "email" : usuario_email } )
	#Luego se buscan los campos que ya deben estar predefinidos en la template de personalizacion
	nombre = usuario_auth["nombre"]
	email = usuario_email

	#Se hace request de los campos que se van a actualizar desde la form de personalizacion
	nombre = request.form['nombre']
	apellido = request.form['apellido']
	descripcion = request.form['descripcion']
	libro = request.form['libro']
	musica = request.form['musica']
	video_juego = request.form['video_juego']
	fecha_nacimiento = request.form['fecha_nacimiento']
	telefono = request.form['telefono']
	genero = request.form['genero']
	email = request.form['email']
	
	#Se actualizan los campos 
	users.update_one({"email":usuario_email}, {"$set":{"nombre":nombre}})
	users.update_one({"email":usuario_email}, {"$set":{"apellido":apellido}})
	users.update_one({"email":usuario_email}, {"$set":{"descripcion":descripcion}})
	users.update_one({"email":usuario_email}, {"$set":{"libro":libro}})
	users.update_one({"email":usuario_email}, {"$set":{"musica":musica}})
	users.update_one({"email":usuario_email}, {"$set":{"video_juego":video_juego}})
	users.update_one({"email":usuario_email}, {"$set":{"fecha_nacimiento":fecha_nacimiento}})
	users.update_one({"email":usuario_email}, {"$set":{"telefono":telefono}})
	users.update_one({"email":usuario_email}, {"$set":{"genero":genero}})
	users.update_one({"email":usuario_email}, {"$set":{"fecha_nacimiento":fecha_nacimiento}})
	users.update_one({"email":usuario_email}, {"$set":{"email": email}})

	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("personalizar.html", nombre = nombre, email = email, apellido = apellido, descripcion = descripcion, libro = libro, musica = musica, video_juego = video_juego, fecha_nacimiento = fecha_nacimiento, telefono = telefono, genero = genero)


@app_flask.route("/solicitud_amistad")
def friend_req():
	if sesion_state == 1:
		return render_template("login.html")
	else:
		return render_template("solicitud_amistad.html")

#{{ url_for('static', filename='js/
	