""" 
Bakery Product Catalog Application
This is a to build a simple small bakery website called Sweet Crumbs Bakery.
this project is just a very simple website. no authentication or add to order. 
"""


from flask import Flask, Blueprint
from config import Config
from extensions import db
from routes.pages import pages

app = Flask(__name__) # Initialize the Flask application
app.config.from_object(Config) # Load configuration from the config object





def create_app():
    db.init_app(app)
    
    
    
    with app.app_context():
        # Register blueprints
        app.register_blueprint(pages)
        
    
    
    
    
    
    
    
    
    return app





if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)