from flask import Flask
from controllers import carrinho_controller

def adicionar_rotas_carrinho(app: Flask):
    app.add_url_rule('/carrinho', view_func=carrinho_controller.carrinho, methods=['GET', 'POST'])