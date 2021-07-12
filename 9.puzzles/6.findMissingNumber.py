# Find the missing number in the given list
# Example N=10, Given List [1, 2, 3, 4, 6, 7, 8, 9, 10]
# 5 is missing

def findMissingNumber(n, array):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i
    
    sum2 = 0
    for j in range(len(array)):
        sum2 += array[j]

    return sum1 - sum2

def main():
    output = findMissingNumber(10, [1, 2, 3, 4, 6, 7, 8, 9, 10])
    print(output)

if __name__ == "__main__":
    main()
