from app import db

class Pedido(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id"),nullable=True)
    itens=db.relationship("ItemPedido",backref="pedido",cascade="all, delete-orphan")
    
    id_pagamento=db.Column(db.String(300),nullable=True)
    metodo=db.Column(db.String(50),nullable=True)
    link=db.Column(db.String(300),nullable=True)
    
    status=db.Column(db.String(100),nullable=False,default="PENDING")
    total=db.Column(db.Numeric(10,2),nullable=False)
    
class ItemPedido(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_pedido=db.Column(db.Integer,db.ForeignKey("pedido.id"),nullable=False)
    id_produto=db.Column(db.Integer,db.ForeignKey("produto.id"),nullable=False)
    quantidade=db.Column(db.Integer,nullable=False,default=1)
    preco=db.Column(db.Numeric(10,2),nullable=False)
    produto=db.relationship("Produto")