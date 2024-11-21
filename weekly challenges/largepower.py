def largePower(base, exponent):
    result = base ** exponent
    print(result)

    if result > 5000:
        print("True")
    else:
        print("False")

largePower(3, 12)