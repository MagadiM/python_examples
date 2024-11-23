try:
    with open("trialfile.txt", 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("The file is not available.")