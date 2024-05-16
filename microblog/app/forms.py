from flask_wtf import FlaskForm
from flask import request
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo, Email, Length
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Юзернейм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
    

class RegistrationForm(FlaskForm):
    username = StringField('Юзернейм', validators=[DataRequired()])
    email = StringField('Имейл', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')
    
    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Такой юзернейм уже занят. Придумайте, пожалуйста, другой.')
        
    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Такой имейл уже занят. Укажите, пожалуйста, другой.')
        

class EditProfileForm(FlaskForm):
    username = StringField('Юзернейм', validators=[DataRequired()])
    about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
    submit = SubmitField('Сохранить')
    
    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = db.session.scalar(sa.select(User).where(
                User.username == self.username.data))
            if user is not None:
                raise ValidationError('Такой юзернейм уже занят. Придумайте, пожалуйста, другой.')
            

class EmptyForm(FlaskForm):
    submit = SubmitField('Подписаться')
    

class PostForm(FlaskForm):
    post = TextAreaField('Напишите что-нибудь', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Опубликовать')
    

class SearchForm(FlaskForm):
    q = StringField(('Найти'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)