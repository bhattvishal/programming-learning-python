def findSum(number: int):
    sum = 0
    while(number > 0):
        sum = sum + number%10
        number = number//10        
    return sum

def main():
    input = 3409578034953
    print("Some of Digits:", input, "is",findSum(input))
    
if __name__ == "__main__":
    main()