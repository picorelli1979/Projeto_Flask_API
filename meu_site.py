# AQUI IMPORTAMOS A BIBLIOTECA DO FLASK , E AS TAMPLETES POR PADRÃO
from flask import Flask, render_template

# AQUI DEMOS UM NOME PARA NOSSA APLICAÇÃO QUE NO CASO É : APP
app = Flask(__name__)

# AQUI CRIAMOS A ROTA DA PAGINA INICIAL 
@app.route("/")
def homepage():  
    return render_template('homepage.html')

# AQUI CRIAMOS UMA ROTA DE USUARIOS(ESTATICA), OU SEJA UMA SEGUNDA PAGINA
@app.route("/cadastro/")
def cadastro():
    return render_template('cadastro.html')

# AQUI CRIAMOS UMA ROTA DE USUARIOS(DINAMICA), OU SEJA UMA SEGUNDA PAGINA
# AQUI SÃO 2 DECORETORS COMO EXEMPLO SE PASSAR O  NOME DO USUARIO E SE NÃO PASSAR O NOME DO USUARIO
@app.route("/usuario/", defaults = {'nome_usuario':None})
@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template('usuario.html', nome_usuario = nome_usuario)

# AQUI CRIAMOS UMA ROTA DE CONTATOS, OU SEJA UMA TERCEIRA PAGINA 
@app.route("/contatos/")
def lista_contatos():
    return render_template('lista_contatos.html')

# AQUI DIZEMOS O CAMINHO, OU SEJA SÓ PODERÁ RODAR AQUI DENTRO
if __name__ == '__main__':
    app.run(debug=True)
