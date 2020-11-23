# Bubble sort in the most basic sorting algorithm.
# It is known as Bubble Sort because the largest number bubbles to the top of the list with each iteration
# Bubble sort has the Time Complexity of O(n^2), which is quadratic and is NOT considered to be a practical solution

def bubbleSort(list):
    # For the top forloop we start with the n-1 times the number of items in the list and decrement by 1
    for i in range(len(list) - 1, 0, -1):
        # for inner loop, we compare the item with it's next item and swap if the item is larger then it's next item
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    
        print("Current State: ", list)
    
    
def main():
    unsortedList  = [6, 20, 8, 19, 56, 23, 87, 49, 41, 54]
    
    print("Unsorted List: ", unsortedList)
    bubbleSort(unsortedList)
    print("Sorted List: ", unsortedList)

if __name__ == "__main__":
    main()