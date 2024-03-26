from flask import Flask, render_template, request, redirect, url_for
import connect as conexao

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Consulta o banco de dados para verificar se o usuário e senha estão corretos
    usuarios = conexao.consultar_usuarios()
    for user in usuarios:
        if user[1] == nome and user[2] == password:
            return redirect(url_for('success', nome=nome))
    
    # Se as informações estiverem erradas,será redirecionado para a página de login
    return redirect(url_for('failure'))

@app.route("/success/<nome>")
def success(nome):
    return f"<h1>Olá, {nome}! Login bem-sucedido.</h1>"

@app.route("/failure")
def failure():
    return "<h1>Credenciais inválidas. Tente novamente.</h1>"

if __name__=='__main__':
    app.run(host='0.0.0.0')