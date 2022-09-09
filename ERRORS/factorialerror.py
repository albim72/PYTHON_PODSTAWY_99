class NegativeErrorFactorial(Exception):

    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"wartość {self.n} jest ujemna. Silnia jest niezdefiniowana dla liczb ujemnych!"
