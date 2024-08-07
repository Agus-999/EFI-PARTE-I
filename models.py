from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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

    equipo = db.relationship('Equipo', backref=db.backref('stock', uselist=False))

class Accesorio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(80), nullable=False)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipo.id'), nullable=False)

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    modelo_id = db.Column(db.Integer, db.ForeignKey('modelo.id'), nullable=False)
    fabricante_id = db.Column(db.Integer, db.ForeignKey('fabricante.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id', ondelete='CASCADE'), nullable=False)
    
    modelo = db.relationship('Modelo', backref=db.backref('equipos', lazy=True))
    fabricante = db.relationship('Fabricante', backref=db.backref('equipos', lazy=True))
    proveedor = db.relationship('Proveedor', backref=db.backref('equipos', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('equipos', lazy=True, passive_deletes=True))
    accesorios = db.relationship('Accesorio', backref='equipo', lazy=True)

class Car1(db.Model):  # Renombrado de Caracteristica a Car1
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
