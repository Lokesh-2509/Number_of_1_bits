def count_one_bits(num):
    count = 0
    while num:
        if num & 1:
            count += 1
        num >>= 1
    return count
num = int(input("Enter a number: "))
result = count_one_bits(num)
print(result)

