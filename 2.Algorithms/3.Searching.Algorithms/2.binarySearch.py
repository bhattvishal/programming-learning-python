#TODO: Need to add explanations

itemsList = [6, 14, 34, 56, 76, 78, 82, 88, 97, 107, 156]

def findItem(item, items):
    lowerIdx = 0
    upperIdx = len(items) - 1
    while(lowerIdx <= upperIdx):
        midIdx = (lowerIdx + upperIdx) // 2
        
        if items[midIdx] == item:
            return midIdx
        
        if item < items[midIdx]:
            upperIdx = midIdx + 1
        else:   
            lowerIdx = midIdx - 1
            
        if lowerIdx > upperIdx:
            return None

def main():
    print(findItem(56, itemsList))
    print(findItem(88, itemsList))
    print(findItem(250, itemsList))
    
if __name__ == "__main__":
    main()