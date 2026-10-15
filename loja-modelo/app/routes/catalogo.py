from flask import Blueprint, request, render_template
from app.models import Produto
from flask_login import login_required

catalogo_bp =Blueprint("catalogo",__name__)

@catalogo_bp.route("/<string:categoria>", methods=["POST","GET"])
def categoria(categoria):
    try:
        produtos_categoria=Produto.query.filter(Produto.categoria == categoria).all()
        if request.method == "POST":
            pesquisa=request.form["pesquisa"]
            produtos_categoria=Produto.query.filter(Produto.categoria == categoria, Produto.nome.ilike(f"%{pesquisa}%")).all()
    except Exception as erro:
        return render_template("erro.html", erro=erro)
    return render_template("categoria.html",produtos=produtos_categoria)
    
@catalogo_bp.route("/produto/<int:id>")
@login_required
def produto(id):
    try:
        produto=Produto.query.get(id)
    except Exception as erro:
        return render_template("erro.html",erro=erro)
    return render_template("produto.html",produto=produto)