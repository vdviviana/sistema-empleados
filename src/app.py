
#from significa que llamo al modulo o librerias flask
from flask import Flask #importo la clase Flask
from flask import render_template # importo el metodo o funcion render_template
from flaskext.mysql import MySQL #importo la clase MySQL

#vamos a instanciar las clases
app = Flask(__name__) #name es palabra reservada de Flask
mysql = MySQL()

if __name__ == 'main':
    app.run(debug=True) #nos muestra errores por consola*
    #ejecuto app #correr flask

