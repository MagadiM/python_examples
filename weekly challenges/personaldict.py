personal_details = {}

entries = int(input("Number of entries: "))

for i in range(entries):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    personal_details[key] = value
print("The personal details dictionary", personal_details)
