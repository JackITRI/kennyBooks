
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect  # 1. 匯入 CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_message = '請先登入以存取此頁面。'
login_message_category = 'warning'

csrf = CSRFProtect()  # 2. 建立 csrf 實例