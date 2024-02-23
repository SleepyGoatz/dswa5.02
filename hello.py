# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():

    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Luis%20de%20Moura/PT3019861/IFSP-PTB">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'


@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):

    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: {nome}</h2><h2>Prontuário: {prontuario}</h2><h2>Instituição: {instituicao}</h2><a href="/">Voltar</a>'


@app.route('/contextorequisicao')
def contexto_requisicao():

    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host

    return f'<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {user_agent}</h2><h2>O IP do computador remoto é: {remote_ip}</h2><h2>O host da aplicação é: {host}</h2><a href="/">Voltar</a>'
