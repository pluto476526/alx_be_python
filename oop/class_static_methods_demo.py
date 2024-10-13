class Calculator:

    calcType = "Arithmetic Operations"

    @staticmethod
    def add(a:int, b:int):
        return a + b

    @classmethod
    def multiply(cls, a:int, b:int):
        print(f"Calculation Type: {cls.calcType}")
        return a * b
