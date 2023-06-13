# importando os módulos da biblioteca flask
from flask import Flask , render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():

    name = "Quebra cranio" # escreva seu nome
    age  = "14" # escreva sua idade

    return render_template('index.html' , name = name , age = age)

# defina a rota para a página do pai
@app.route("/pai")
def pai():

    nome = "Duende do papai noel" # escreva seu nome
    idade  = "76" # escreva sua idade

    return render_template('pai.html' , nome = nome, idade = idade)

# defina a rota para a página da mãe
@app.route("/mae")
def mae():

    nome = "Golddigger" # escreva seu nome
    idade  = "27" # escreva sua idade

    return render_template('mae.html' , nome = nome, idade = idade)


# defina a rota para a página do amigo
@app.route("/amigo")
def amigo():

    nome = "Chupa cabra" # escreva seu nome
    idade  = "9" # escreva sua idade

    return render_template('amigo.html' , nome = nome, idade = idade)


# adicione outras rotas, se você quiser




# execute o arquivo
if __name__  ==  '__main__':
    app.run(debug=True)
