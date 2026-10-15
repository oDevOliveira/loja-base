from app import db
from flask_login import UserMixin

class Usuario(UserMixin, db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(200),nullable=False)
    cpf=db.Column(db.String(50),nullable=False)
    gateway_key=db.Column(db.String(300))
    
    administrador=db.Column(db.Boolean,nullable=False,default=False)