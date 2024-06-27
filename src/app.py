from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_HOST']= 'localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='empleados'

mysql.init_app(app)
#con un decorador
#en la ruta raiz, cuando accedemos a localhost:5000
#vamos a definir una funcion 
@app.route('/')

#----------
# #empieza función index()
def index():
    sql= "Insert into empleados (nombre, correo, foto)  values ('Juan', 'juan@email.com','fotojuan.jpg');" 
    #guardo string en variable sql

    #conexión a la db
    conn =mysql.connect()
    cursor= conn.cursor()
    #con el cursor me deja ejecutar query de la variable sql
    cursor.execute(sql)
    #envio petición
    conn.commit()
    #la funcion index() va a retornar un template html
    return render_template('empleados/index.html')

#termina funcion index()
#----------

if __name__ == '__main__':
    app.run(debug=True)
