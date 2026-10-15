from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()
lm=LoginManager()

def criar_app():
    app=Flask(__name__)
    
    app.config.from_object("config.Config")
    
    db.init_app(app)
    lm.init_app(app)
    lm.login_view="autenticacao.login"
    
    from app.routes import loja_bp, autenticacao_bp, dashboard_bp, catalogo_bp, carrinho_bp, pagamento_bp
    
    app.register_blueprint(loja_bp)
    app.register_blueprint(catalogo_bp, url_prefix="/catalogo")
    app.register_blueprint(carrinho_bp,url_prefix="/carrinho")
    app.register_blueprint(pagamento_bp,url_prefix="/pagamento")
    app.register_blueprint(autenticacao_bp,url_prefix="/autenticacao")
    app.register_blueprint(dashboard_bp,url_prefix="/dashboard")
    
    @lm.user_loader
    def carregar_usuario(id):
        from app.models import Usuario
        return db.session.get(Usuario,int(id))
    
    with app.app_context():
        db.create_all()
    
    return app
















