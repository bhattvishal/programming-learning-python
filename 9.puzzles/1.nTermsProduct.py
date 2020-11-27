# Write a program which takes an integer input 'n' and returns the PRODUCT of the first 'n' terms of
# abra_ka_dabra series. Abra_ka_dabra series looks like following:

# (1+2+3), (2+3+4), (3+4+5), (4+5+6), ... 
# So, your method should return 6, 54, 648, 9720 for inputs 1,2,3,4 and so on...


def product(n):
    if n == 1:
        return 6
    else:
        return (n + (n+1) + (n+2)) * product(n - 1)
        
        
def main():
    print(product(1))    
    
if __name__ == "__main__":
    main()