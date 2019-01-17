from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration( FlaskForm ) :
	username = StringField( 'Username',
							validators = [DataRequired(), Length( min = 2, max = 10 )] )
	email = StringField( 'Email',
						validators = [DataRequired(), Email()] )
	password = PasswordField( 'Password',
							validators = [DataRequired()] )
	confirm_password = PasswordField( 'Confirm Password',
							validators = [DataRequired(), EqualTo( 'password' ) ] )
	submit_button = SubmitField( 'Register' )

class Login( FlaskForm ) :
	email = StringField( 'Email',
						validators = [DataRequired(), Email()] )
	password = PasswordField( 'Password',
							validators = [DataRequired()] )
	remember_me = BooleanField( 'Remember Me' )
	login_button = SubmitField( 'Login' )
