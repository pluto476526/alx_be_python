# Custom exception class

class ValueTooHighError(Exception) :
    def __init__(self, val) :
        self.val = val
        self.message = f"Value {val} is too high!"
        super().__init__(self.message)

def checkVal(val) :
    if val > 100 :
        raise ValueTooHighError(val)
    else :
        print(f"Value {val} is nice.")

if __name__ == "__main__" :
    try :
        input = int(input("Enter value... "))
        checkVal(input)
    except ValueTooHighError as e :
        print(e)
