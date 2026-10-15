import os

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI="sqlite:///loja.db"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    API_PAG_LINK=os.environ.get("API_PAG_LINK")
    API_PAG_KEY=os.environ.get("API_PAG_KEY")
    
    BASE_DIR=os.path.dirname(os.path.abspath(__file__))
    PRODUTO_DIR=os.path.join(BASE_DIR, 'app','static','img')