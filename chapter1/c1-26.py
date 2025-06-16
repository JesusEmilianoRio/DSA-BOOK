def validate():
    a = int(input("Write A value:"))
    b = int(input("Write B value:"))
    c = int(input("Write C value:"))

    if (a + b) == c:
        print("a + b = c is True")
    else:
        print("a + b = c is False")
    if (b - c) == a:
        print("b - c = a is True")
    else:
        print("b - c = a is False")
    if (a * b) == c:
        print("a * b = c is True")
    else:
        print("a * b = c is False")

validate()
    
