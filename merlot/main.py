from flask import Flask
import os
from dotenv import load_dotenv
from merlot.routes.routes import bp

load_dotenv()
def create_app():
    merlot = Flask(__name__)
    merlot.register_blueprint(bp)  # registra a rota do WhatsApp
    return merlot

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "False").lower() == "true"  # Ativa debug se estiver no .env como DEBUG=true (ou True, ou TRUE)
    port = int(os.getenv("PORT", 8080))  # Usa porta do .env, ou 8080 se não estiver definida
    merlot = create_app()  
    merlot.run(debug=debug, port=port) 
