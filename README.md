# red-parATI
Control de versiones dered-parATI

# Instrucciones para montar
    Activar el ambiete virtual (en una terminal):
        source virtualizacion/bin/activate

    Requisitos (para instalar, por si falta: pip3 install <paquete>):
        1.- Flask (debería de estar ya) (paquete: flask)
        2.- Pymongo (debería de estar ya) (paquete: pymongo)
        3.- MongoDB (debe ser instalado y configurado en la PC)

    MONGO (en otra terminal):
        Instalar mongo:
            https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
            
        Activar mongo (en otra terminal):
            mongod
            NO CERRAR

        Configurar mongo (en otra terminal):
            mongo
            use redparATI_db
            db.createCollection("Usuario", { capped: false })
            NO CERRAR
    
    Activar server (estando en el ambiente virtual):
        export FLASK_APP=redparATI.py
        flask run
    
    Debería de funcionar al pelo.
