from flask import Flask
from routes import site_router, admin_router


app = Flask(__name__)

site_router.adicionar_rotas_site(app)
admin_router.adicionar_rotas_admin(app)