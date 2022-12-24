try:
    print("Calculator")
    print(10/0)
    print("Name error")
    while True:
        a = int(input("Vedyt 1 chyslo"))
        if (a == 0):
            break
        b = int(input("Vedyt 2 chyslo"))
        suma = input("Znak + and - and * and /")
        if (suma != "+" and suma != "-" and suma != "*" and suma != "/"):
            break
        if (suma == "+"):
            print(a + b)
        if (suma == "-"):
            print(a - b)
        if (suma == "*"):
            print(a * b)
        if (suma == "/"):
            if (b == 0):
                print("Ділити на  ")
            else:
                print(a / b)
except (NameError,ZeroDivisionError):
    print("На 0 ділити не можна ")




















