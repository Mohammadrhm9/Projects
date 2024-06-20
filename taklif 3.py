
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2*i + 1  # left = 2i + 1
    right = 2*i + 2  # right = 2i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

if __name__ == "__main__":
    # دریافت داده‌ها از ورودی
    data = input("لطفاً داده‌ها را وارد کنید (با فاصله از هم جدا کنید): ")
    arr = list(map(int, data.split()))

    # مرتب‌سازی داده‌ها با استفاده از مرتب‌سازی هرمی
    heap_sort(arr)

    # نمایش داده‌های مرتب شده
    print("داده‌های مرتب شده: ")
    print(arr)