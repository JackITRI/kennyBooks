from flask import Flask
from config import Config
from extensions import db, login_manager, csrf  # 1. 匯入 csrf
from routes.auth import auth_bp
from routes.books import books_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化擴充套件
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)  # 2. 初始化 csrf，這會在全局 Jinja2 注入 csrf_token() 函式

    # 註冊藍圖
    app.register_blueprint(auth_bp)
    app.register_blueprint(books_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    