# app/routes/main.py

from flask import Blueprint, render_template, request
main = Blueprint('main', __name__)

# ENRUTAMIENTO A index.html
@main.route('/')
def index():
    return render_template('index.html')

# ENRUTAMIENTO A login_form.html
@main.route('/login')
def login():
    return render_template('login_form.html')

#ENRUPTAMIENTO A register_form.html
@main.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Aquí puedes procesar los datos enviados
        usuario = request.form['usuario']
        email = request.form['email']
        password = request.form['password']
        # Aquí iría la lógica de guardado en la base de datos
        print(f"Registrando usuario: {usuario}, {email}")
        return "Registro exitoso"
    return render_template('register_form.html')