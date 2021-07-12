# The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0, and 1


def Fibonacci(n):
    if n <= 0:
        print("Invalid Number")
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
def main():
    print(Fibonacci(4))
    
if __name__ == "__main__":
    main()
    