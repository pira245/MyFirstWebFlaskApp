# importamos las librerias de python y flask para crear la App
from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

# Creamos la aplicación con Flask
app = Flask(__name__)

# Creamos la ruta principal de la web -home (pagina de bienvenida)
@app.route('/')
def home():
    return render_template('cover/index.html')

# Creamos la ruta de la pagina para crear las tareas.
@app.route('/Inicio', methods=['POST'])
def iniciar():
    return render_template('index.html')

# Datos para crear la tabla de datos sobre las tareas.
headings = ('TAREA','FINALIZADA', 'FECHA DE CREACIÓN', 'FECHA DE ENTREGA')
@app.route('/gestor-de-tareas')
def gestor():
    results = db.session.query(Tarea).all()
    db.session.commit()
    return render_template('index.html', headings=headings, tareas=results)

# Ruta para la creación del objeto tarea
@app.route('/crear-tarea', methods=['POST'])
def crear():
    import datetime as dt
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False, fecha_creada=dt.datetime.today(), hora=dt.datetime.now(), fecha_entrega=dt.datetime.today())
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('gestor'))

# Ruta para eliminar una tarea de la base de datos
@app.route('/eliminar-tarea/<id>')
def eliminar(id):
     tarea = db.session.query(Tarea).filter_by(id=int(id)).delete()
     db.session.commit()
     return redirect(url_for('gestor'))

# Ruta para cambiar el estado de una tarea hecha o no
@app.route('/tarea-hecha/<id>')
def hecha(id):
     tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
     tarea.hecha= not(tarea.hecha)
     db.session.commit()
     return redirect(url_for('gestor'))

# Ruta para actualizar y cambiar los atributos de una tarea (contenido y fecha de entrega)
@app.route('/actualizar-tarea/<id>')
def actualizar_tarea(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    return render_template('actualizar_tarea.html', contenido=tarea.contenido, fecha=tarea.fecha_entrega, id=tarea.id)

@app.route('/actualizar-tarea-tarea/<id>', methods=['POST'])
def actualizar_tarea_(id):
    import datetime as dt
    nuevo_contenido = request.form['contenido']
    nueva_fecha_limite = request.form['fecha_entrega']
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    if nueva_fecha_limite == '':
        pass
    else:
        mm = nueva_fecha_limite[0:2]
        dd = nueva_fecha_limite[3:5]
        yyyy = nueva_fecha_limite[6:10]
        fecha = dt.date(int(yyyy), int(mm), int(dd))
        tarea.fecha_entrega = fecha

    if nuevo_contenido == '':
        pass
    else:
        tarea.contenido = nuevo_contenido
    db.session.commit()
    return redirect(url_for('gestor'))


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # creamos el modelo de datos
    app.run(debug=True)  # El debug =True hace que cada vez que reiniciemos el servidor o odifiquemos codigo,
    # el servidor se reinicie solo
