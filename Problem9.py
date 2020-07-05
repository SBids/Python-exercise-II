# 9. Write a binary search function. It should take a sorted sequence and the item it is looking for. It should return
# the index of the item if found. It should return -1 if the item is not found.


def binary_search(seq, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if seq[mid] == x:
            return mid
        elif seq[mid] > x:
            return binary_search(seq, low, mid - 1, x)
        else:
            return binary_search(seq, mid + 1, high, x)
    else:
        return -1


sequence = [2, 3, 4, 5, 6, 7, 70, 80]
print(binary_search(sequence, 0, len(sequence)-1, 800))

