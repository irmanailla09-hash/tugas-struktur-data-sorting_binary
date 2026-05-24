from typing import List, Optional
import math


class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class AdvancedSorter:
    def __init__(self):
        pass

    # =========================================================
    # 1. ARRAY MERGE SORT
    # (Virtual Sublists + Single tmpArray)
    # =========================================================
    def sort_array(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr

        tmp_array = [0] * len(arr)
        self._rec_merge_sort(arr, 0, len(arr) - 1, tmp_array)
        return arr

    def _rec_merge_sort(self, arr, first, last, tmp_array):
        if first >= last:
            return

        mid = (first + last) // 2

        self._rec_merge_sort(arr, first, mid, tmp_array)
        self._rec_merge_sort(arr, mid + 1, last, tmp_array)

        self._merge_virtual(arr, first, mid, last, tmp_array)

    def _merge_virtual(self, arr, left_start, mid, right_end, tmp_array):
        left = left_start
        right = mid + 1
        index = left_start

        # Merge dua virtual sublist
        while left <= mid and right <= right_end:

            # STABLE: gunakan <=
            if arr[left] <= arr[right]:
                tmp_array[index] = arr[left]
                left += 1
            else:
                tmp_array[index] = arr[right]
                right += 1

            index += 1

        # Sisa elemen kiri
        while left <= mid:
            tmp_array[index] = arr[left]
            left += 1
            index += 1

        # Sisa elemen kanan
        while right <= right_end:
            tmp_array[index] = arr[right]
            right += 1
            index += 1

        # Copy kembali ke array asli
        for i in range(left_start, right_end + 1):
            arr[i] = tmp_array[i]

    # =========================================================
    # 2. LINKED LIST MERGE SORT
    # (Fast-Slow + Dummy Merge)
    # =========================================================
    def sort_linked_list(
        self,
        head: Optional[ListNode]
    ) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        right_head = self._split_linked_list(head)
        left_head = head

        left_sorted = self.sort_linked_list(left_head)
        right_sorted = self.sort_linked_list(right_head)

        return self._merge_linked_lists(left_sorted, right_sorted)

    def _split_linked_list(
        self,
        head: ListNode
    ) -> Optional[ListNode]:

        midPoint = head
        curNode = head.next

        # Fast-slow pointer
        while curNode and curNode.next:
            midPoint = midPoint.next
            curNode = curNode.next.next

        right_head = midPoint.next
        midPoint.next = None

        return right_head

    def _merge_linked_lists(
        self,
        listA: Optional[ListNode],
        listB: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode(0)
        tail = dummy

        while listA and listB:

            # STABLE
            if listA.data <= listB.data:
                tail.next = listA
                listA = listA.next
            else:
                tail.next = listB
                listB = listB.next

            tail = tail.next

        # Sambungkan sisa node
        tail.next = listA if listA else listB

        return dummy.next

    # =========================================================
    # 3. QUICK SORT PARTITION
    # (Median-of-Three Pivot)
    # =========================================================
    def partition_quick(
        self,
        arr: List[int],
        first: int,
        last: int
    ) -> int:

        mid = (first + last) // 2

        # Median-of-three
        if arr[first] > arr[mid]:
            arr[first], arr[mid] = arr[mid], arr[first]

        if arr[first] > arr[last]:
            arr[first], arr[last] = arr[last], arr[first]

        if arr[mid] > arr[last]:
            arr[mid], arr[last] = arr[last], arr[mid]

        # Median dipindah ke first
        arr[first], arr[mid] = arr[mid], arr[first]

        pivot = arr[first]

        left = first + 1
        right = last

        while True:

            while left <= right and arr[left] <= pivot:
                left += 1

            while left <= right and arr[right] > pivot:
                right -= 1

            if left > right:
                break

            arr[left], arr[right] = arr[right], arr[left]

        # Tempatkan pivot ke posisi final
        arr[first], arr[right] = arr[right], arr[first]

        return right

    # =========================================================
    # QUICK SORT DENGAN DEPTH LIMITER
    # =========================================================
    def quick_sort(self, arr: List[int]) -> List[int]:

        if len(arr) <= 1:
            return arr

        max_depth = 2 * int(math.log2(len(arr)))

        self._quick_sort_recursive(
            arr,
            0,
            len(arr) - 1,
            0,
            max_depth
        )

        return arr

    def _quick_sort_recursive(
        self,
        arr,
        first,
        last,
        depth,
        max_depth
    ):

        if first >= last:
            return

        # Fallback ke merge sort
        if depth > max_depth:

            sub_arr = arr[first:last + 1]
            self.sort_array(sub_arr)

            for i in range(len(sub_arr)):
                arr[first + i] = sub_arr[i]

            return

        pivot_index = self.partition_quick(arr, first, last)

        self._quick_sort_recursive(
            arr,
            first,
            pivot_index - 1,
            depth + 1,
            max_depth
        )

        self._quick_sort_recursive(
            arr,
            pivot_index + 1,
            last,
            depth + 1,
            max_depth
        )


# =========================================================
# CONTOH PENGGUNAAN
# =========================================================

if __name__ == "__main__":

    sorter = AdvancedSorter()

    # ================= ARRAY =================
    arr = [9, 3, 7, 1, 8, 2, 5]

    print("Array sebelum sort:")
    print(arr)

    sorter.sort_array(arr)

    print("Setelah Merge Sort:")
    print(arr)

    # ================= QUICK SORT =================
    arr2 = [10, 4, 8, 1, 6, 2, 9]

    print("\nQuick Sort:")
    print(sorter.quick_sort(arr2))

    # ================= LINKED LIST =================
    head = ListNode(7)
    head.next = ListNode(3)
    head.next.next = ListNode(9)
    head.next.next.next = ListNode(1)

    sorted_head = sorter.sort_linked_list(head)

    print("\nLinked List setelah sort:")

    cur = sorted_head
    while cur:
        print(cur.data, end=" ")
        cur = cur.next