class Algorithms:

    @staticmethod
    def bubble_sort(arr):
        """
        Bubble Sort:
        Repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    @staticmethod
    def selection_sort(arr):
        """
        Selection Sort:
        Divides the input list into two parts: the sublist of items already sorted and the sublist of items remaining
        to be sorted.
        """
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    @staticmethod
    def insertion_sort(arr):
        """
        Insertion Sort:
        Builds the final sorted array one item at a time.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    @staticmethod
    def merge_sort(arr):
        """
        Merge Sort:
        Divides the unsorted list into n sublists, each containing one element, then repeatedly merges sublists
        to produce sorted ones until there's only one sublist remaining.
        """
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            Algorithms.merge_sort(left_half)
            Algorithms.merge_sort(right_half)

            i, j, k = 0, 0, 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
        return arr

    @staticmethod
    def quick_sort(arr):
        """
        Quick Sort:
        It works by selecting a 'pivot' element and partitioning the other elements into two sub-arrays, according to
        whether they are less than or greater than the pivot.
        """
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return Algorithms.quick_sort(left) + middle + Algorithms.quick_sort(right)

    @staticmethod
    def linear_search(arr, x):
        """
        Linear Search:
        Sequentially checks each element of the list until a match is found or the whole list has been searched.
        """
        for i in range(len(arr)):
            if arr[i] == x:
                return i
        return -1

    @staticmethod
    def binary_search(arr, x):
        """
        Binary Search:
        Searches a sorted array by repeatedly dividing the search interval in half.
        """
        l = 0
        h = len(arr) - 1
        mid = 0

        while l <= h:
            mid = (h + l) // 2

            if arr[mid] < x:
                l = mid + 1

            elif arr[mid] > x:
                h = mid - 1

            else:
                return mid

        return -1

# Example Usage
algo = Algorithms()
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", arr)
print("Bubble Sorted:", algo.bubble_sort(arr.copy()))
print("Selection Sorted:", algo.selection_sort(arr.copy()))
print("Insertion Sorted:", algo.insertion_sort(arr.copy()))
print("Merge Sorted:", algo.merge_sort(arr.copy()))
print("Quick Sorted:", algo.quick_sort(arr.copy()))

search_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Linear Search (Find 7):", algo.linear_search(search_arr, 7))
print("Binary Search (Find 7):", algo.binary_search(search_arr, 7))
