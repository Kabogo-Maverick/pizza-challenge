from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from server.extensions import db, migrate
from server.config import Config

# App-wide extensions
# db = SQLAlchemy()
# migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from server.controllers.restaurant_controller import restaurant_bp
    from server.controllers.pizza_controller import pizza_bp
    from server.controllers.restaurant_pizza_controller import restaurant_pizza_bp
    
    # Register blueprints
    app.register_blueprint(restaurant_bp)
    app.register_blueprint(pizza_bp)
    app.register_blueprint(restaurant_pizza_bp)

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Pizza API!"})

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555,debug=True)