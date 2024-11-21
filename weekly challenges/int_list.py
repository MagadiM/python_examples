int_list = []
n = int(input("Please number of items: "))

for i in range(0, n):
    item = int(input())
    
    int_list.append(item)

print(int_list)
print(sum(int_list))

