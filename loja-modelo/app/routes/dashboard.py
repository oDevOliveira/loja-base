from flask import Blueprint, request, render_template, redirect, url_for
from app.models import Usuario, Produto, Carrinho, ItemCarrinho, Pedido
from app import db
from flask_login import login_required, current_user, login_user
from app.services import id_cliente_api_pagamento,consultar_pagamentos
from config import Config
import os

dashboard_bp =Blueprint("dashboard",__name__)

@dashboard_bp.route("/")
@login_required
def dashboard_menu():
    try:
        if not current_user.administrador:
            return redirect(url_for("loja.menu"))
            
        produtos=Produto.query.all()
        
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return render_template("dashboardmenu.html",produtos=produtos)

@dashboard_bp.route("/add_produto", methods=["POST","GET"])
@login_required
def addproduto():
    try:
        if not current_user.administrador:
            return redirect(url_for("loja.menu"))
            
        if request.method == "POST":
            nome=request.form["nome"]
            estoque=request.form["estoque"]
            preco=request.form["preco"]
            categoria=request.form["categoria"]
            
            imagem=request.files.get("imagem")
            nome_imagem=None
            
            if imagem and imagem.filename:
                nome_imagem=imagem.filename
                imagem.save(os.path.join(Config.PRODUTO_DIR,nome_imagem))
            
            produto=Produto(nome=nome,estoque=estoque,preco=preco,categoria=categoria,imagem=nome_imagem)
            db.session.add(produto)
            db.session.commit()
            
            return redirect(url_for("dashboard.dashboard_menu"))
            
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return render_template("addproduto.html")
    
@dashboard_bp.route("/edit_produto/<int:id>", methods=["POST","GET"])
@login_required
def editproduto(id):
    try:
        if not current_user.administrador:
            return redirect(url_for("loja.menu"))
        
        produto=Produto.query.get_or_404(id)
        if request.method == "POST":
            nome=request.form["nome"]
            estoque=request.form["estoque"]
            preco=request.form["preco"]
            categoria=request.form["categoria"]
            
            imagem=request.files.get("imagem")
            nome_imagem=None
            
            if imagem and imagem.filename:
                if produto.imagem:
                    os.remove(os.path.join(Config.PRODUTO_DIR,produto.imagem))
                
                nome_imagem=imagem.filename
                imagem.save(os.path.join(Config.PRODUTO_DIR,nome_imagem))
                produto.imagem=nome_imagem
            
            produto.nome=nome
            produto.estoque=estoque
            produto.preco=preco
            produto.categoria=categoria
            
            db.session.commit()
            
            return redirect(url_for("dashboard.dashboard_menu"))
            
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return render_template("editproduto.html",produto=produto)

@dashboard_bp.route("/removerproduto/<int:id>",methods=["POST","GET"])
@login_required
def remover_produto(id):
    try:
        if not current_user.administrador:
            return redirect(url_for("loja.menu"))
        
        produto=Produto.query.get_or_404(id)
        
        if produto.imagem:
            os.remove(os.path.join(Config.PRODUTO_DIR,produto.imagem))
        
        db.session.delete(produto)
        db.session.commit()
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return redirect(url_for("dashboard.dashboard_menu"))
    
@dashboard_bp.route("/verpedidos")
@login_required
def ver_pedidos():
    try:
        if not current_user.administrador:
            return redirect(url_for("loja.menu")) 
        
        pedidos=Pedido.query.all()
        
        for p in pedidos:
            if p.id_pagamento:
                p.status=consultar_pagamentos(p)
        
        db.session.commit()
        
    except Exception as erro:
        db.session.rollback()
        return render_template("erro.html",erro=erro)
    return render_template("pedidos.html",pedidos=pedidos)