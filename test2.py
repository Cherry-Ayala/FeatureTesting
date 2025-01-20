#make a quicksort function ```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


#function that reverses a binary tree
```python
def reverse_binary_tree(root):
    if root is None:
        return None
    # Swap the left and right child
    root.left, root.right = root.right, root.left
    # Recursively reverse the left and right subtrees
    reverse_binary_tree(root.left)
    reverse_binary_tree(root.right)
    return root
```

def add_two_nums(x,y):
    return x+y


#make a dijkstra function
def dijkstra(graph, start, end):
    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode
        unseenNodes.pop(minNode)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)
    if shortest_distance[end] != infinity:
        print('Shortest distance is ' + str(shortest_distance[end]))
        print('And the path is ' + str(path))


def multipy_3_nums(x,y,z):
    result = x*y*zdef multipy_3_nums(x, y, z):
    result = x * y * z
    return result