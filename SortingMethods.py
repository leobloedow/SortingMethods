import random as r
import time as t

for i in range(10):
    print(f"\nExecução: {i + 1}")

    print("Gerando listas em ordem crescente sem valores repetidos")

    list1 = list(range(128))
    list2 = list(range(256))
    list3 = list(range(512))
    list4 = list(range(1024))
    list5 = list(range(2048))
    list6 = list(range(4096))
    list7 = list(range(8192))
    list8 = list(range(16384))
    list9 = list(range(32768))
    list10 = list(range(65536))

    print("Gerando listas em ordem decrescente sem valores repetidos")

    list11 = sorted(list1, reverse=True)
    list12 = sorted(list2, reverse=True)
    list13 = sorted(list3, reverse=True)
    list14 = sorted(list4, reverse=True)
    list15 = sorted(list5, reverse=True)
    list16 = sorted(list6, reverse=True)
    list17 = sorted(list7, reverse=True)
    list18 = sorted(list8, reverse=True)
    list19 = sorted(list9, reverse=True)
    list20 = sorted(list10, reverse=True)

    print("Gerando listas aleatórias sem valores repetidos")

    list21 = r.sample(list1, len(list1))
    list22 = r.sample(list2, len(list2))
    list23 = r.sample(list3, len(list3))
    list24 = r.sample(list4, len(list4))
    list25 = r.sample(list5, len(list5))
    list26 = r.sample(list6, len(list6))
    list27 = r.sample(list7, len(list7))
    list28 = r.sample(list8, len(list8))
    list29 = r.sample(list9, len(list9))
    list30 = r.sample(list10, len(list10))

    print("Gerando listas aleatórias com valores repetidos")

    list31 = [r.randint(1, 1000) for i in range(len(list1))]
    list32 = [r.randint(1, 1000) for i in range(len(list2))]
    list33 = [r.randint(1, 1000) for i in range(len(list3))]
    list34 = [r.randint(1, 1000) for i in range(len(list4))]
    list35 = [r.randint(1, 1000) for i in range(len(list5))]
    list36 = [r.randint(1, 1000) for i in range(len(list6))]
    list37 = [r.randint(1, 1000) for i in range(len(list7))]
    list38 = [r.randint(1, 1000) for i in range(len(list8))]
    list39 = [r.randint(1, 1000) for i in range(len(list9))]
    list40 = [r.randint(1, 1000) for i in range(len(list10))]


    def bubble_sort(list_):
        start_time = t.perf_counter_ns()
        n = len(list_)
        for i in range(n - 1):
            for i2 in range(n - i - 1):
                if list_[i2] > list_[i2 + 1]:
                    list_[i2], list_[i2 + 1] = list_[i2 + 1], list_[i2]
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")


    def insertion_sort(list_):
        start_time = t.perf_counter_ns()
        for i in range(1, len(list_)):
            key = list_[i]
            j = i - 1
            while j >= 0 and key < list_[j]:
                list_[j + 1] = list_[j]
                j -= 1
            list_[j + 1] = key
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")


    def selection_sort(list_):
        start_time = t.perf_counter_ns()
        n = len(list_)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if list_[min_idx] > list_[j]:
                    min_idx = j
            list_[i], list_[min_idx] = list_[min_idx], list_[i]
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")


    def heap_sort(list_):
        start_time = t.perf_counter_ns()
        n = len(list_)
        for i in range(n // 2 - 1, -1, -1):
            heapify(list_, n, i)
        for i in range(n - 1, 0, -1):
            list_[i], list_[0] = list_[0], list_[i]
            heapify(list_, i, 0)
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")


    def heapify(list_, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and list_[l] > list_[largest]:
            largest = l
        if r < n and list_[r] > list_[largest]:
            largest = r
        if largest != i:
            list_[i], list_[largest] = list_[largest], list_[i]
            heapify(list_, n, largest)


    def shell_sort(list_):
        start_time = t.perf_counter_ns()
        n = len(list_)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = list_[i]
                j = i
                while j >= gap and list_[j - gap] > temp:
                    list_[j] = list
                    list_[j - gap]
                    j -= gap
                list_[j] = temp
            gap //= 2
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")


    def merge_sort(list_):
        start_time = t.perf_counter_ns()
        sorted_list = _merge_sort(list_)
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")
        return sorted_list


    def _merge_sort(list_):
        if len(list_) > 1:
            mid = len(list_) // 2
            left_half = list_[:mid]
            right_half = list_[mid:]

            _merge_sort(left_half)
            _merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    list_[k] = left_half[i]
                    i += 1
                else:
                    list_[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                list_[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                list_[k] = right_half[j]
                j += 1
                k += 1
        return list_


    def quick_sort(list_):
        start_time = t.perf_counter_ns()
        quick_sort_iterative(list_)
        end_time = t.perf_counter_ns()
        print(f"{end_time - start_time}")

    def quick_sort_iterative(list_):
        size = len(list_)
        stack = [(0, size - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pi = partition(list_, low, high)
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))

    def partition(list_, low, high):
        pivot = list_[high]
        i = low - 1
        for j in range(low, high):
            if list_[j] <= pivot:
                i += 1
                list_[i], list_[j] = list_[j], list_[i]
        list_[i + 1], list_[high] = list_[high], list_[i + 1]
        return i + 1



    print("Ordem crescente sem valores repetidos:\n")

    print("\nBubble Sort:\n\n")

    bubble_sort(list1)
    bubble_sort(list2)
    bubble_sort(list3)
    bubble_sort(list4)
    bubble_sort(list5)
    bubble_sort(list6)
    bubble_sort(list7)
    bubble_sort(list8)
    bubble_sort(list9)
    bubble_sort(list10)

    print("\nInsertion Sort:\n\n")

    insertion_sort(list1)
    insertion_sort(list2)
    insertion_sort(list3)
    insertion_sort(list4)
    insertion_sort(list5)
    insertion_sort(list6)
    insertion_sort(list7)
    insertion_sort(list8)
    insertion_sort(list9)
    insertion_sort(list10)

    print("\nSelection Sort:\n\n")

    selection_sort(list1)
    selection_sort(list2)
    selection_sort(list3)
    selection_sort(list4)
    selection_sort(list5)
    selection_sort(list6)
    selection_sort(list7)
    selection_sort(list8)
    selection_sort(list9)
    selection_sort(list10)

    print("\nHeap Sort:\n\n")

    heap_sort(list1)
    heap_sort(list2)
    heap_sort(list3)
    heap_sort(list4)
    heap_sort(list5)
    heap_sort(list6)
    heap_sort(list7)
    heap_sort(list8)
    heap_sort(list9)
    heap_sort(list10)

    print("\nShell Sort:\n\n")

    shell_sort(list1)
    shell_sort(list2)
    shell_sort(list3)
    shell_sort(list4)
    shell_sort(list5)
    shell_sort(list6)
    shell_sort(list7)
    shell_sort(list8)
    shell_sort(list9)
    shell_sort(list10)

    print("\nMerge Sort:\n\n")

    merge_sort(list1)
    merge_sort(list2)
    merge_sort(list3)
    merge_sort(list4)
    merge_sort(list5)
    merge_sort(list6)
    merge_sort(list7)
    merge_sort(list8)
    merge_sort(list9)
    merge_sort(list10)

    print("\nQuick Sort:\n\n")

    quick_sort(list1)
    quick_sort(list2)
    quick_sort(list3)
    quick_sort(list4)
    quick_sort(list5)
    quick_sort(list6)
    quick_sort(list7)
    quick_sort(list8)
    quick_sort(list9)
    quick_sort(list10)

    print("\nOrdem decrescente sem valores repetidos:\n")

    print("\nBubble Sort:\n\n")

    bubble_sort(list11)
    bubble_sort(list12)
    bubble_sort(list13)
    bubble_sort(list14)
    bubble_sort(list15)
    bubble_sort(list16)
    bubble_sort(list17)
    bubble_sort(list18)
    bubble_sort(list19)
    bubble_sort(list20)

    print("\nInsertion Sort:\n\n")

    insertion_sort(list11)
    insertion_sort(list12)
    insertion_sort(list13)
    insertion_sort(list14)
    insertion_sort(list15)
    insertion_sort(list16)
    insertion_sort(list17)
    insertion_sort(list18)
    insertion_sort(list19)
    insertion_sort(list20)

    print("\nSelection Sort:\n\n")

    selection_sort(list11)
    selection_sort(list12)
    selection_sort(list13)
    selection_sort(list14)
    selection_sort(list15)
    selection_sort(list16)
    selection_sort(list17)
    selection_sort(list18)
    selection_sort(list19)
    selection_sort(list20)

    print("\nHeap Sort:\n\n")

    heap_sort(list11)
    heap_sort(list12)
    heap_sort(list13)
    heap_sort(list14)
    heap_sort(list15)
    heap_sort(list16)
    heap_sort(list17)
    heap_sort(list18)
    heap_sort(list19)
    heap_sort(list20)

    print("\nShell Sort:\n\n")

    shell_sort(list11)
    shell_sort(list12)
    shell_sort(list13)
    shell_sort(list14)
    shell_sort(list15)
    shell_sort(list16)
    shell_sort(list17)
    shell_sort(list18)
    shell_sort(list19)
    shell_sort(list20)

    print("\nMerge Sort:\n\n")

    merge_sort(list11)
    merge_sort(list12)
    merge_sort(list13)
    merge_sort(list14)
    merge_sort(list15)
    merge_sort(list16)
    merge_sort(list17)
    merge_sort(list18)
    merge_sort(list19)
    merge_sort(list20)

    print("\nQuick Sort:\n\n")

    quick_sort(list11)
    quick_sort(list12)
    quick_sort(list13)
    quick_sort(list14)
    quick_sort(list15)
    quick_sort(list16)
    quick_sort(list17)
    quick_sort(list18)
    quick_sort(list19)
    quick_sort(list20)

    print("\nOrdem aleatória sem valores repetidos:\n")

    print("\nBubble Sort:\n\n")

    bubble_sort(list21)
    bubble_sort(list22)
    bubble_sort(list23)
    bubble_sort(list24)
    bubble_sort(list25)
    bubble_sort(list26)
    bubble_sort(list27)
    bubble_sort(list28)
    bubble_sort(list29)
    bubble_sort(list30)

    print("\nInsertion Sort:\n\n")

    insertion_sort(list21)
    insertion_sort(list22)
    insertion_sort(list23)
    insertion_sort(list24)
    insertion_sort(list25)
    insertion_sort(list26)
    insertion_sort(list27)
    insertion_sort(list28)
    insertion_sort(list29)
    insertion_sort(list30)

    print("\nSelection Sort:\n\n")

    selection_sort(list21)
    selection_sort(list22)
    selection_sort(list23)
    selection_sort(list24)
    selection_sort(list25)
    selection_sort(list26)
    selection_sort(list27)
    selection_sort(list28)
    selection_sort(list29)
    selection_sort(list30)

    print("\nHeap Sort:\n\n")

    heap_sort(list21)
    heap_sort(list22)
    heap_sort(list23)
    heap_sort(list24)
    heap_sort(list25)
    heap_sort(list26)
    heap_sort(list27)
    heap_sort(list28)
    heap_sort(list29)
    heap_sort(list30)

    print("\nShell Sort:\n\n")

    shell_sort(list21)
    shell_sort(list22)
    shell_sort(list23)
    shell_sort(list24)
    shell_sort(list25)
    shell_sort(list26)
    shell_sort(list27)
    shell_sort(list28)
    shell_sort(list29)
    shell_sort(list30)

    print("\nMerge Sort:\n\n")

    merge_sort(list21)
    merge_sort(list22)
    merge_sort(list23)
    merge_sort(list24)
    merge_sort(list25)
    merge_sort(list26)
    merge_sort(list27)
    merge_sort(list28)
    merge_sort(list29)
    merge_sort(list30)

    print("\nQuick Sort:\n\n")

    quick_sort(list21)
    quick_sort(list22)
    quick_sort(list23)
    quick_sort(list24)
    quick_sort(list25)
    quick_sort(list26)
    quick_sort(list27)
    quick_sort(list28)
    quick_sort(list29)
    quick_sort(list30)

    print("\nOrdem aleatória com valores repetidos:\n")

    print("\nBubble Sort:\n\n")

    bubble_sort(list31)
    bubble_sort(list32)
    bubble_sort(list33)
    bubble_sort(list34)
    bubble_sort(list35)
    bubble_sort(list36)
    bubble_sort(list37)
    bubble_sort(list38)
    bubble_sort(list39)
    bubble_sort(list40)

    print("\nInsertion Sort:\n\n")

    insertion_sort(list31)
    insertion_sort(list32)
    insertion_sort(list33)
    insertion_sort(list34)
    insertion_sort(list35)
    insertion_sort(list36)
    insertion_sort(list37)
    insertion_sort(list38)
    insertion_sort(list39)
    insertion_sort(list40)

    print("\nSelection Sort:\n\n")

    selection_sort(list31)
    selection_sort(list32)
    selection_sort(list33)
    selection_sort(list34)
    selection_sort(list35)
    selection_sort(list36)
    selection_sort(list37)
    selection_sort(list38)
    selection_sort(list39)
    selection_sort(list40)

    print("\nHeap Sort:\n\n")

    heap_sort(list31)
    heap_sort(list32)
    heap_sort(list33)
    heap_sort(list34)
    heap_sort(list35)
    heap_sort(list36)
    heap_sort(list37)
    heap_sort(list38)
    heap_sort(list39)
    heap_sort(list40)

    print("\nShell Sort:\n\n")

    shell_sort(list31)
    shell_sort(list32)
    shell_sort(list33)
    shell_sort(list34)
    shell_sort(list35)
    shell_sort(list36)
    shell_sort(list37)
    shell_sort(list38)
    shell_sort(list39)
    shell_sort(list40)

    print("\nMerge Sort:\n\n")

    merge_sort(list31)
    merge_sort(list32)
    merge_sort(list33)
    merge_sort(list34)
    merge_sort(list35)
    merge_sort(list36)
    merge_sort(list37)
    merge_sort(list38)
    merge_sort(list39)
    merge_sort(list40)

    print("\nQuick Sort:\n\n")

    quick_sort(list31)
    quick_sort(list32)
    quick_sort(list33)
    quick_sort(list34)
    quick_sort(list35)
    quick_sort(list36)
    quick_sort(list37)
    quick_sort(list38)
    quick_sort(list39)
    quick_sort(list40)

print("\n\n\nFim da execução!")