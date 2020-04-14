from app import app
from importlib.machinery import SourceFileLoader


# Import the helpers module
app_module = SourceFileLoader('*', './app/app.py').load_module()

if __name__ == "__main__":
        app_module.app.run()
