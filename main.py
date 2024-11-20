array = [13,56,6,85,3,45,49,78,1,65]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                return array

print(bubble_sort())


            
