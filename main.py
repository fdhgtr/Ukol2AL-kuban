import random
array = [13,56,6,85,3,45,49,78,1,65]

def bubble_sort():
    n = len(array)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                return array

print(bubble_sort())
arraya = [78,26,58,7,5,98,43,63,4,2]
def is_sorted(arrayb):
    for i in range(1, len(arrayb)):
        if arrayb[i] < arrayb[i-1]:
            return False
    return True

def bogosort(arrayb):
    count = 0
    while not is_sorted(arrayb):
        random.shuffle(arrayb)
        count += 1
        print(f"Pokus {count}: {arrayb}")
    print(f"Sorted array after {count} shuffles: ")
    bogosort(arrayb)
    print("Bogo",arrayb)
    




            
