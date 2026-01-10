from flask import Flask
from backend.routes.leads import leads_bp
from backend.routes.testimonials import testimonials_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(leads_bp)
    app.register_blueprint(testimonials_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
