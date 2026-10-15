from flask import Blueprint, request, render_template, redirect, url_for
from app.models import Usuario, Produto, Carrinho, ItemCarrinho
from app import db
from flask_login import login_required, current_user, login_user, logout_user
from app.services import id_cliente_api_pagamento

autenticacao_bp =Blueprint("autenticacao",__name__)

@autenticacao_bp.route("/login", methods=["POST","GET"])
def login():
    try:
        if current_user.is_authenticated:
            return redirect(url_for("loja.menu"))
        if request.method == "POST":
            nome=request.form["nome"]
            cpf=request.form["cpf"]
            
            usuario=Usuario.query.filter_by(nome=nome, cpf=cpf).first()
            if usuario:
                login_user(usuario)
                return redirect(request.referrer or "/")
                
    except Exception as erro:
        return render_template("erro.html", erro=erro)
    return render_template("login.html")

@autenticacao_bp.route("/cadastro", methods=["POST","GET"])
def cadastro():
    try:
        if current_user.is_authenticated:
            return redirect(url_for("loja.menu"))
        if request.method == "POST":
            nome=request.form["nome"]
            cpf=request.form["cpf"]
            
            usuario=Usuario(nome=nome,cpf=cpf,gateway_key=id_cliente_api_pagamento(nome,cpf),administrador=Usuario.query.count() == 0)
            db.session.add(usuario)
            db.session.commit()
            
            carrinho=Carrinho(id_usuario=usuario.id)
            db.session.add(carrinho)
            db.session.commit()
            
            login_user(usuario)
            
            return redirect(url_for("loja.menu"))
            
            return redirect(request.referrer or "/")
    except Exception as erro:
        return render_template("erro.html", erro=erro)
    return render_template("cadastro.html")
    
@autenticacao_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("loja.menu"))
    
    
    