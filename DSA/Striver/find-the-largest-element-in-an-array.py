"""
Given an array, we have to find the largest element in the array
"""
# Function to sort the array and return the largest element
def sortArr(arr):
    max = arr[0]

    for i in arr:
        if max < i:
            max = i
    return max

# Driver code
if __name__ == "__main__":
    # Initialize arrays
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    
    # Find and output the largest element in both arrays
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))