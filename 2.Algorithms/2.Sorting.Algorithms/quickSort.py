#################################### QUICK SORT #####################################
# Quick sort performs better than Merge Sort & also uses the Divide and Conquer strategy
# Quick Sort work on the pivot point and then works the same way as Merge Sort
# Quick sort also have Time Complexity of O(n log n), and have a worst case complexity of 
# O(n^2) when the list is mostly already sorted
#####################################################################################

def quickSort(list, first, last):
    if first < last:
        pivotIdx = partition(list, first, last)
        
        quickSort(list, first, pivotIdx - 1)
        quickSort(list, pivotIdx + 1, last)
    
    
def partition(dataValues, first, last):
    pivotValue = dataValues[first]
    
    lowerIndex = first + 1
    upperIndex = last
    
    isDone = False
    while not isDone:
        
        # Increment the lower index
        while lowerIndex <= upperIndex and dataValues[lowerIndex] <= pivotValue:
            lowerIndex += 1
            
        # Decrement the upper index
        while dataValues[upperIndex] >= pivotValue and upperIndex >= lowerIndex:
            upperIndex -= 1
            
        if upperIndex < lowerIndex:
            isDone = True
        else:
            temp = dataValues[lowerIndex]
            dataValues[lowerIndex] = dataValues[upperIndex]
            dataValues[upperIndex] = temp
           
        
            # when the split point is found, exchange the pivot value
        temp = dataValues[first]
        dataValues[first] = dataValues[upperIndex]
        dataValues[upperIndex] = temp
        
        return upperIndex
     
def main():
    unsortedList  = [6, 20, 8, 19, 56, 23, 87, 49, 41, 54]
    print("Unsorted List: ", unsortedList)
    quickSort(unsortedList, 0, len(unsortedList) - 1)
    print("Sorted List: ", unsortedList)
    
if __name__ == "__main__":
    main()