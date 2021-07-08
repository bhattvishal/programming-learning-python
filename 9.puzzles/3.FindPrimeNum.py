def IsPrime(number):
    if number == 1:
        return True
    if number == 2:
        return True
    
    # If given number is divisible by any number less than it, then it's not a Prime Number
    for n in range(2, number):        
        if (number%n == 0):
            return False
        return True
            
        
def main():
    for i in range(1, 10 + 1):
       if IsPrime(i):
           print(i, "is a PRIME NUMBER")
       else:
           print(i, "is NOT a PRIME NUMBER")  
    
if __name__ == "__main__":
    main()      