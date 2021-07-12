MAX = 3

def getExcelColumnName(number):
    string = ["\0"] * MAX 
    i = 0;   
    while number > 0:
        rem = number%26
           
        if rem == 0:
            string[i] = 'Z'
            i += 1
            number = int((number / 26) - 1)
        else:
            string[i] = chr((rem - 1) + ord('A'))
            i += 1
            number = int(number / 26)
    string[i] = '\0'       
    return "".join(string[::-1])

def main():
    input = 52
    name = getExcelColumnName(input)
    print("Excel column name for", input, "is", name)


if __name__ == "__main__":
    main()