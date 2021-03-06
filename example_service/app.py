import os
from flask import Flask
from konfig import Config
from example_service.endpoints import blueprints


def create():
    settings = os.path.join(os.path.dirname(__file__), 'settings.ini')
    settings = os.environ.get('FLASK_SETTINGS', settings)

    app = Flask(__name__)
    app.config_file = Config(settings)
    app.config.update(app.config_file.get_map('flask'))

    for blueprint in blueprints:
        app.register_blueprint(blueprint['pkg'],
                               url_prefix=blueprint['prefix'])

    return app


if __name__ == '__main__':
    app = create()
    app.run()
