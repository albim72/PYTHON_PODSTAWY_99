class MyError(Exception):

    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wywołano konstruktor str")
        if self.message:
            return f"MyError, {self.message}"
        else:
            return f"klasa MyError jest już w użyciu"

raise MyError('Mamy problem.....')
