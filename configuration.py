from routes.route import livros_routes


def configure_all(app):
    configure_routes(app)
    
def configure_routes(app):
	app.register_blueprint(livros_routes)
      