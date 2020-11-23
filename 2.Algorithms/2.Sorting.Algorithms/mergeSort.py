#################################### MERGE SORT #####################################
# Merge sort is better than the Bubble Sort and it uses the Divide and Conquer strategy
# Merge sort divides the list in smaller lists work on them and then merges them
# Merge sort have Time Complexity of O(n log n), which is logarithmic complexity
#####################################################################################

def mergeSort(list):
    if len(list) > 1:
        mid = len(list) // 2
        leftArray = list[:mid]
        rightArray = list[mid:]
        
        # We will now call the function recursively on both arrays until the length of 
        # list in > 1
        mergeSort(leftArray)
        mergeSort(rightArray)
        
        i = 0 # holds the current index of left array
        j = 0 # holds the current index of right array
        k = 0 # holds the current index of merged array
        
        # Merge the arrays
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                list[k] = leftArray[i]
                i+=1
            else:
                list[k] = rightArray[j]
                j+=1
            k += 1
               
        # if there are still values in the left array, lets add them in the merged array       
        while i < len(leftArray):
            list[k] = leftArray[i]
            i += 1
            k += 1


        # if there are still values in the right array, lets add them in the merged array
        while j < len(rightArray):
            list[k] = rightArray[j]
            j += 1
            k += 1    
    
def main():
    unsortedList  = [6, 20, 8, 19, 56, 23, 87, 49, 41, 54]
    
    print("Unsorted List: ", unsortedList)
    mergeSort(unsortedList)
    print("Sorted List: ", unsortedList)
    
if __name__ == "__main__":
    main()