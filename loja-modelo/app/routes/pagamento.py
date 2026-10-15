from flask import Blueprint, request, render_template, redirect, url_for
from app.models import Usuario, Produto, Carrinho, ItemCarrinho, Pedido, ItemPedido
from flask_login import login_required, current_user, login_user
from app.services import id_cliente_api_pagamento,gerar_pagamento,pegar_boleto,pegar_pix
from config import Config
from app import db
import os

pagamento_bp =Blueprint("pagamento",__name__)

@pagamento_bp.route("/", methods=["POST"])
@login_required
def finalizar():
    try:
        carrinho=Carrinho.query.filter_by(id_usuario=current_user.id).first()
        
        if not carrinho or not carrinho.itens:
            return render_template("erro.html",erro="Você não tem itens no carrinho!!")
            
        total=sum(i.preco*i.quantidade for i in carrinho.itens)
        pedido=Pedido(id_usuario=current_user.id,total=total,status="PENDING")
        
        db.session.add(pedido)
        db.session.flush()
        
        for item in carrinho.itens:
            item_pedido=ItemPedido(id_pedido=pedido.id,id_produto=item.id_produto,quantidade=item.quantidade,preco=item.preco,produto=item.produto)
            db.session.add(item_pedido)
            
        for item in carrinho.itens[:]:
            db.session.delete(item)
        
        db.session.commit()
        return redirect(url_for("pagamento.escolher_forma",id=pedido.id))
            
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)

@pagamento_bp.route("/escolherforma/<int:id>",methods=["POST","GET"])
@login_required
def escolher_forma(id):
    try:
        pedido=Pedido.query.filter_by(id=id,id_usuario=current_user.id).first_or_404()
        
        if request.method == "POST":
            metodo=request.form["metodo"]
            
            if pedido.id_pagamento:
                if pedido.metodo != metodo:
                    return render_template("erro.html", erro="Erro no método de pagamento!!")
            else:
                id_pagamento=gerar_pagamento(current_user.gateway_key,pedido.total,metodo)
                pedido.id_pagamento=id_pagamento
                pedido.metodo=metodo
                db.session.commit()
                
            if metodo == "BOLETO":
                boleto=pegar_boleto(pedido.id_pagamento)
                
                if not boleto:
                    return render_template("erro.html",erro="Erro ao gerar link do boleto!!")
                
                pedido.link=boleto
                db.session.commit()
                return redirect(boleto)
                
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return render_template("escolher_forma.html",total=pedido.total,pedido=pedido)
    
    