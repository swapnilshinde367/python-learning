from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration, Login

objFlask = Flask( '__name__' )

objFlask.config['SECRET_KEY'] = 'TISSECRETKEY'

posts = [
		{
			'title' : 'ABC',
			'age'	: 21,
			'author' : 'John',
			'date_posted' : '28 Jan 2001',
			'content' : 'Test Content 1'
		},
		{
			'title' : 'XYZ',
			'age'	: 25,
			'author' : 'Randy',
			'date_posted' : '07 Feb 2000',
			'content' : 'Test Content 2'
		}
	]

@objFlask.route( '/' )
@objFlask.route( '/home' )
def home() :
	return render_template( 'home.html', posts = posts, title = 'Home' )

@objFlask.route( '/about' )
def about() :
	return render_template( 'about.html', title = 'About' )

@objFlask.route( '/register', methods = ['GET', 'POST'] )
def register() :
	form = Registration()
	if form.validate_on_submit() :
		flash( f'Account created for {form.username.data}!', 'success' )
		return redirect( url_for( 'home' ) )
	return render_template( 'register.html', title = 'Register', form = form )

@objFlask.route( '/login', methods = ['GET', 'POST'] )
def login() :
	form = Login()
	if form.validate_on_submit() :
		if 'test@test.com' == form.email.data and 'password' == form.password.data :
			flash( f'Logged in!', 'success' )
			return redirect( url_for( 'home' ) )
		else :
			flash( f'Username/Password is incorrect', 'danger' )

	return render_template( 'login.html', title = 'Login', form = form )

if __name__ == '__main__' :
	objFlask.debug = True
	objFlask.run()