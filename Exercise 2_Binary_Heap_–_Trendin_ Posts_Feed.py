# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:57:48 2026

@author: turet
"""

import math
import copy


class TrendingHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _heapify_up(self, i):
        if i == 0:
            return

        parent = self._parent(i)

        if self.heap[parent][0] < self.heap[i][0]:
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            self._heapify_up(parent)

    def _max_heapify(self, i):
        largest = i
        left = self._left(i)
        right = self._right(i)

        if left < self.size() and self.heap[left][0] > self.heap[largest][0]:
            largest = left

        if right < self.size() and self.heap[right][0] > self.heap[largest][0]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._max_heapify(largest)

    def push(self, post_id, likes, timestamp):
        self.heap.append([likes, post_id, timestamp])
        self._heapify_up(self.size() - 1)

    def pop_max(self):
        if self.size() == 0:
            return None

        max_post = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        if self.size() > 0:
            self._max_heapify(0)

        return max_post

    def peek_max(self):
        if self.size() == 0:
            return None
        return self.heap[0]

    def get_top_k(self, k):
        temp = copy.deepcopy(self)
        result = []
        for _ in range(min(k, temp.size())):
            result.append(temp.pop_max())
        return result

    def update_likes(self, post_id, new_likes, timestamp):
        for i in range(self.size()):
            if self.heap[i][1] == post_id:
                old_likes = self.heap[i][0]
                self.heap[i] = [new_likes, post_id, timestamp]
                if new_likes > old_likes:
                    self._heapify_up(i)
                elif new_likes < old_likes:
                    self._max_heapify(i)
                return

    def is_valid_heap(self):
        for i in range(self.size() // 2):
            left = self._left(i)
            right = self._right(i)
            if left < self.size() and self.heap[i][0] < self.heap[left][0]:
                return False
            if right < self.size() and self.heap[i][0] < self.heap[right][0]:
                return False
        return True

    def get_height(self):
        if self.size() == 0:
            return 0
        return int(math.floor(math.log2(self.size())))

    def get_level_order(self):
        result = []
        start = 0
        count = 1

        while start < self.size():
            level = []
            for i in range(start, min(start + count, self.size())):
                level.append(self.heap[i])
            result.append(level)
            start += count
            count *= 2

        return result


# ===== TEST =====
heap = TrendingHeap()

heap.push("A", 100, 1)
heap.push("B", 50, 2)
heap.push("C", 200, 3)
heap.push("D", 150, 4)

print("Heap:", heap.heap)
print("Max:", heap.peek_max())
print("Pop max:", heap.pop_max())
print("Heap after pop:", heap.heap)

print("Top 2:", heap.get_top_k(2))

heap.update_likes("B", 180, 5)
print("After update:", heap.heap)

print("Is valid heap:", heap.is_valid_heap())
print("Height:", heap.get_height())
print("Level order:", heap.get_level_order())