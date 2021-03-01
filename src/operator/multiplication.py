def advanced_multiplication(func):
    def inner(a, b):
        if a == 0 or b == 0:
            print("You must enter number greater than 0")
            return
        return func(a, b)

    return inner


@advanced_multiplication
def multiplication(a, b):
    return float(a) * float(b)
