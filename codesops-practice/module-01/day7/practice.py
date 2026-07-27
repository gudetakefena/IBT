# day07/practice.py

import time
from collections import deque

# 1. Big-O Analysis
# a. List index
# O(1) because it directly accesses the element at a given index.
def list_index_example(lst, index):
    return lst[index]

# b. Single loop
# O(n) because it involves iterating through the list once.
def single_loop_example(lst):
    for element in lst:
        print(element)

# c. Nested loop
# O(n^2) because there are two nested loops, which leads to n * n iterations.
def nested_loop_example(lst1, lst2):
    for element1 in lst1:
        for element2 in lst2:
            print(element1, element2)

# d. Dict lookup
# O(1) on average because dictionary lookups are based on hash tables.
def dict_lookup_example(dct, key):
    return dct.get(key)

# e. Binary search
# O(log n) because it reduces the search space by half with each iteration.
def binary_search_example(sorted_list, target):
    left, right = 0, len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# 2. List vs. Dict Lookup
def lookup_timing():
    fake_accounts_list = [f"account_{i}" for i in range(100000)]
    fake_accounts_dict = {f"account_{i}": True for i in range(100000)}

    start_time = time.time()
    find_in_list = fake_accounts_list[99999]  # Finding an account near the end
    list_time = time.time() - start_time

    start_time = time.time()
    find_in_dict = fake_accounts_dict.get("account_99999")
    dict_time = time.time() - start_time

    print(f"List lookup time: {list_time:.6f} seconds")
    print(f"Dict lookup time: {dict_time:.6f} seconds")

# 3. Stack implementation
class Stack:
    def init(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

def reverse_names(names):
    stack = Stack()
    for name in names:
        stack.push(name)

    reversed_names = []
    while not stack.is_empty():
        reversed_names.append(stack.pop())
    return reversed_names

# 4. Queue implementation using deque
def bank_service_line():
    queue = deque()
    customers = ["Customer 1", "Customer 2", "Customer 3", "Customer 4", "Customer 5"]

    # Enqueue customers
    for customer in customers:
        queue.append(customer)

    # Serve customers in order
    while queue:
        served_customer = queue.popleft()
        print(f"Serving {served_customer}")

# 5. Singly linked list implementation
class Node:
    def init(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def init(self):
        self.head = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

if name == "main":
    # Example usage:
    print("1. Big-O examples:")
    print(list_index_example([1, 2, 3, 4, 5], 2))  # Output: 3
    single_loop_example([1, 2, 3, 4, 5])
    nested_loop_example([1, 2], [3, 4])
    print(dict_lookup_example({'key': 'value'}, 'key'))  # Output: value
    print(binary_search_example([1, 2, 3, 4, 5], 3))  # Output: 2

    print("\n2. List vs. Dict Lookup:")
    lookup_timing()

    print("\n3. Reverse names:")
    names = ["Alice", "Bob", "Charlie"]
    print(reverse_names(names))  # Output: ['Charlie', 'Bob', 'Alice']

    print("\n4. Bank service line:")
    bank_service_line()

    print("\n5. Singly linked list:")
    linked_list = LinkedList()
    linked_list.push_front(10)
    linked_list.push_front(20)
    linked_list.push_front(30)
    linked_list.print_all()  # Output: 30, 20, 10