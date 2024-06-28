from flask import Flask
from flask import render_template
from flask import request #para metodo POST
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='empleados'

mysql.init_app(app)


#----------

@app.route('/') #metodo get[] cuando accedemos a localhost:5000
#empieza función index()
def index():
    #conexion
    conn =mysql.connect()
    cursor = conn.cursor()
    #guardo string en variable sql
    sql= "SELECT * FROM empleados;" 
    #con el cursor me deja ejecutar query de la variable sql
    cursor.execute(sql)
    #guardo resultado de la consulta en la variable
    empleados=cursor.fetchall() #la variable empleados se convertira en tupa
    print('.................tupla empleados...............')
    print(empleados)
    #envio petición
    conn.commit()
    #la funcion index() va a retornar un template html + la tupla
    return render_template('empleados/index.html', empleados=empleados)

#termina funcion index()
#----------

@app.route('/create') #metodo get[]
#----------
# #empieza función create()
def create():
  
    return render_template('empleados/create.html')

#termina funcion create()
#----------

#indico que es metodo post
@app.route('/store', methods=['POST'])
#----------
#empieza función store()
def store():
    #guardo los datos del formulario
    _nombre=request.form['txtNombre']
    _correo=request.form['txtCorreo']
    _foto=request.files['txtFoto']


     #guardo string en variable sql. Los '%s' son espacios que me permeten agregar valores mas adelante
    sql= "Insert into empleados (nombre, correo, foto)  values (%s, %s, %s);" 
    #creo tupla
    datos= (_nombre, _correo, _foto.filename)

    #conexion
    conn =mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    #inserto, el valor de variables, en la base de datos
    conn.commit()
    return render_template('/')
#termina funcion store()
#----------

if __name__ == '__main__':
    app.run(debug=True)
 
