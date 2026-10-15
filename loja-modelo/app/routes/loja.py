from flask import Blueprint, request, render_template
from app.models import Produto
from app import db

loja_bp =Blueprint("loja",__name__)

@loja_bp.route("/", methods=["POST","GET"])
def menu():
    try:
        categorias=db.session.query(Produto.categoria).distinct().all()
        produtos=Produto.query.all()
        if request.method == "POST":
            pesquisa=request.form["pesquisa"]
            
            produtos=Produto.query.filter(Produto.nome.ilike(f"%{pesquisa}%")).all()
    except Exception as erro:
        return render_template("erro.html", erro=erro)
    return render_template("menu.html",produtos=produtos,categorias=categorias)