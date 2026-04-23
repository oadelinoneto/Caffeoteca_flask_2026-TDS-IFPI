from flask import render_template, request, redirect, url_for

from models.produto_model import listar_produtos, obter_produto_por_id


def index():
    return render_template('index.html')


def login():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            return redirect(url_for('menu', username=username))

        return render_template('login.html')

    return render_template('login.html')


def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        username = request.form.get('username', '').strip()
        senha = request.form.get('password', '').strip()
        confirmacao = request.form.get('confirm_password', '').strip()

        if not username or not senha or senha != confirmacao:
            return render_template('cadastro.html')

        return redirect(url_for('login', username=username))

    return render_template('cadastro.html')


def menu():
    username = request.args.get('username', 'Guest')
    cart_ids = request.args.getlist('cart_id', type=int)
    return render_template(
        'menu.html',
        username=username,
        listaProdutos=listar_produtos(),
        cart_ids=cart_ids,
    )


def perfil_usuario():
    perfil = {
        'nome': request.args.get('nome', 'Visitante'),
        'username': request.args.get('username', 'guest'),
        'email': request.args.get('email', 'nao informado'),
        'membro_desde': 'Abril de 2026',
        'status': 'Conta ativa',
        'plano': 'Padrao'
    }

    return render_template('perfil_usuario.html', perfil=perfil)


def carrinho():
    produto_id = request.args.get('id', type=int)
    carrinho_ids = request.args.getlist('cart_id', type=int)

    if produto_id:
        carrinho_ids.append(produto_id)

    carrinho_itens = []
    for item_id in carrinho_ids:
        produto_encontrado = obter_produto_por_id(item_id)
        if produto_encontrado:
            carrinho_itens.append(produto_encontrado)

    return render_template('carrinho.html', carrinho=carrinho_itens, cart_ids=carrinho_ids)
