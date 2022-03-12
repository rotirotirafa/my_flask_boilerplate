from src.app import application
from src.settings import HOST, PORT

if __name__ == "__main__":
    application.run(HOST, PORT)
