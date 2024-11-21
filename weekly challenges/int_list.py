int_list = []
a = int(input("Please number of items: "))

for i in range(a):
    item = int(input("Enter items: ".format(i+1)))
int_list.append(item)

print("List:",int_list)