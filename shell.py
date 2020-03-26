import bit

while True:
    text = input('bit > ')
    result, error = bit.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)