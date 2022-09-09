class ContextManager:

    def __init__(self):
        print("inicjacja konstruktora init")
    def __enter__(self):
        print("inicjacja konstruktora enter")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("inicjacja konstrutora exit")

with ContextManager() as manager:
    print("to jest część wykonawcza programu z użyciem CM")
