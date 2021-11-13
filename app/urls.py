import views


def add_url(app):
    app.add_url_rule('/', view_func=views.index, methods=['GET', 'POST'])
    app.add_url_rule('/docs', view_func=views.docs, methods=['GET', 'POST'])

    return app
