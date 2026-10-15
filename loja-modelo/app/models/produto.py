from app import db

class Produto(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    nome=db.Column(db.String(150),nullable=False)
    estoque=db.Column(db.Integer,nullable=False,default=0)
    preco=db.Column(db.Numeric(10,2),nullable=False)
    categoria=db.Column(db.String(150),nullable=False)
    imagem=db.Column(db.String(250))
    