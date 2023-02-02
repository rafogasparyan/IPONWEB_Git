def mergeSort(l):
    n = len(l)
    if n < 2:
        return

    mid = n // 2
    l1 = l[:mid]
    l2 = l[mid:]
    mergeSort(l1)
    mergeSort(l2)
    merge(l1, l2, l)


def merge(l1, l2, l):
    i, j = 0, 0
    print(i)
    while i + j < len(l):
        if j == len(l2) or (i < len(l1) and l1[i] < l2[j]):
            l[i + j] = l1[i]
            i += 1
        else:
            l[i + j] = l2[j]
            j += 1


# mergeSort([1, 10, 12, 4, 24, 18, 7])


def insertion(l: list):
    for i in range(1, len(l)):
        cur = l[i]
        j = i
        while j > 0 and l[j - 1] > cur:
            l[j] = l[j - 1]
            j -= 1
        l[j] = cur
    print(l)


# insertion([1, 10, 20, 5, 12, 43, 11])


def counting_sort(arr):
    n = len(arr)
    m = max(arr) + 1
    count = [0] * m
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1, m):
        count[i] += count[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    return output

# print(counting_sort([1, 10, 15, 5, 4, 12, 8, 15, 13, 7]))
