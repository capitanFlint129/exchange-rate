from views import get_exchange_rate


def setup_routes(app):
    app.router.add_get('/', get_exchange_rate)