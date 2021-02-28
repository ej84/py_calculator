def division(a, b):
    try:
        return round(float(b) / float(a), 9)
    except ZeroDivisionError as error:
        print('error: zero is not divisional: ', error)