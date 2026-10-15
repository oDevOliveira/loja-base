from flask import Blueprint, request, render_template, redirect,url_for
from app.models import Produto, Carrinho, ItemCarrinho, Pedido
from app import db
from flask_login import login_required, current_user
from app.services import consultar_pagamentos

carrinho_bp =Blueprint("carrinho",__name__)

@carrinho_bp.route("/")
@login_required
def vizualizar_carrinho():
    try:
        pedidos=Pedido.query.filter_by(id_usuario=current_user.id).all()
        
        for p in pedidos:
            if p.id_pagamento:
                p.status=consultar_pagamentos(p)
        
        db.session.commit()
        
        carrinho=Carrinho.query.filter_by(id_usuario=current_user.id).first()
        
        total=sum(item.preco * item.quantidade for item in carrinho.itens)
    except Exception as erro:
        db.session.rollback()
        return render_template("carrinho.html",erro=erro)
    return render_template("carrinho.html",itens=carrinho.itens,total=total,pedidos=pedidos)

@carrinho_bp.route("/add/<int:id>")
@login_required
def add_carrinho(id):
    try:
        produto=Produto.query.get_or_404(id)
        carrinho=Carrinho.query.filter_by(id_usuario=current_user.id).first()
        
        item=ItemCarrinho(id_carrinho=carrinho.id,id_produto=produto.id,quantidade=int(request.args.get("quantidade",1)),preco=produto.preco)
        db.session.add(item)
        db.session.commit()
        
    except Exception as erro:
        return render_template("carrinho.html",erro=erro)
    return redirect(url_for("loja.menu"))

@carrinho_bp.route("/remover/<int:id>", methods=["POST","GET"])
@login_required
def rmv_carrinho(id):
    try:
        item=ItemCarrinho.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
    except Exception as erro:
        return render_template("carrinho.html",erro=erro)
    return redirect(url_for("carrinho.vizualizar_carrinho"))