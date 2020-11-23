itemsList = [34, 54, 89, 74 ,12, 37, 98, 134]

def findItems(item, items):
    for i in range(0, len(items)):
        if item == items[i]:
            return i       
    return None    

def main():
    print(findItems(89, itemsList))
    print(findItems(444, itemsList))
    
if __name__ == "__main__":
    main()  