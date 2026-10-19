from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('使用者名稱', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('電子郵件', validators=[DataRequired(), Email()])
    password = PasswordField('密碼', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('確認密碼', validators=[DataRequired(), EqualTo('password', message='兩次輸入的密碼不一致。')])
    submit = SubmitField('註冊')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('該使用者名稱已被使用。')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('該電子郵件已被註冊。')

class LoginForm(FlaskForm):
    username = StringField('使用者名稱', validators=[DataRequired()])
    password = PasswordField('密碼', validators=[DataRequired()])
    submit = SubmitField('登入')

class BookForm(FlaskForm):
    title = StringField('書名', validators=[DataRequired(), Length(max=150)])
    author = StringField('作者', validators=[DataRequired(), Length(max=100)])
    isbn = StringField('ISBN', validators=[Length(max=20)])
    publisher = StringField('出版社', validators=[Length(max=100)])
    submit = SubmitField('儲存')