def quick_sort_recurrsive(arr, start, end):
    if start >= end:
        return
    partition_index = partition(arr, start, end)
    quick_sort_recurrsive(arr, start, partition_index-1)
    quick_sort_recurrsive(arr, partition_index+1, end)




def quick_sort_iterative():
    pass



def quick_sort(arr, start, end):
    if (start >= end):
        return;
    index = partition(arr,start,end)
    quick_sort(arr, start, index-1)
    quick_sort(arr, index+1, end)

def partition(arr, start, end) -> int:
    ###
    # two pointer approach
    # pivot                               v
    #        ex [10, 80, 30, 90, 40, 50, 70]
    #     L       ^
    #     R                           ^
    ###
    L = start  # Less then pivot
    R = end-1  # Greater then pivot
    # Always choose last index value as pivot
    pivot = arr[end]

    while(L>=R):
        print(arr)
        print(L, R)
        # Check for partition index (Where R and L Meet)
        if L >= R:
            arr[end], arr[L] = arr[L], arr[end]
            return L

        if arr[L] > pivot and arr[R] < pivot:
            # Swap
            arr[L], arr[R] = arr[R], arr[L]
            R-=1
            L+=1

        else:
            if arr[R] > pivot:
                R-=1
            elif arr[L] <= pivot:
                L+=1


arr = [10, 80, 30, 90, 40, 50, 70]
quick_sort_recurrsive(arr, 0, len(arr)-1)
print(arr)