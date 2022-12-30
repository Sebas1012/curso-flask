from flask import Flask, render_template, make_response, redirect, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Clave Secreta'

@app.route('/')
def index():
    user_ip = request.remote_addr
    session['user_ip'] = user_ip
    response = make_response(redirect('/user_ip'))
    return response

@app.route('/user_ip')
def user_ip():
    user_ip = session.get('user_ip')
    return render_template('user_ip.html', ip=user_ip)

