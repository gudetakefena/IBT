# day09/practice.py

import heapq

# 1. Build a Binary Search Tree (BST)
class Node:
    def init(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right) if root else []

# Insert values and print them in sorted order
bst_root = None
values = [7, 3, 9, 1, 5, 8, 10]
for val in values:
    bst_root = insert(bst_root, val)

print("BST In-Order Traversal (sorted):", inorder_traversal(bst_root))

# 2. Tree depth
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

print("Tree Depth:", height(bst_root))

# 3. Graph BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return visited

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print("BFS reachable vertices from A:", bfs(graph, 'A'))

# 4. Graph DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited

print("DFS visit order starting from A:", dfs(graph, 'A'))

# 5. Priority queue using heapq
tasks = [(2, 'task2'), (1, 'task1'), (5, 'task5'), (3, 'task3'), (4, 'task4')]
priority_queue = []

# Push tasks into the priority queue
for task in tasks:
    heapq.heappush(priority_queue, task)

print("Tasks popped in order of priority:")
while priority_queue:
    print(heapq.heappop(priority_queue))

# if name == "main":
#     pass