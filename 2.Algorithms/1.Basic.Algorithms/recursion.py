# In this example we will use the concept of RECURSION
# to the the Power and the Factorial of a given Number

def calculatePower(number, power):
    if power == 0:
        return 1
    else:
        return number * calculatePower(number, power - 1)   


def calculateFactorial(number):
    if number == 0:
        return 1
    else:
        return number * calculateFactorial(number - 1)

def main():
    print("{0} to the power of {1} is: {2}".format(2, 3, calculatePower(2, 3))) 
    print("{0} to the power of {1} is: {2}".format(10, 2, calculatePower(10, 2))) 
    
    print("Factorial of {0} is: {1}".format(0, calculateFactorial(0))) 
    print("Factorial of {0} is: {1}".format(5, calculateFactorial(5))) 

if __name__ == "__main__":
    main()