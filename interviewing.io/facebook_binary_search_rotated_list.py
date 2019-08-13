# Welcome to Facebook!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!

# Hello!

# find the index of X in a rotated sorted array.
# rotated sorted array:
# i.e.   [4, 5, 1, 2, 3]
# index  [            4]
#          ^
# find the index of 3 in this array. The output is 4.
# find the index of 2 in this array. The output is 3.

'''
binary search
len = 5
mid = 5/2
mid = 2
 [5, 1, 2, 3, 4]
        ^
 [4, 5, 1, 2, 3]
        ^
 [3, 4, 5, 1, 2]
        ^
start, end
mid
'''


def bin_search(arr, k):
    start = 0
    end = len(arr) - 1
    mid = (start + end) / 2

    while (start < end):
        mid = (start + end) / 2

        if arr[mid] == k:
            return mid

        elif arr[mid] > k:
            if mid + 1 < len(arr) - 1
                if arr[mid + 1] > k:
                    end = mid
                if arr[mid + 1] < k:
                    start = mid
            else:
                if arr[mid - 1] > k:
                    start = mid
                if arr[mid - 1] < k:
                    end = mid

        elif arr[mid] < k:
            if mid + 1 < len(arr) - 1
                if arr[mid + 1] > k:
                    start = mid
                if arr[mid + 1] < k:
                    end = mid
            else:
                if arr[mid - 1] > k:
                    end = mid
                if arr[mid - 1] < k:
                    start = mid


