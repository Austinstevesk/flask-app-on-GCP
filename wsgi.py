#Entry point of the application

#Imports the app initialized in app.py
from src.app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
