from app import db

class Carrinho(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_usuario=db.Column(db.Integer,db.ForeignKey("usuario.id"),nullable=True)
    itens=db.relationship("ItemCarrinho",backref="carrinho",cascade="all, delete-orphan")
    
class ItemCarrinho(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    id_carrinho=db.Column(db.Integer,db.ForeignKey("carrinho.id"),nullable=False)
    id_produto=db.Column(db.Integer,db.ForeignKey("produto.id"),nullable=False)
    quantidade=db.Column(db.Integer,nullable=False,default=1)
    preco=db.Column(db.Numeric(10,2),nullable=False)
    produto=db.relationship("Produto")