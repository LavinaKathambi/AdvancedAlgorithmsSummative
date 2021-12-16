# PYTHON ALGORITHM FOR SUMMING NUMBERS IN A RANGE 
inputNumber = int(input("Input a number for maximum range: "))
# Initialize sum of elements to be 0 at the beginning
totalSum = 0
# loop through the range of array elements 
# Increament the values to the total sum
for num in range(1, inputNumber + 1):
    # Increament the values to the total sum
    totalSum = totalSum + num
# Return the final total sum
print(totalSum)