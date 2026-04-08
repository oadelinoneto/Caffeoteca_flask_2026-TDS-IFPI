from flask import render_template, request, session
from models.produto_model import listaProdutos


def carrinho():
    produto_id = request.args.get('id', type=int)
    carrinho_ids = session.get('carrinho_ids', [])

    if produto_id:
        carrinho_ids.append(produto_id)
        session['carrinho_ids'] = carrinho_ids

    carrinho_itens = []
    for item_id in carrinho_ids:
        produto_encontrado = None
        for produto in listaProdutos:
            if produto.id == item_id:
                produto_encontrado = produto
                break

        if produto_encontrado:
            carrinho_itens.append(produto_encontrado)

    return render_template('carrinho.html', carrinho=carrinho_itens)