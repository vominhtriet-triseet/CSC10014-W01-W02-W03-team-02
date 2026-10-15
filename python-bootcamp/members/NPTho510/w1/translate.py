#insertion sort
def insertion_sort(array):
    n = len(array)
      
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    return array

a = [1, 3, 5, 2, 1, 4, 9, 3]
insertion_sort(a)
print(a)