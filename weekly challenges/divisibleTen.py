def divisible_by_ten(num):
    result = num % 10
    print(result)

    if result == 0:
        print("True")
    else:
        print("False")

divisible_by_ten(123)