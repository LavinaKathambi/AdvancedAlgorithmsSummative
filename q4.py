# PYTHON CODE FOR FINDING A SUPER DIGIT
def superDigit(n, k):
    # Define a function to get the sum of each digit in a given number
    def findSum(num):
        # check if super digit has been obtained
        if num  < 10: 
            # return number if criteria has been met
            return num  
        # else, if num is greater than 10 
        # find the sum of each value in the digit, by iterating through it 
        # iterate through the string and sum values as integers 
        s = sum(int(i) for i in str(num ))
        # recursively call the findSum function until the super digit is obtained
        return findSum(s)
    # call the findSum function on the given input n 
    x = findSum(int(n))
    # multiply the result by the given input k and recursively call the function again
    # this will go on until the value is less than 10, which is the super digit
    return findSum(k*x)

n = '9875'
k = 4
print(superDigit(n,k))



