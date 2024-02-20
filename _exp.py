size = int(input("Enter the size of the square multiplication table: "))
for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            product = i * j
            row.append(product)
        print('\t'.join(map(str, row)))