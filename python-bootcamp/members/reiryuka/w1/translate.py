#W1-4
#binary search on a sorted vector → return index or −1
def binary_search(a: list[int], key: int) -> int:
    """Python lists use dynamic typing."""
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if a[mid] == key:
            return mid

        if a[mid] < key:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


print(binary_search([1, 3, 5, 7, 9], 5))   # 2
print(binary_search([1, 3, 5, 7, 9], 4))   # -1