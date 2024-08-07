from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/efip3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '626c21c0dabcad24e1b2fff010c886d2'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

class Modelo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

class Fabricante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer, nullable=False)
    letra_almacen = db.Column(db.String(10), nullable=False)
    numero_almacen = db.Column(db.Integer, nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)

    # Relación inversa
    equipo = db.relationship('Equipo', backref=db.backref('stock', uselist=False))

class Accesorios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Car1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id', ondelete='CASCADE'), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    accesorios_id = db.Column(db.Integer, db.ForeignKey('accesorios.id'))
    caracteristicas_id = db.Column(db.Integer, db.ForeignKey('car1.id'))

    # Relaciones
    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('equipos', lazy=True))
    proveedor = db.relationship('Proveedor', backref=db.backref('equipos', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True, passive_deletes=True))
    accesorios = db.relationship('Accesorios', backref=db.backref('equipos', lazy=True))
    caracteristicas = db.relationship('Car1', backref=db.backref('equipos', lazy=True))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/marcas', methods=['GET', 'POST'])
def marcas():
    if request.method == 'POST':
        nombre = request.form['nombre']
        if nombre:
            nueva_marca = Marca(nombre=nombre)
            db.session.add(nueva_marca)
            db.session.commit()
            flash('Marca agregada con éxito.', 'success')
            return redirect(url_for('marcas'))

    marcas = Marca.query.all()
    return render_template('marcas.html', marcas=marcas)

@app.route('/editar_marca/<int:id>', methods=['GET', 'POST'])
def editar_marca(id):
    marca = Marca.query.get_or_404(id)
    
    if request.method == 'POST':
        marca.nombre = request.form.get('nombre')
        db.session.commit()
        flash('Marca actualizada exitosamente!')
        return redirect(url_for('marcas'))

    return render_template('editar_marca.html', marca=marca)

@app.route('/marcas/eliminar/<int:id>', methods=['GET'])
def eliminar_marca(id):
    marca = Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    flash('Marca eliminada con éxito.', 'success')
    return redirect(url_for('marcas'))

@app.route('/celulares', methods=['GET', 'POST'])
def celulares():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        modelo_nombre = request.form.get('modelo')
        fabricante_nombre = request.form.get('fabricante')
        proveedor_nombre = request.form.get('proveedor')
        marca_id = request.form.get('marca_id')
        stock_cantidad = request.form.get('stock_cantidad')
        stock_letra_almacen = request.form.get('stock_letra_almacen')
        stock_numero_almacen = request.form.get('stock_numero_almacen')
        accesorios_nombre = request.form.get('accesorios')
        caracteristicas_descripcion = request.form.get('caracteristicas')
        precio = request.form.get('precio')

        # Insertar o obtener ID para Modelo
        modelo = Modelo.query.filter_by(nombre=modelo_nombre).first()
        if not modelo:
            modelo = Modelo(nombre=modelo_nombre)
            db.session.add(modelo)
            db.session.commit()
        modelo_id = modelo.id

        # Insertar o obtener ID para Fabricante
        fabricante = Fabricante.query.filter_by(nombre=fabricante_nombre).first()
        if not fabricante:
            fabricante = Fabricante(nombre=fabricante_nombre)
            db.session.add(fabricante)
            db.session.commit()
        fabricante_id = fabricante.id

        # Insertar o obtener ID para Proveedor
        proveedor = Proveedor.query.filter_by(nombre=proveedor_nombre).first()
        if not proveedor:
            proveedor = Proveedor(nombre=proveedor_nombre)
            db.session.add(proveedor)
            db.session.commit()
        proveedor_id = proveedor.id

        # Insertar o obtener ID para Accesorios
        if accesorios_nombre:
            accesorio = Accesorios.query.filter_by(nombre=accesorios_nombre).first()
            if not accesorio:
                accesorio = Accesorios(nombre=accesorios_nombre)
                db.session.add(accesorio)
                db.session.commit()
            accesorios_id = accesorio.id
        else:
            accesorios_id = None

        # Insertar o obtener ID para Características
        if caracteristicas_descripcion:
            caracteristica = Car1.query.filter_by(descripcion=caracteristicas_descripcion).first()
            if not caracteristica:
                caracteristica = Car1(descripcion=caracteristicas_descripcion)
                db.session.add(caracteristica)
                db.session.commit()
            caracteristicas_id = caracteristica.id
        else:
            caracteristicas_id = None

        nuevo_equipo = Equipo(
            nombre=nombre,
            modelo_id=modelo_id,
            fabricante_id=fabricante_id,
            proveedor_id=proveedor_id,
            marca_id=marca_id,
            precio=precio,
            accesorios_id=accesorios_id,
            caracteristicas_id=caracteristicas_id
        )
        db.session.add(nuevo_equipo)
        db.session.commit()

        if stock_cantidad and stock_letra_almacen and stock_numero_almacen:
            nuevo_stock = Stock(
                cantidad=stock_cantidad,
                letra_almacen=stock_letra_almacen,
                numero_almacen=stock_numero_almacen,
                equipo_id=nuevo_equipo.id
            )
            db.session.add(nuevo_stock)
            db.session.commit()

        flash('Celular agregado exitosamente!')
        return redirect(url_for('celulares'))

    equipos = Equipo.query.all()
    marcas = Marca.query.all()
    return render_template('celulares.html', equipos=equipos, marcas=marcas)

@app.route('/editar_celular/<int:id>', methods=['GET', 'POST'])
def editar_celular(id):
    equipo = Equipo.query.get_or_404(id)
    
    if request.method == 'POST':
        # Actualizar campos del equipo
        equipo.nombre = request.form.get('nombre')
        equipo.precio = request.form.get('precio')

        # Obtener o crear Modelo
        modelo_nombre = request.form.get('modelo')
        modelo = obtener_o_crear(Modelo, nombre=modelo_nombre)
        equipo.modelo_id = modelo.id

        # Obtener o crear Fabricante
        fabricante_nombre = request.form.get('fabricante')
        fabricante = obtener_o_crear(Fabricante, nombre=fabricante_nombre)
        equipo.fabricante_id = fabricante.id

        # Obtener o crear Proveedor
        proveedor_nombre = request.form.get('proveedor')
        proveedor = obtener_o_crear(Proveedor, nombre=proveedor_nombre)
        equipo.proveedor_id = proveedor.id

        # Obtener o crear Accesorios
        accesorios_nombre = request.form.get('accesorios')
        accesorio = obtener_o_crear(Accesorios, nombre=accesorios_nombre) if accesorios_nombre else None
        equipo.accesorios_id = accesorio.id if accesorio else None

        # Obtener o crear Características
        caracteristicas_descripcion = request.form.get('caracteristicas')
        caracteristica = obtener_o_crear(Car1, descripcion=caracteristicas_descripcion) if caracteristicas_descripcion else None
        equipo.caracteristicas_id = caracteristica.id if caracteristica else None

        # Asignar Marca
        marca_id = request.form.get('marca_id')
        equipo.marca_id = marca_id

        db.session.commit()
        flash('Celular actualizado exitosamente!')
        return redirect(url_for('celulares'))

    # Consultar datos para el formulario
    modelos = Modelo.query.all()
    fabricantes = Fabricante.query.all()
    proveedores = Proveedor.query.all()
    accesorios = Accesorios.query.all()
    caracteristicas = Car1.query.all()
    marcas = Marca.query.all()

    return render_template('editar_celular.html', equipo=equipo, modelos=modelos, fabricantes=fabricantes, proveedores=proveedores, accesorios=accesorios, caracteristicas=caracteristicas, marcas=marcas)

def obtener_o_crear(modelo, **kwargs):
    """Obtiene una instancia del modelo o crea una nueva si no existe."""
    instancia = modelo.query.filter_by(**kwargs).first()
    if not instancia:
        instancia = modelo(**kwargs)
        db.session.add(instancia)
        db.session.commit()
    return instancia


@app.route('/eliminar_celular/<int:id>', methods=['GET'])
def eliminar_celular(id):
    equipo = Equipo.query.get(id)
    if equipo:
        # Eliminar fila en Stock
        Stock.query.filter_by(equipo_id=id).delete()
        # Eliminar la fila en Equipo
        db.session.delete(equipo)
        db.session.commit()
        flash('Celular eliminado exitosamente.', 'success')
    else:
        flash('Celular no encontrado.', 'error')
    return redirect(url_for('celulares'))

if __name__ == '__main__':
    app.run(debug=True)
