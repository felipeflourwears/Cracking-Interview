def sumArray(array):
    sum = 0
    for i in range(0, len(array), 1):
        sum += array[i]
        print(array[i])
    return sum
        

sum = sumArray([1, 2, 3, 4, 5])
print("Total Sum: ", sum)